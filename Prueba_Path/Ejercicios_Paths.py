from pathlib import Path

descargas = Path(Path.home(), 'Downloads')

print(descargas)


def archivos_pdf():
    descargas = Path(Path.home(), 'Downloads')
    archivos = []

    for archivo in descargas.glob('*.pdf'):
        if '.pdf' in archivo.suffix:
            print(archivo.name)
            archivos.append(archivo.name)
    return archivos


print(archivos_pdf())

# if len(archivos_pdf()) > 0:
#   Path.mkdir(Path(descargas, 'archivos_pdf'))

print(len(archivos_pdf()))

# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

ruta_base = Path.home()

print(ruta_base)

# Práctica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir
# de la siguiente estructura de carpetas:

# "Curso Python"
# "Día 6"
# "practicas_path.py"


ruta = Path("Curso Python", "Día 6", "practicas_path.py")

print(ruta)

# Práctica Path 3
#
# Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir
# de la siguiente estructura de carpetas:
#
# "Curso Python"
# "Día 6"
# "practicas_path.py"

ruta = Path(ruta_base, ruta)

print(ruta)
