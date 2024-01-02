# """ Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista. """

# mi_lista = list(range(2500, 2586))

# print(mi_lista)


# print("""
# %s

# Utilizando la función range(), crea en una
# única linea de código una lista formada por
# todos los números múltiplos de 3 desde el 3 al 300 (inclusive).
# Almacena dicha lista en la variable mi_lista.

# """ % ('Práctica Rango 2'.upper()))

# mi_lista = list(range(3, 301, 3))

# print(mi_lista)

print(""" 

%s

Utiliza la función range() y un loop para sumar los cuadrados 
de todos los números del 1 al 15 (inclusive). 
Almacena el resultado en una variable llamada suma_cuadrados. 

""" % ('Práctica Rango 3'.upper()))

suma_cuadrados = 0

for numero in range(1, 16):

    potencia = numero ** 2
    suma_cuadrados += potencia

print(f'Resultado := {suma_cuadrados}')
