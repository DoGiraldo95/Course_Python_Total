import os

from Cliente import Cliente


class Datos:

    @staticmethod
    def validar_numero(numero):
        if not numero.isnumeric():
            numero = 0
            return numero
        else:
            return int(numero)

    @staticmethod
    def solicitar_datos_cliente():
        print('datos del cliente'.upper().center(50, '*'))

        nombre_cliente = input('Ingrese nombre del cliente : ')
        apellido_cliente = input('Ingrese apellido del cliente : ')
        cuenta = input('Ingrese numero de cuenta : ')
        balance = input('Ingrese el saldo actual de la cuenta : ')

        cliente = Cliente(nombre_cliente, apellido_cliente, Datos.validar_numero(cuenta), Datos.validar_numero(balance))
        os.system('Close')
        return cliente
