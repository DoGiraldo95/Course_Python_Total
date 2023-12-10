"""Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable
llamada prueba"""
lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
prueba = lista1[2] == lista2[0]

print(prueba)

"""
Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
"""

division = 17834 / 34
multiplicacion = 87 * 56

print(division > multiplicacion)

"""
Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()
"""

raiz = 25 ** 0.5
print(raiz == 5)



"""
¿Qué método debo usar para hallar el quinto carácter dentro del string “éxito”, almacenada en la variable palabra?
"""

palabra = 'exito'

print(palabra[4])



redes = ['Youtube', 'Facebook', 'Twitter']
redes.sort()
print(redes)