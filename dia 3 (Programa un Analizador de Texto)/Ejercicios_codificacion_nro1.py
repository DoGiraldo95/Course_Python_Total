"""
Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
"""

# palabra = "ordenador"

# print(palabra[4])

'''
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
'''
# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# print(frase.index('práctica'))

'''
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
'''

# frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

# print(frase.index('práctica',frase.index('práctica')+1))

'''
Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:

"Controlar la complejidad es la esencia de la programación"
'''

# frase = "Controlar la complejidad es la esencia de la programación"

'''
Extraer palabras desde los indices, comenzando desde un rango inicial hasta un rango final example [rangoIni:rangoFinal]
'''

# print(frase[:len('Controlar')]) 

'''
Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
'''

# frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

# print(frase[8::3])

'''
Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
'''

frase = 'Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza'

print(frase[::-1])
