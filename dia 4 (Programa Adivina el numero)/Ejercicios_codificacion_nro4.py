# Práctica Zip 1

# Muestra en pantalla frases como la del siguiente ejemplo:

# La capital de Alemania es Berlín

# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

#     capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
#     paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

paise_capital = list(zip(paises, capitales))

for (pais, capital) in paise_capital:
    print('La capital de %s es %s' % (pais, capital))


# Práctica Zip 2

# Crea un objeto zip formado a partir de listas,
# de un conjunto de marcas y productos que tú prefieras,
# dentro de la variable mi_zip.


marca = ['Nike', 'Adidas', 'New Balance']
producto = ['Nike Cortez', 'Samba', 'NEW BALANCE 420']


mi_zip = zip(marca, producto)

print(type(mi_zip))


# Práctica Zip 3


# Crea el zip con las traducciones los números del 1 al 5 en español,
# portugués e inglés (en el mismo orden),
# y convierte el objeto generado en una lista almacenada en la variable numeros:

# uno / um / one

# dos / dois / two

# tres / três / three

# cuatro / quatro / four

# cinco / cinco / five

# El resultado deberá seguir la estructura:

# [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

espaniol = 'uno dos tres cuatro cinco'
ingles = 'one two three four five'
portuges = 'um dois três quatro cinco'

numeros = list(zip(espaniol.split(), portuges.split(), ingles.split()))

print(numeros)
