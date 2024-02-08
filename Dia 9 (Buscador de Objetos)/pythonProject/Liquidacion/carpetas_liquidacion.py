"""
Creacion de carpetas de liquidacion diaria
"""

import datetime
import os
from pathlib import Path


class Carpetas:
    """Clase contenedora de las funciones de creacion de carpetas de liquidacion"""
    RUTA = Path(r'C:\Users\dgiraldo\Documents\UTRYT\Liquidaciones Diego\2024\02_Febrero')
    FECHA = datetime.date.today()
    CARPETAS = ['Detalle', 'Valor a Consignar']

    @classmethod
    def carpeta_dia(cls):
        """La funcion crea carpeta principal de acuerdo al día de ejecución"""
        carpeta = Path(cls.RUTA, str(cls.FECHA.day+1))
        carpeta.mkdir()
        return carpeta

    @classmethod
    def carpetas(cls, carpeta):
        os.chdir(carpeta)
        if os.path.isdir(carpeta):
            for x in cls.CARPETAS:
                Path(carpeta, x).mkdir()
