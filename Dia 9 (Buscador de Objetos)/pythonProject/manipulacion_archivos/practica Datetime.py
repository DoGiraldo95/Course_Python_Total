from datetime import date, datetime
import time
"""
[Práctica Módulo Datetime 2]
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
"""
hoy = date.today()

print(hoy)

"""Práctica Módulo Datetime 3
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
"""
tInit = time.time()
minutos = datetime.today().minute
tFin = time.time()
print(minutos)
print(tInit - tFin)
