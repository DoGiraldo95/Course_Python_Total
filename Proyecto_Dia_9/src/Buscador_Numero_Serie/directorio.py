import os, time
import math
from collections import namedtuple
from dotenv import load_dotenv
from datetime import date
from src.Buscador_Numero_Serie import padron

load_dotenv()

class Directorio:

    RUTA = os.getenv("RUTA_DIRECTORIO")
    ARCHIVOS = []
    NRO_SERIES = []

    @staticmethod
    def decorador(funcion):
        def tiempoEjecucion(*args):
            print("-"*50)
            print(f"Fecha de busqueda: {date.today().strftime("%d/%m/%Y")}")
            inicio = time.time()
            funcion(*args)
            print(f"Duración de la búsqueda: {math.ceil(time.time()-inicio)} segundos")
            print("_"*50)
        return tiempoEjecucion
    
    @classmethod
    def recorrer_directorio(cls):
        Busqueda = namedtuple("Busqueda", ["Archivos", "Numero_Serie"])
        for room, dir, file in os.walk(cls.RUTA):
           for i in file :
               serie = padron.numero_serie(os.path.join(room, i))
               if serie != "":
                   cls.ARCHIVOS.append(i)
                   cls.NRO_SERIES.append(serie)
        encontrados = Busqueda(cls.ARCHIVOS, cls.NRO_SERIES)
        return encontrados
    
    @staticmethod
    @decorador
    def imprimir_busqueda(objeto):
        
        titulo_1 = "archivo".upper()
        titulo_2 = "nro. serie".upper()
        print()
        print(f"""{titulo_1}\t\t{titulo_2}
{"_"*len(titulo_1)}\t\t{"_"*len(titulo_2)}""")
        for i in objeto.Archivos:
            print(f"{i}\t{objeto.Numero_Serie[objeto.Archivos.index(i)]}")
        print(f"\nNumeros encontrados: {len(objeto.Numero_Serie)}")
        


if __name__ == "__main__":
    encontrados =  Directorio.recorrer_directorio()

    Directorio.imprimir_busqueda(encontrados)


