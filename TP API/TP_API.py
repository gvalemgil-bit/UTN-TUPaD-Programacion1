import sqlite3
import sys
from contextlib import closing
import requests
from flask import Flask, jsonify, request

DB_PATH = "biblioteca.db"
URL_BASE = "http://127.0.0.1:5000"

app = Flask(__name__)

#EJERCICIO 1: Reutilizacion de la Base de Datos SQLite

def _conexion():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def inicializar_db():
    con = _conexion()
    try:
        con.execute(
            """CREATE TABLE IF NOT EXISTS autores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   nacionalidad TEXT NOT NULL
               )"""
        )
        con.execute(
            """CREATE TABLE IF NOT EXISTS libros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   anio INTEGER NOT NULL,
                   autor_id INTEGER NOT NULL,
                   FOREIGN KEY (autor_id) REFERENCES autores (id)
               )"""
        )
        con.commit()
    finally:
        con.close()

def obtener_autores_db():
    con = _conexion()
    try:
        filas = con.execute(
            "SELECT id, nombre, nacionalidad FROM autores ORDER BY id"
        ).fetchall()
        return [dict(fila) for fila in filas]
    finally:
        con.close()

def obtener_autor_db(autor_id):
    con = _conexion()
    try:
        fila = con.execute(
            "SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (autor_id,)
        ).fetchone()
        return dict(fila) if fila else None
    finally:
        con.close()

def insertar_autor_db(nombre, nacionalidad):
    con = _conexion()
    try:
        cursor = con.execute(
            "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
            (nombre, nacionalidad),
        )
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()

def obtener_libros_db():
    con = _conexion()
    try:
        filas = con.execute(
            """SELECT l.id, l.titulo, l.anio, l.autor_id,
                      a.nombre AS autor_nombre, a.nacionalidad AS autor_nacionalidad
               FROM libros l
               INNER JOIN autores a ON a.id = l.autor_id
               ORDER BY l.id"""
        ).fetchall()
        return [dict(fila) for fila in filas]
    finally:
        con.close()

def obtener_libro_db(libro_id):
    con = _conexion()
    try:
        fila = con.execute(
            """SELECT l.id, l.titulo, l.anio, l.autor_id,
                      a.nombre AS autor_nombre, a.nacionalidad AS autor_nacionalidad
               FROM libros l
               INNER JOIN autores a ON a.id = l.autor_id
               WHERE l.id = ?""",
            (libro_id,),
        ).fetchone()
        return dict(fila) if fila else None
    finally:
        con.close()

def insertar_libro_db(titulo, anio, autor_id):
    con = _conexion()
    try:
        cursor = con.execute(
            "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
            (titulo, anio, autor_id),
        )
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()

def actualizar_libro_db(libro_id, titulo, anio, autor_id):
    con = _conexion()
    try:
        cursor = con.execute(
            "UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?",
            (titulo, anio, autor_id, libro_id),
        )
        con.commit()
        return cursor.rowcount
    finally:
        con.close()

def eliminar_libro_db(libro_id):
    con = _conexion()
    try:
        cursor = con.execute("DELETE FROM libros WHERE id = ?", (libro_id,))
        con.commit()
        return cursor.rowcount
    finally:
        con.close()

#EJERCICIO 2: Definicion e Implementacion de Endpoints HTTP

@app.route("/api/autores", methods=["GET"])
def listar_autores():
    return jsonify(obtener_autores_db()), 200

@app.route("/api/autores", methods=["POST"])
def crear_autor():
    datos = request.get_json(silent=True) or {}
    fallo = validar_campos(datos, "nombre", "nacionalidad")
    if fallo:
        return fallo
    autor_id = insertar_autor_db(datos["nombre"], datos["nacionalidad"])
    return jsonify(obtener_autor_db(autor_id)), 201

@app.route("/api/autores/<int:autor_id>", methods=["GET"])
def obtener_un_autor(autor_id):
    autor = obtener_autor_db(autor_id)
    if autor is None:
        return error_json(404, f"El autor con id {autor_id} no existe")
    return jsonify(autor), 200

@app.route("/api/libros", methods=["GET"])
def listar_libros():
    return jsonify(obtener_libros_db()), 200

@app.route("/api/libros/<int:libro_id>", methods=["GET"])
def obtener_un_libro(libro_id):
    libro = obtener_libro_db(libro_id)
    if libro is None:
        return error_json(404, f"El libro con id {libro_id} no existe")
    return jsonify(libro), 200

@app.route("/api/libros", methods=["POST"])
def crear_libro():
    datos = request.get_json(silent=True) or {}
    fallo = validar_campos(datos, "titulo", "anio", "autor_id")
    if fallo:
        return fallo
    anio = convertir_entero(datos["anio"])
    autor_id = convertir_entero(datos["autor_id"])
    if anio is None:
        return error_json(400, "El campo 'anio' debe ser un numero entero")
    if autor_id is None:
        return error_json(400, "El campo 'autor_id' debe ser un numero entero")
    if obtener_autor_db(autor_id) is None:
        return error_json(404, f"El autor con id {autor_id} no existe")
    nuevo_id = insertar_libro_db(datos["titulo"], anio, autor_id)
    return jsonify(obtener_libro_db(nuevo_id)), 201

@app.route("/api/libros/<int:libro_id>", methods=["PUT"])
def actualizar_un_libro(libro_id):
    libro = obtener_libro_db(libro_id)
    if libro is None:
        return error_json(404, f"El libro con id {libro_id} no existe")
    datos = request.get_json(silent=True) or {}
    campos = [campo for campo in ("titulo", "anio", "autor_id") if campo in datos]
    if not campos:
        return error_json(400, "Debe enviar al menos uno de los campos: titulo, anio, autor_id")
    titulo = datos.get("titulo", libro["titulo"])
    anio = convertir_entero(datos["anio"]) if "anio" in datos else libro["anio"]
    autor_id = convertir_entero(datos["autor_id"]) if "autor_id" in datos else libro["autor_id"]
    if not isinstance(titulo, str) or not titulo.strip():
        return error_json(400, "El campo 'titulo' debe ser un texto no vacio")
    if anio is None:
        return error_json(400, "El campo 'anio' debe ser un numero entero")
    if autor_id is None:
        return error_json(400, "El campo 'autor_id' debe ser un numero entero")
    if obtener_autor_db(autor_id) is None:
        return error_json(404, f"El autor con id {autor_id} no existe")
    actualizar_libro_db(libro_id, titulo, anio, autor_id)
    return jsonify(obtener_libro_db(libro_id)), 200

@app.route("/api/libros/<int:libro_id>", methods=["DELETE"])
def eliminar_un_libro(libro_id):
    libro = obtener_libro_db(libro_id)
    if libro is None:
        return error_json(404, f"El libro con id {libro_id} no existe")
    eliminar_libro_db(libro_id)
    return jsonify({"mensaje": f"Libro con id {libro_id} eliminado", "libro": libro}), 200


#EJERCICIO 3: Manejo de Errores y Validaciones

def error_json(codigo, mensaje):
    return jsonify({"error": mensaje}), codigo

def validar_campos(datos, *obligatorios):
    faltantes = [
        campo
        for campo in obligatorios
        if campo not in datos or datos[campo] is None or datos[campo] == ""
    ]
    if faltantes:
        return error_json(400, "Faltan campos obligatorios: " + ", ".join(faltantes))
    return None

def convertir_entero(valor):
    if isinstance(valor, bool):
        return None
    try:
        return int(valor)
    except (TypeError, ValueError):
        return None

@app.errorhandler(404)
def recurso_no_encontrado(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(405)
def metodo_no_permitido(error):
    return jsonify({"error": "Metodo no permitido"}), 405


#EJERCICIO 4: Script de Prueba

def ejecutar_pruebas():
    print("== Inicio de pruebas ==")

    respuesta = requests.get(f"{URL_BASE}/api/libros")
    assert respuesta.status_code == 200, respuesta.text
    print("1) GET /api/libros ->", respuesta.status_code, respuesta.json())

    respuesta = requests.post(
        f"{URL_BASE}/api/autores",
        json={"nombre": "Gabriel Garcia Marquez", "nacionalidad": "Colombiana"},
    )
    assert respuesta.status_code == 201, respuesta.text
    autor = respuesta.json()
    print("2) POST /api/autores ->", respuesta.status_code, autor)

    respuesta = requests.post(
        f"{URL_BASE}/api/libros",
        json={"titulo": "Cien anos de soledad", "anio": 1967, "autor_id": autor["id"]},
    )
    assert respuesta.status_code == 201, respuesta.text
    libro = respuesta.json()
    print("   POST /api/libros ->", respuesta.status_code, libro)

    respuesta = requests.put(
        f"{URL_BASE}/api/libros/{libro['id']}",
        json={"titulo": "El amor en los tiempos del colera"},
    )
    assert respuesta.status_code == 200, respuesta.text
    assert respuesta.json()["titulo"] == "El amor en los tiempos del colera"
    print("3) PUT /api/libros/<id> ->", respuesta.status_code, respuesta.json())

    respuesta = requests.delete(f"{URL_BASE}/api/libros/{libro['id']}")
    assert respuesta.status_code == 200, respuesta.text
    assert "eliminado" in respuesta.json()["mensaje"].lower()
    print("4) DELETE /api/libros/<id> ->", respuesta.status_code, respuesta.json())

    respuesta = requests.get(f"{URL_BASE}/api/libros/{libro['id']}")
    assert respuesta.status_code == 404, respuesta.text
    print("   GET del libro eliminado ->", respuesta.status_code, respuesta.json())

    respuesta = requests.post(f"{URL_BASE}/api/libros", json={"titulo": "Sin anio"})
    assert respuesta.status_code == 400, respuesta.text
    print("   POST /api/libros sin campos obligatorios ->", respuesta.status_code, respuesta.json())

    respuesta = requests.get(f"{URL_BASE}/api/libros/999999")
    assert respuesta.status_code == 404, respuesta.text
    print("   GET /api/libros/999999 ->", respuesta.status_code, respuesta.json())

    print("== Todas las pruebas finalizaron correctamente ==")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        ejecutar_pruebas()
    else:
        inicializar_db()
        app.run(host="127.0.0.1", port=5000, debug=False)
