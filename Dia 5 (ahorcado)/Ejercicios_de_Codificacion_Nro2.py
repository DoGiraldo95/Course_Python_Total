# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"
#
# Solo debes definir la función, no debes invocarla luego.

def saludar():
    print("¡Hola mundo!")


saludar()

# Práctica Crear Funciones 2
# Declara una función llamada bienvenida, que tome como argumento el nombre de una
# persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
#
# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
#
# Solo debes definir la función y crear la variable, no debes invocar la función luego.

nombre_persona = 'carlos'


def bienvenida(nombre):
    print(f"¡Bienvenido {nombre}!")


bienvenida(nombre_persona)

# Práctica Crear Funciones 3
# Declara una función llamada cuadrado, que tome como argumento un número cualquiera,
# y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
#
# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número
# cualquiera.
#
# Solo debes definir la función y crear la variable, no debes invocar la función luego.

un_numero = 3


def cuadrado(numero):
    print(numero ** 2)


cuadrado(un_numero)
