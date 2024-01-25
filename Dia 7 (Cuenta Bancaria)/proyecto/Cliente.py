from Persona import Persona


def decorador_operaciones(name):
    def fun_operacion(funcion):
        def operacion(*args):
            if name == 'depositar':
                print('depositando a la cuenta del cliente'.title())
            else:
                print('retirando a la cuenta del cliente'.title())

            funcion(*args)
            print(args[0])

        return operacion

    return fun_operacion


class Cliente(Persona):

    def __init__(self, nombre, apellido, cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        mensaje = f'''[Numero de Cuenta] - " {self.cuenta} "
[Numero de Balance] - " ${self.balance} "        
'''
        return mensaje

    @decorador_operaciones('depositar')
    def depositar(self, numero):
        self.balance += numero

    @decorador_operaciones('retirar')
    def retirar(self, numero):
        if self.balance >= numero:
            self.balance -= numero
        else:
            print('Saldo Insuficiente')


if __name__ == '__main__':
    cliente1 = Cliente('diego', 'giraldo', '25668', 25000)
