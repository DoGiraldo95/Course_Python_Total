"""Creacion de decorador de turno y la clase TurneroFarmacia"""


def turno_perfume():
    for i in range(1, 101):
        turno = i
        yield f'P-{turno}'


def turno_farmacia():
    for i in range(1, 101):
        turno = i
        yield f'P-{turno}'


def turno_cosmeticos():
    for i in range(1, 101):
        turno = i
        yield f'P-{turno}'


p = turno_perfume()
f = turno_farmacia()
c = turno_cosmeticos()


def decorador(tipo_turno):
    print("Su turno es :")
    match tipo_turno:
        case 'P':
            print(next(p))
        case 'F':
            print(next(f))
        case 'C':
            print(next(c))

    print("aguarde y será atendido")
