import re

"""Práctica Módulo RE 1

Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el 
email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque 
aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la 
frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" 
imprimiendo el mensaje."""

"""Notas := 
            [^ Caracter] dentro excluye cualquier caracter dentro de la busqueda
            \\ la barra invertidad puede omitir el comodin o el metadato especial
            . El punto hace coincidir con cualquier caracter 
            * Coincide con cero mas veces el caracter ejemplo ca*t coincidirá con 'ct' (0 'a' caracteres)"""


def verificar_email(email):
    patron = r"\w@{1}\w+\.(com|com\.br)"
    if re.search(patron, email) is not None:
        print('Ok')
    else:
        print('La dirección de email es incorrecta')


"""Práctica Módulo RE 2
Crea una función llamada verificar_saludo para verificar si una frase entregada 
como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar 
mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario 
"No has saludado" imprimiendo el mensaje en pantalla."""


def verificar_saludo(frase):
    if re.search(r"^[Hh]ola", frase) is not None:
        print("Ok")
    else:
        print("No has saludado")
"""
Práctica Módulo RE 3
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). 
Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
"""

def verificar_cp(cp):
    if re.search(r"^\w{2}\d{4}", cp) is not None:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

if __name__ == "__main__":
    # correo = input('Ingrese la direccion de correo : ')
    # verificar_email(correo)

    # padron = r"a[bcd]*b"
    # texto = "abcd"
    #
    # print(re.findall(padron, texto))
    verificar_cp("4X6t66")
