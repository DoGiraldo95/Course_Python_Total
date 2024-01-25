"""
Procedimiento suma de dos numeros
"""


def decora_operaciones(name):
    def fun_operacion(funcion):
        def operacion(*args):
            print('[operacion {}]'.format(name).upper().center(50, '-'))
            print(f'El resultado de su operacion es := {funcion(*args)}')

        return operacion

    return fun_operacion


class Operaciones:

    @decora_operaciones('suma')
    def sumar(self, numero1, numero2):
        """funcion retorna el valor de la suma de los dos numeros"""
        return numero1 + numero2


suma = Operaciones.sumar

suma(None, 1, 6)
