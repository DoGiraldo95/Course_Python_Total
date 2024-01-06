import os
from pathlib import Path

"""Obtener ruta actual"""
ruta_actual = os.getcwd()

# ruta = os.mkdir(Path(ruta_actual)/ 'archivos_prueba')
ruta_nueva = os.chdir(Path(ruta_actual) / 'archivos_prueba')

with open('texto5.txt', 'w') as archivo:
    archivo.write('nuevo archivo de texto'.capitalize())
    print('archivo creado con exito')

