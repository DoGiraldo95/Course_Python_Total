import os


def abrir_leer(archivo):
    try:
        archivo = open(archivo)
        return archivo.read()

    except Exception as err:
        print(err)


print(abrir_leer('Ejercicios_Paths.py'))


# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como
# parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo):
    try:
        file = open(archivo, 'w')
        file.write('contenido eliminado')
    except Exception as err:
        print(err)


# sobrescribir('archivo.txt')


# Práctica Archivos y Funciones 3
#
# Crea una función llamada registro_error() que abra (open) un archivo indicado como
# parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
# Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    try:
        file = open(archivo, 'a')
        file.write('se ha registrado un error de ejecución')
    except Exception as err:
        print(err)


registro_error('archivo.txt')
