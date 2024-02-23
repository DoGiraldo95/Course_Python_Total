import re

def numero_serie(file):
    serie = None
    with open(file) as archivo:
        buscar = re.search(r"N\D{3}-\d{5}", archivo.read())
        if buscar:
            serie = buscar.group()
        else :
            serie = ""
    return serie



if __name__ == "__main__":
    print(numero_serie(r"C:\Users\dgiraldo\Documents\git\Course_Python_Total\Proyecto_Dia_9\Recurso\Mi_Gran_Directorio\Directorio_1\Directorio_1A\archivo3.txt"))