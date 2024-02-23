import os, shutil, logging, time




logging.basicConfig(format="%(asctime)s - %(levelname)s := %(message)s", level=logging.DEBUG, datefmt="%d-%m-%Y %I:%M:%S %p")

def decorador(funcion):
    def decora_descomprimir(*args):
        inicio = time.time()
        funcion(*args)
        print(f"tiempo de ejecucion --> {round(time.time()-inicio,2)}".title())
    return decora_descomprimir

@decorador
def descomprimir_archivo(archivo, destino):
    try:
        shutil.unpack_archive(archivo, destino, "zip")
    except ValueError  as ve:
        logging.error(f"Ocurrio un error en la ejecucion := {ve}")
    else:
        logging.info(f"Archivo descomprimido en la ruta --> {destino}")
        os.remove(archivo)
