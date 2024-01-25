import os
from pathlib import Path

ruta_actual = os.getcwd()

recetas = Path(ruta_actual, 'Recetas')
ruta_actual = os.chdir(recetas)

os.chdir(recetas)


print(os.getcwd())


