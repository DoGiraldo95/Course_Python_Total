from pathlib import Path
import os
import shutil

# from collections import deque, namedtuple

direccion = Path(r'C:\Users\dgiraldo\Downloads')
os.chdir(direccion)


def organiza(file):
    if 'pdf' in file:
        shutil.move(file, Path(direccion, 'PDF'))
    elif 'xlsx' in file:
        shutil.move(file, Path(direccion, 'EXCEL'))
    elif 'jpeg' in file:
        shutil.move(file, Path(direccion, 'EXCEL'))
    else:
        shutil.move(file, Path(direccion, 'OTROS'))


def archivo():
    archivos = os.listdir()
    try:
        for i in archivos:
            if os.path.isfile(i):
                organiza(i)
    except:
        print('Ocurrio un error')
    else:
        print('Archivos organizados con exito')


#
# def organizar_pdf():
#     archivo = os.listdir()
#     try:
#         for i in direccion.glob('**/*.pdf'):
#             archivo.append(i.name)
#
#         tupla = namedtuple('archivo', 'PDF')
#         pdf = tupla(archivo)
#
#         for j in pdf.PDF:
#             shutil.move(j, Path(direccion, 'PDF'))
#     except Exception:
#         print('Los archivo ya existe en el carpeta')
#     else:
#         print('archivos ordenados')
#
#
# def organizar_excel():
#     archivo = []
#     try:
#         for i in direccion.glob('**/*.xlsx'):
#             archivo.append(i.name)
#
#         tupla = namedtuple('archivo', 'EXCEL')
#         excel = tupla(archivo)
#
#         for j in excel.EXCEL:
#             shutil.move(j, Path(direccion, 'EXCEL'))
#     except Exception:
#         print('Los archivo ya existe en el carpeta')
#     else:
#         print('archivos ordenados')
#
#
# organizar_excel()

archivo()
