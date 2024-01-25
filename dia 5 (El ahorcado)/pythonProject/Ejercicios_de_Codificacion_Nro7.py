# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la
# cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    return len(kwargs)


datos_usario = {'Nombre': 'carlos', 'edad': '28'}

print(f'la cantidad de elementos ingresados por el usuario son : {cantidad_atributos(**datos_usario)}')

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
#
# Crea una función llamada lista_atributos que devuelva en forma
# de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer
# recibir cualquier cantidad de argumentos de este tipo.


datos_usario = {'Nombre': 'carlos', 'edad': '28'}


def lista_atributos(**kwargs):
    lista_valores = []
    for valores in kwargs.values():
        lista_valores.append(valores)
    return lista_valores


print(lista_atributos(**datos_usario))


# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de
# argumentos. Esta función deberá mostrar en pantalla:
#
# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:
#
# describir_persona("María", color_ojos="azules", color_pelo="rubio")
#
# Mostrará en pantalla:
#
# Características de María:
# color_ojos: azules
# color_pelo: rubio


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


describir_persona('Eilen', color_ojos='azules', color_pelo='rubio')
