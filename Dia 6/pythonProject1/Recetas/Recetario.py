from os import system
import os
from pathlib import Path


class Recetario:
    @classmethod
    def control_rutas(cls, categoria):
        ruta = Path(os.getcwd(), categoria.capitalize())
        if ruta.exists():
            os.chdir(ruta)
            return ruta
        else:
            print('la categoria ingresada no existe')

    @classmethod
    def mostrar_seleccionar_categoria(cls):
        ruta_actual = Path(os.getcwd())

        print('Categorias'.center(50, '*'))
        for i in ruta_actual.iterdir():
            if i.is_dir():
                print(os.path.basename(i))

        categoria = input('ingrese el nombre de la categoria: ').lower()
        return categoria

    @classmethod
    def leer_receta(cls):
        print('leer recetas'.center(50, '*').upper())
        recetas = []
        contador = 0

        categoria = cls.mostrar_seleccionar_categoria()
        system('clear')
        try:
            ruta = cls.control_rutas(categoria)
            if ruta:
                print('recetas: '.capitalize())
                for txt in ruta.glob('*.txt'):
                    print(f'''{contador}) {txt.stem}''')
                    recetas.append(txt)
                    contador += 1

                receta = int(input('Ingrese el numero de la receta a mostrar : '))
                system('clear')
                mostrar_reseta = open(recetas[receta])
                print(f'''Contenido receta: 
        {mostrar_reseta.read()}''')
                mostrar_reseta.close()
        except Exception as err:
            print(err)

    @classmethod
    def crear_receta(cls):
        print('crear receta'.center(50, '*').upper())
        categoria = cls.mostrar_seleccionar_categoria()
        receta = input('ingrese el nombre de la receta: '.title())

        try:
            ruta = cls.control_rutas(categoria)
            print('Ingrese el contenido de la receta:'.center(50, '*'))
            contenido = input('contenido : ')
            system('clear')
            if ruta:
                receta = f'{receta.title()}.txt'

                nueva_receta = open(receta, 'x')
                nueva_receta.write(contenido)
                print(f'Receta {Path(receta).stem} creada con exito')
                nueva_receta.close()

        except Exception as err:
            print(f''' Error: = {err}
receta {receta} existe''')

    @classmethod
    def crear_categoria(cls):
        print('leer categoria'.center(50, '*').upper())
        categoria = Path(os.getcwd(), cls.mostrar_seleccionar_categoria().capitalize())
        system('clear')
        try:
            if not categoria.exists():
                Path.mkdir(categoria)
                print(f'Categoria "{os.path.basename(categoria)}" creado con exito'.capitalize())
            else:
                print(f'Categoria {os.path.basename(categoria)} existe'.capitalize())
        except Exception as err:
            print(err)

    @classmethod
    def eliminar_receta(cls):
        print('eliminar recetas'.center(50, '*').upper())
        ruta = Path(os.getcwd())
        recetas = []
        contador = 0
        try:
            for receta in ruta.glob('**/*txt'):
                print(f'{contador}) {receta.stem}')
                recetas.append(receta)
                contador += 1
            receta_usuario = int(input('ingrese la receta a eliminar '))

            if recetas[receta_usuario].exists():
                os.remove(recetas[receta_usuario])
                print(f'Receta {recetas[receta_usuario].stem} eliminada ')
            else:
                print(f'Receta incorrecta')

        except Exception as err:
            print(err)

    @classmethod
    def eliminar_categoria(cls):
        print('eliminar categoria'.center(50, '*').upper())
        categoria = cls.mostrar_seleccionar_categoria()
        system('clear')
        ruta = Path(os.getcwd(), categoria.capitalize())

        try:
            if ruta.exists():
                os.rmdir(ruta)
                print(f'categoria eliminada')

            else:
                print('categoria no exite')
        except Exception as err:
            print(err)


if __name__ == '__main__':
    # categoria = input('ingrese la categoria de la receta: ').lower()
    # receta = input('

    Recetario.eliminar_categoria()
