
import re

texto = 'si necesitas ayuda llama al numero 433-61-56'.title()
patron = r'\d{3}-\d{2}-\d{2}'

buscar = re.search(patron, texto)

if buscar :
    print(buscar.group())
else:
   print( 'no contiene un numero correcto')