import os
import shutil
from collections import namedtuple
from datetime import date
import openpyxl

from carpetas_liquidacion import Carpetas
from formatos.formatos import FormatosLiquidacion


def decora_archivo(funcion):
    def crear_archivo(*args):
        forma = funcion(*args)
        archivo = None
        formato = forma[0]
        nombre = forma[1]
        if not os.path.exists(forma[1]):
            archivo = openpyxl.Workbook()
            archivo.save(nombre)
        shutil.copy(formato, nombre)

    return crear_archivo


class Archivos:

    @staticmethod
    def nombre_archivo():
        fecha = date.today()
        fecha_fin = '{}-{}-{}'.format(fecha.day - 1, fecha.month, fecha.year)

        Detalle = namedtuple('Detalle',
                             ['Consolidada', 'Reporte', 'Detallado', 'Liquidacion_Consolidada', 'Valor_Trasladar'])

        match fecha.strftime("%w"):
            case 1:
                fecha_init = '{}-{}-{}'.format(fecha.day - 2, fecha.month, fecha.year)

                consolidada = f'Liquidacion Consolidada Detallado {fecha}.xlsx'
                reporte = f'Reporte Liquidación {fecha} (TRX. {fecha_init} a {fecha_fin}).xlsx'
                detallado = f'Reporte Liquidación Detallado  {fecha} (TRX. {fecha_init} a {fecha_fin}).xlsx'
            case _:
                consolidada = f'Liquidacion Consolidada Detallado {fecha}.xlsx'
                reporte = f'Reporte Liquidación {fecha} (TRX. {fecha_fin}).xlsx'
                detallado = f'Reporte Liquidación Detallado  {fecha} (TRX. {fecha_fin}).xlsx'
        nom_archivo = Detalle(consolidada, reporte, detallado, f'Liquidacion Consolidada {date.today()}.xlsx',
                              'Monto Total Ventas y Recargas XXXX.xlsx')

        return nom_archivo

    @classmethod
    @decora_archivo
    def archivo_liquidacion(cls, ruta):
        os.chdir(ruta)
        nom_archivo = cls.nombre_archivo().Liquidacion_Consolidada
        return FormatosLiquidacion.formatos().Liquidacion, nom_archivo

    @staticmethod
    def archivos_detalle(ruta):
        os.chdir(os.path.join(ruta, Carpetas.CARPETAS[0]))
        nombre_archivo = Archivos.nombre_archivo()
        formatos = FormatosLiquidacion.formatos()

        for i in range(0, 3):
            archivo = openpyxl.Workbook()
            archivo.save(nombre_archivo[i])
            shutil.copy(formatos[i], nombre_archivo[i])

    @classmethod
    @decora_archivo
    def valor_a_trasladar(cls, ruta):
        os.chdir(os.path.join(ruta, Carpetas.CARPETAS[1]))
        nombre_archivo = cls.nombre_archivo().Valor_Trasladar
        return FormatosLiquidacion.formatos().ValorTrasladar, nombre_archivo


if __name__ == '__main__':
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
