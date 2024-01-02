from random import *


#
#
# # Práctica sobre Interacción entre Funciones 1
# # Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
# #
# # La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
# #
# # Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
# #
# # Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda
# # función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
# #
# # Si la suma es menor o igual a 6:
# # "La suma de tus dados es {suma_dados}. Lamentable"
# # Si la suma es mayor a 6 y menor a 10:
# # "La suma de tus dados es {suma_dados}. Tienes buenas chances"
# # Si la suma es mayor o igual a 10:
# # "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# # Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
#
# def lanzar_dados():
#     """
#     Genera numeros aleatorios asignados al valor de los dados
#     :return: arreglo
#     """
#     dado1 = randint(1, 6)
#     dado2 = randint(1, 6)
#
#     return dado1, dado2
#
#
# def evaluar_jugada(*args):
#     mensaje = None
#     suma = sum(*args)
#     # Si la suma es menor o igual a 6:
#     if suma <= 6:
#         mensaje = f"La suma de tus dados es {suma}. Lamentable"
#     # Si la suma es mayor a 6 y menor a 10:
#     elif 6 < suma < 10:
#         mensaje = f"La suma de tus dados es {suma}. Tienes buenas chances"
#     # Si la suma es mayor o igual a 10:
#     else:
#         mensaje = f"La suma de tus dados es {suma}. Parece una jugada ganadora"
#     return mensaje
#
#
# print(evaluar_jugada(lanzar_dados()))


# Práctica sobre Interacción entre Funciones 2
#
# Crea una función llamada reducir_lista() que tome una lista como
# argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando
# uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.
#
# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
#
# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función,
# y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
#
# lista_numerous = [1, 2, 15, 7, 2]
#
#
# def reducir_lista(lista):
#     lista_unicos = []
#
#     for numero in lista:
#         if numero not in lista_unicos:
#             lista_unicos.append(numero)
#
#     lista_unicos.remove(max(lista))
#
#     return lista_unicos
#
#
# def promedio(lista):
#     promedio_lista = sum(lista) / len(lista)
#     return promedio_lista
#
#
# lista_numerous = [1, 2, 15, 7, 2, 8]
#
#
# def reducir_lista(lista):
#     lista = list(set(lista))  # los sets eliminan duplicados
#     lista.sort()  # ordena la lista
#     lista.pop(-1)
#     return lista
#
#
# def promedio(lista):
#     valor_medio = sum(lista) / len(lista)
#     return valor_medio


# Práctica sobre Interacción entre Funciones 3
# Crea una función (llamada lanzar_moneda) que devuelva el resultado de
# lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir
# argumentos para funcionar.
#
# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del
# lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con
# valores y llamarla lista_numeros).
#
# Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (
# devolverla como lista vacía []).
#
# Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
#
# Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

def lanzar_moneda():
    moneda = choice(('cara'.capitalize(), 'cruz'.capitalize(),))
    print(moneda)
    return moneda


def probar_suerte(resultado, lista_numeros):
    if resultado == 'cara'.capitalize():
        print("La lista se autodestruirá")
        lista_numeros = []
        return lista_numeros
    else:
        print("La lista fue salvada")
        return lista_numeros


lista_numerous = [1, 2, 15, 7, 2]

lanzar_moneda()

print(probar_suerte(lanzar_moneda(), lista_numerous))
