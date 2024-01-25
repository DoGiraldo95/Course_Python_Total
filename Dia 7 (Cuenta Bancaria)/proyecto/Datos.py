import os

from Cliente import Cliente


class Datos:

    @staticmethod
    def validar_numero():
        while True:
            try:
                numero = int(input('ingrese un numero: '.capitalize()))
            except ValueError:
                print('ingrese un valor numerico')
            else:
                return numero

    @staticmethod
    def solicitar_datos_cliente():
        print('datos del cliente'.upper().center(50, '*'))

        nombre_cliente = input('Ingrese nombre del cliente : ')
        apellido_cliente = input('Ingrese apellido del cliente : ')
        cuenta = input('Ingrese numero de cuenta : ')

        cliente = Cliente(nombre_cliente, apellido_cliente, cuenta)
        os.system('Close')
        return cliente


if __name__ == '__main__':
    numero = Datos.validar_numero()
    print(numero)
