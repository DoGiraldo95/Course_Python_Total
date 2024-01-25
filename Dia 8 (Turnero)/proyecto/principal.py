from os import system

import numeros


def principal():
    areas = ['P', 'F', 'C']
    print('bienvenido a la farmacia'.center(50, '-').upper())

    while True:
        try:
            print('''Areas disponibles:
[P]-Perfumeria 
[F]-Farmacia 
[C]-Cosmeticos''')

            area = input('Ingrese el area deseada : '.upper())
            areas.index(area)
            system("cls")
        except ValueError:
            print('Area no disponible')
        else:
            break
    numeros.decorador(area)


def run():
    principal()

    try:
        opcion = str(input('Desea pedir mar turnos [S] o [N] : '))
        ['S', 'N'].index(opcion)

    except ValueError:
        print('opccion incorrecta')

    else:
        if not opcion == 'N':
            run()
        else:
            print('Adios')


run()
