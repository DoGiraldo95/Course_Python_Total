from random import randint


class Adivinar_numero:

    intentos = 0
    numero_secreto = randint(1, 100)
    numeros_ingresados = []

    @classmethod
    def adivinar(cls):
        numero = 0
        nombre = input('Ingrese el nombre del participante : ').capitalize()

        while cls.intentos < 8:

            numero = int(input('Ingrese el numero del participante : '))

            cls.intentos += 1
            cls.numeros_ingresados.append(numero)

            print(f"""
                  
Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo {cls.intentos} intentos
para adivinar cuál crees que es el número
                  
                  """)
            print(f'Numero ingresado es {numero}')

            if numero not in range(1, 101):
                print('ha elegido un número que no está permitido')

            elif numero < cls.numero_secreto:
                print(f'ha elegido un número menor al número secreto := {cls.numero_secreto}')

            elif numero > cls.numero_secreto:
                print(f'ha elegido un número mayor al número secreto := {cls.numero_secreto}')

            else:
                mensaje = 'ha ganado'.upper().center(50, '*')
                print(f'''{mensaje}
Numero de intentos realizados := {cls.intentos}
Numero ingresados := {cls.numeros_ingresados}''')

                break

        if numero != cls.numero_secreto:
            print('has perdido'.upper().center(50, '*'))


if __name__ == '__main__':
    Adivinar_numero.adivinar()
