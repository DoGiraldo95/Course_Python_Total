"""Creacion de decorador de turno y la clase TurneroFarmacia"""


def turno_perfume():
    turno = 0
    for i in range(0, 101):
        turno += 1
        yield f'P-{turno}'


def turno_farmacia():
    turno = 0
    for i in range(0, 101):
        turno += 1
        yield f'F-{turno}'


def turno_cosmeticos():
    turno = 0
    for i in range(0, 101):
        turno += 1
        yield f'C-{turno}'


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
