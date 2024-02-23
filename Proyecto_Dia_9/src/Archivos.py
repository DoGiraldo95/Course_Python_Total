import os, re 


def archivo(ruta):
    zip = None  
    for i in os.listdir(ruta): 
        buscar = re.search(r"P\D{7}\+\D{3}\+\d{1}(\.zip)$", i) 
        if buscar is not None:
            zip = buscar.group()
            break
        else :
            zip = ""
    return os.path.join(ruta, zip)
