import os
from src import Archivos, Descomprimir
from dotenv import load_dotenv

load_dotenv()

def run():
    archivo = Archivos.archivo(ruta=os.environ.get("RUTA_DESCARGAS"))
    Descomprimir.descomprimir_archivo(archivo, os.environ.get("RUTA_RECURSO"))

run()