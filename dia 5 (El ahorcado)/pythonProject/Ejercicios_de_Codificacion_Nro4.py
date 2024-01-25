from random import shuffle

# def chequear_3_cifras(lista):
#     for n in lista:
#         if n in range(100, 1000):
#             return True
#         else:
#             pass
#     return False
#
#
# lista_nume = [12, 23, 23]
#
# print(chequear_3_cifras(lista_nume))

# Práctica Funciones Dinámicas 1
#
# Crea una función (todos_positivos) que reciba una lista de números como parámetro,
# y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es
# negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.
#
# No invoques la función, solo es necesario definirla.

lista_numeros = list(range(-7, 10))

shuffle(lista_numeros)

print(lista_numeros)


def todos_positivos(lista):
    for n in lista:
        if n > 0:
            pass

        else:
            return False

    return True


print(todos_positivos(lista_numeros))

# Práctica Funciones Dinámicas 2
#
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la
# variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

# lista_numeros = [1, 4, 5, -1, 10001, 20]
#
#
#
# def suma_menores(lista):
#     suma = 0
#
#     for numero in lista:
#         if 0 < numero < 1000:
#             suma += numero
#     return suma
#
#
# print(suma_menores(lista_numeros))
#
# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros),
# y devuelva el resultado de dicha cuenta.

lista_numeros = [1, 4, 5, -1, 10001, 20]


def cantidad_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1

    return contador


print(cantidad_pares(lista_numeros))
