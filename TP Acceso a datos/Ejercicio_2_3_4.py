import sqlite3
#Ejercicio 2
def inicializar_db():
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    #Tabla autores
    cursor.execute('''CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL)''')
    #Tabla libros
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    anio INTERGER,
                    autor_id INTEGER,
                    FOREIGN KEY (autor_id) REFERENCES autores (id)
                    )
                    ''')
    conexion.commit()
    conexion.close()
    print("Base de datos biblioteca.db creada con exito.")

#Ejercicio 3
def registrar_autor(nombre, nacionalidad):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)', (nombre, nacionalidad))
    autor_id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return autor_id

def registrar_libro(titulo, anio, autor_id):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)', (titulo, anio, autor_id))
    conexion.commit()
    conexion.close()

def listar_libros():
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT libros.id, libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    ''')
    resultados = cursor.fetchall()
    conexion.close()

    print("\n--- Catálogo de Libros ---")
    if not resultados:
        print("No hay libros registrados.")
    for fila in resultados:
        print(f"ID: {fila[0]} | Título: '{fila[1]}' | Año: {fila[2]} | Autor: {fila[3]}")
    print("--------------------------\n")

def actualizar_titulo_libro(id_libro, nuevo_titulo):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('UPDATE libros SET titulo = ? WHERE id = ?', (nuevo_titulo, id_libro))
    conexion.commit()
    conexion.close()

def eliminar_libro(id_libro):
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM libros WHERE id = ?', (id_libro,))
    conexion.commit()
    conexion.close()

#Ejercicio 4
if __name__ == '__main__':
    inicializar_db()
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
        print("1. Registrar nuevo autor")
        print("2. Registrar nuevo libro")
        print("3. Listar todos los libros")
        print("4. Actualizar título de un libro")
        print("5. Eliminar un libro")
        print("6. Salir")    
        opcion = input("Seleccione una opción (1-6): ")   
        if opcion == '1':
            nombre = input("Ingrese el nombre del autor: ")
            nacionalidad = input("Ingrese la nacionalidad del autor: ")
            id_gen = registrar_autor(nombre, nacionalidad)
            print(f"✅ Autor registrado exitosamente con el ID: {id_gen}") 
        elif opcion == '2':
            titulo = input("Ingrese el título del libro: ")
            try:
                anio = int(input("Ingrese el año de publicación: "))
                autor_id = int(input("Ingrese el ID del autor correspondiente: "))
                registrar_libro(titulo, anio, autor_id)
                print("✅ Libro registrado exitosamente.")
            except ValueError:
                print("❌ Error: El año y el ID del autor deben ser números enteros.")         
        elif opcion == '3':
            listar_libros()
        elif opcion == '4':
            try:
                id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                nuevo_titulo = input("Ingrese el nuevo título: ")
                actualizar_titulo_libro(id_libro, nuevo_titulo)
                print("✅ Título actualizado exitosamente.")
            except ValueError:
                print("❌ Error: El ID del libro debe ser un número entero.") 
        elif opcion == '5':
            try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                eliminar_libro(id_libro)
                print("✅ Libro eliminado exitosamente.")
            except ValueError:
                print("❌ Error: El ID del libro debe ser un número entero.")     
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")