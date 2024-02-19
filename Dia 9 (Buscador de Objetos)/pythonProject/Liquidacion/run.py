import os

from archivos_liquidacion import Archivos
from carpetas_liquidacion import Carpetas


def mostrar_contenido():
    ruta = os.path.join(Carpetas.RUTA, str(Carpetas.FECHA.day))

    for home, dirs, files in os.walk(ruta):
        print(f'Carpeta {home}')
        for x in dirs:
            print(f'\t{x}')
        print('Archivos:')
        for j in files:
            print(f'\t{j}')
        print('\n')


def ejercutable():
    try:
        carpeta = Carpetas.carpeta_dia()
        Carpetas.carpetas(carpeta)
        Archivos.archivos_detalle(carpeta)
        Archivos.archivo_liquidacion(carpeta)
        Archivos.valor_a_trasladar(carpeta)
    except FileExistsError as exError:
        print('La carpeta o archivo ya existe --> {}'.format(exError))
    except FileNotFoundError as noFoError:
        print('Error en la ruta indicada {}'.format(noFoError))
    else:
        print('Carpeta liquidacion creada')
        mostrar_contenido()


ejercutable()
