# Práctica Métodos Especiales 1
#
# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{
# titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).

class Libro:

    def __init__(self, titulo, autor, cantidad_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__cantidad_paginas = cantidad_paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor
    @property
    def cantidad_paginas(self):
        return self.__cantidad_paginas
    def __str__(self):
        mensaje = f'"{self.titulo}", de {self.autor}'
        return mensaje

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        print("Libro eliminado")


libro = Libro('Cien anios de soledad'.capitalize(), 'gabriel garcia marquez'.capitalize(), 24)

print(libro)
print(len(libro))
del libro
