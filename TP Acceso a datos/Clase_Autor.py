class Autor:
    def __init__(self,id_autor: int, nombre: str, nacionalidad: str):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def __str__(self):
        return f"Autor[ID: {self.id_autor}, Nombre: {self.nombre}, Nacionalidad: {self.nacionalidad}]"