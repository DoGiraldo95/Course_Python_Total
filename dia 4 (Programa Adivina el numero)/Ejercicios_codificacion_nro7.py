# Práctica Comprensión de Listas 1


# convertir una lista de medidas pies a metros

form_metros = (1.0/3.28)

pies = [10, 20, 30, 40, 50]

metros = [round((pie * form_metros), 2) for pie in pies]

print(metros)


# Para realizar el ejercicio a continuación, puedes optar por diferentes caminos.
# Si bien en programación el camino correcto es el que devuelve el resultado correcto,
# te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar
# a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

# Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

# valores = [1, 2, 3, 4, 5, 6, 9.5]

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [numero**2 for numero in valores]

print(valores_cuadrado)


# Crea una lista valores_pares formada por
# los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [numero for numero in valores if numero % 2 == 0]

print(valores_pares)


# Para la siguiente lista de temperaturas en grados Fahrenheit,
# expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius.
# La conversión entre tipo de unidades es la siguiente:

# °C = (°F - 32) * (5/9)

# o expresado de otro modo:

# (grados_fahrenheit-32)*(5/9)


temperatura_fahrenheit = [32, 212, 275]


def celsius(temperatura):
    return ((temperatura - 32)*(5/9))


grados_celsius = [celsius(temperatura)
                  for temperatura in temperatura_fahrenheit]

print(grados_celsius)
