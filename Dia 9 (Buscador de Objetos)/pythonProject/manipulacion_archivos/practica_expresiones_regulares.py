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


if __name__ == "__main__":
    # correo = input('Ingrese la direccion de correo : ')
    # verificar_email(correo)

    padron = r"a[bcd]*b"
    texto = "abcd"

    print(re.findall(padron, texto))
