import os
import re
import shutil
import time
from pathlib import Path


class OrganizaDescargas:
    RUTA = r'/home/diego/Descargas'

    @staticmethod
    def categoria(archivo):
        carpetas = ['PDF', 'XLSX', 'JPEG']
        extension = re.search(r'(pdf$|xlsx$|jpeg$)', archivo)
        if extension is not None:
            try:
                extension = extension.group().upper()
                carpetas.index(extension)
            except AttributeError as ae:
                print(f'Ocurrio un error --> {ae}')
            except ValueError as ve:
                print(f'Ocurrio un error --> {ve}')
            else:
                shutil.move(archivo, Path(r'/home/diego/Descargas/', extension))
        else:
            shutil.move(archivo, r'/home/diego/Descargas/OTROS')

        # shutil.move(archivo, r'/home/diego/Descargas/PDF')
        # elif re.search('.xlsx$', archivo) is not None:
        #     shutil.move(archivo, r'/home/diego/Descargas/EXCEL')
        # elif re.search('.jpeg$', archivo) is not None:
        #     shutil.move(archivo, r'/home/diego/Descargas/JPEG')
        # else:
        #

    @classmethod
    def organiza(cls):
        os.chdir(Path(cls.RUTA))

        for archivos in os.listdir(cls.RUTA):
            if os.path.isfile(archivos):
                cls.categoria(archivos)

        print('archivos orgnizados'.title())
        print(f'Finalizo {time.time()}')


OrganizaDescargas.organiza()
