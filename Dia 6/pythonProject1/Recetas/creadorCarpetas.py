import os

from pathlib import Path


def rutas(ruta):
    ruta_nueva = Path(os.getcwd(), ruta)
    if not ruta_nueva.exists():
        Path.mkdir(ruta_nueva)
        os.chdir(ruta_nueva)
        print(f''' Ruta creada con exito, la nueva ruta es: 
{os.getcwd()}
''')
    else:
        print('La ruta existe')


ruta = Path(os.getcwd(), 'Recetas', 'Postres')

rutas(ruta)