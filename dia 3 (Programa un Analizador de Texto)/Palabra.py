class Palabra:

    @staticmethod
    def lista_letras(letras):
        lista = letras.lower()
        if ', ' in letras:
            return lista.split(', ')
        else:
            return None

    def __init__(self, txt, letter) -> None:
        self.__text = txt.lower()
        self.__lis_letras = Palabra.lista_letras(letter)

    @property
    def texto(self):
        return self.__text

    @texto.setter
    def texto(self, txt):
        self.__text = txt

    @property
    def letras(self):
        return self.__lis_letras

    @letras.setter
    def letras(self, letras):
        self.__lis_letras = letras


if __name__ == '__main__':

    diccionario = {'nombre': 'Diego Mauricio Giraldo Garcia'}

    booleano = 'garcia'.capitalize() in diccionario['nombre']

    print(booleano)
