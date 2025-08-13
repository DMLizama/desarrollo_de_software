from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
    
    def obtener_info(self):
        print(f"{self.titulo}, {self.autor}, {self.anio}, {self.genero}")

    def es_clasico(self):
        return ((datetime.now().year - self.anio > 50))
    

l1 = Libro("100 año de soledad", "garcia marquez", 1974, "novela")
l2 = Libro("viaje al centro de la tierra", "qcyo", 2000, "genero 1")

print(l1.obtener_info())
print(l2.obtener_info())
print(f"Es clasico?"+str(l1.es_clasico()))
print(f"Es clasico?"+str(l2.es_clasico()))

