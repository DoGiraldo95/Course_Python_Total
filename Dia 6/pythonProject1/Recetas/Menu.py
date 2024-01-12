import os
from os import system
from pathlib import Path

from Recetario import Recetario


class Menu:

    @classmethod
    def menu_recetario(cls):
        opcion = 0
        while opcion != 6:
            ruta = Path('/home/diego/Documentos/git/Course_Python_Total/Dia 6/pythonProject1/Recetas')
            os.chdir(ruta)
            titulo = f'Menu receterio'.center(50, '*')
            print(f'''{titulo} 
            1) leer receta 
            2) crear receta 
            3) crear categoria
            4) eliminar receta
            5) eliminar categoria
            6) salir
            '''.title())
            opcion = int(input('ingrese la opcion deseada : '))
            system('clear')
            match opcion:

                case 1:
                    Recetario.leer_receta()
                case 2:
                    Recetario.crear_receta()
                case 3:
                    Recetario.crear_categoria()
                case 4:
                    Recetario.eliminar_receta()
                case 5:
                    Recetario.eliminar_categoria()
                case 6:
                    print('Adios')
                case _:
                    print('Opcion Incorrecta')


if __name__ == '__main__':
    Menu.menu_recetario()
