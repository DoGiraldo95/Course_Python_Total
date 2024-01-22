from Persona import Persona


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

    def depositar(self, numero):
        self.balance += numero

    def retirar(self, numero):
        if self.balance >= numero:
            self.balance -= numero
        else:
            print('Saldo Insuficiente')


if __name__ == '__main__':
    cliente1 = Cliente('diego', 'giraldo', '25668', '25000')
