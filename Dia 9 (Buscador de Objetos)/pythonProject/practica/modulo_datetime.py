from pathlib import Path
from datetime import date
import os, shutil


class Liquidacion:
    RUTA = os.getcwd()
    FECHA = date.today()

    @classmethod
    def carpeta(cls):
        ruta = Path(cls.RUTA, str(cls.FECHA.day))
        if not os.path.exists(ruta):
            try:
                os.mkdir(ruta)
            except OSError as error:
                print('Ocurrio el siguiente error: {}'.format(error))
        return ruta


# print(Liquidacion.carpeta())

"""Práctica Módulo Datetime 1

Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999"""

mi_fecha = date(1999, 2, 3)

# print(mi_fecha.strftime('%d de %B de %Y')) -- Ejecucion practica 1 'formato fecha'

"""[Práctica Módulo Datetime 2]

Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada."""




