
def devolver_distintos(num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    suma = sum(lista_numeros)

    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    intermedio = suma - menor - mayor

    if 10 <= suma <= 15:
        return intermedio
    elif suma < 10:
        return menor
    else:
        return mayor


print(devolver_distintos(6, 4, 3))


def letras_unicas(palabra):
    unicas = set()
    for letra in palabra:
        unicas.add(letra)
    lista = list(unicas)
    lista.sort()
    return lista


print(letras_unicas("entretenido"))


def numero_cero(*args):
    indice = 0

    while indice < len(args):
        if args[indice] == 0 and args[indice + 1] == 0:
            return True
        indice += 1
    return False


print(numero_cero(6, 0, 5, 1, 0, 3, 0, 0))


def numero_primo(numero):
    contador_primos = 0
    if type(numero) == int:
        for numero in range(0, numero):
            if 1 < numero > 0 == numero % numero:
                contador_primos += 1
    return contador_primos


print(f'Cantidad numeros primos:= {numero_primo(5)}')
