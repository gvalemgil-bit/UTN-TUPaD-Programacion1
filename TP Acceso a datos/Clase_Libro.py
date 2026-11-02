class Libro:
    def __init__(self, id_libro: 0, titulo: str, anio_publicacion: int, autor: int):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio = anio_publicacion
        self.autor = autor
    def __str__(self):
        return f"Libro[ID: {self.id_libro}, Título: '{self.titulo}', Año: {self.anio_publicacion}, Autor: {self.autor.nombre}]"