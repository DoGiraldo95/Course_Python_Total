"""
Procedimiento suma de dos numeros
"""


def decorador_operacion(funcion):
    def resultado_operacion(numero1, numero2):
        print('Operacion suma'.center(50, '*'))
        resultado = funcion(numero1, numero2)


def sumar(numero1, numero2):
    """funcion retorna el valor de la suma de los dos numeros"""
    return numero1 + numero2


print(sumar(5, 7))
