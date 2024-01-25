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
                numero = Datos.validar_numero()
                cliente.depositar(numero)

            case '2':

                numero = Datos.validar_numero()
                cliente.retirar(numero)

            case '0':
                print('Adios')

            case _:
                print('ingrese una opccion correcta')

        system('Close')


if __name__ == '__main__':
    inicio()
