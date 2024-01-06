import os
from pathlib import Path, PureWindowsPath  # obtener rutas de windows

os.chdir(Path(os.getcwd()) / 'archivos_prueba')

# os.remove('prueba_path.py')

ruta_actual = os.getcwd()

archivo_texto = Path(ruta_actual) / 'texto5.txt'

nombre_archivo = archivo_texto.stem

if nombre_archivo == 'texto5':
    print(Path.read_text(archivo_texto))
    print(PureWindowsPath(archivo_texto))
else:
    print('archivo incorrecto ')