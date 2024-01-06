# Abrir un archivo editar y imprimir su contenido

archivo = open('texto3.txt', 'w')

archivo.write('''Log de erorres
Acciones por el usuario
''')

archivo.close()

archivo = open('texto3.txt')

for i in archivo:
    print(i.rstrip())
archivo.close()


# Editar archivo en un linea final

archivo2 = open('texto3.txt', 'a')
archivo2.write('nuevo inicio de sesión'.capitalize())

archivo2.close()

archivo2 = open('texto3.txt')
for i in archivo2:
    print(i.rstrip())
archivo2.close()
