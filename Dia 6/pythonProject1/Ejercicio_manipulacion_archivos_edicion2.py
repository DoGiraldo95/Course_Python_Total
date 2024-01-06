registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]


archivo = open('texto4.txt', 'a')
registro_ultima_sesion = '\t'.join(registro_ultima_sesion)
archivo.writelines(registro_ultima_sesion)
archivo.close()


archivo = open('texto4.txt')

for i in archivo:
    print(i.rstrip())

archivo.close()