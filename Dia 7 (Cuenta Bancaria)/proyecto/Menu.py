from Datos import Datos
from os import system


def inicio():
    cliente = Datos.solicitar_datos_cliente()
    opcion = None

    while opcion != '0':
        opcion = input(f'''Sr/a {cliente.nombre} {cliente.apellido} ingrese la opcion deseada: 
[1] Depositar
[2] Retirar
[0] Salir
''')
        system('Close')
        match opcion:
            case '1':
                print('depositar a la cuenta'.upper().center(50, '*'))
                numero = input('ingrese un valor: ')

                cliente.depositar(Datos.validar_numero(numero))

                print(cliente)

            case '2':
                print('retirar a la cuenta'.upper().center(50, '*'))
                numero = input('ingrese un valor: ')

                cliente.retirar(Datos.validar_numero(numero))

                print(cliente)

            case '0':
                print('Adios')

            case _:
                print('ingrese una opccion correcta')

        system('Close')


if __name__ == '__main__':
    inicio()
