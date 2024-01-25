import os
from pathlib import  Path

ruta_actual = os.getcwd()
#ruta_home = Path.home()

ruta_origen = Path(ruta_actual).parent.parent.parent
nueva_ruta = Path(ruta_origen, 'Prueba_Path')

Path.mkdir(nueva_ruta)


print(nueva_ruta)