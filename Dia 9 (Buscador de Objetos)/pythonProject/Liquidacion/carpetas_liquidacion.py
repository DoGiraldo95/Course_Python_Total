"""
Creacion de carpetas de liquidacion diaria
"""

import datetime
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Carpetas:
    """Clase contenedora de las funciones de creacion de carpetas de liquidacion"""
    RUTA = os.getenv("RUTA_DES")
    FECHA = datetime.now()
    CARPETAS = ['Detalle', 'Valor a Consignar']

    @classmethod
    def carpeta_mes(cls):
        mes = cls.FECHA.strftime("%B")
        carpeta  = os.path.join(cls.RUTA, mes)

        if mes not in os.listdir(cls.RUTA):
            os.mkdir(carpeta)

        return carpeta
            


    @classmethod
    def carpeta_dia(cls):
        """La funcion crea carpeta principal de acuerdo al día de ejecución"""
        carpeta = Path(cls.carpeta_mes(), str(cls.FECHA.day))
        carpeta.mkdir()
        return carpeta

    @classmethod
    def carpetas(cls, carpeta):
        os.chdir(carpeta)
        if os.path.isdir(carpeta):
            for x in cls.CARPETAS:
                Path(carpeta, x).mkdir()


