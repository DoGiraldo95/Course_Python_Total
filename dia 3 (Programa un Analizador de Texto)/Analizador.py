from Palabra import Palabra
from loggin import log


class Analizador:

    diccionario = {}

    @classmethod
    def analisis_texto(cls, text, letras):
        analisis = Palabra(text, letras)

        cls.diccionario['TEXTO_USUARIO'] = analisis.texto
        cls.diccionario['LETRAS_USUARIO'] = analisis.letras

        log.info('Registro Exitoso')

        return cls.diccionario

    @classmethod
    def contador_letra_texto(cls):
        letras = cls.diccionario['LETRAS_USUARIO']
        texto_usuario = cls.diccionario['TEXTO_USUARIO']

        for i in letras:
            log.info(
                f'La letra {i} aparece en el texto {texto_usuario.count(i)}'.title())

    @classmethod
    def contador_palabras(cls):
        texto_usuario = cls.diccionario['TEXTO_USUARIO'].split()
        log.info(
            f'cantidad de palabras en el texto := {len(texto_usuario)}'.title())
        return texto_usuario

    @classmethod
    def primera_ultima_letra(cls):
        texto_usuario = cls.diccionario['TEXTO_USUARIO']
        log.info(f"""primera letra del texto es {texto_usuario[0]}
ultima letra del texto es {texto_usuario[-1]}""".title())

    @classmethod
    def texto_invertido(cls):
        texto_usuario = cls.contador_palabras()
        texto_usuario.reverse()
        log.info(f"""Texto invertido es:
{" ".join(texto_usuario)}""")

    @classmethod
    def encontrar_python(cls):
        dic_texto = cls.contador_palabras()

        if 'python' in dic_texto:
            log.debug(
                f'La palabra se encuentra en el texto del usuario en la posicion := {dic_texto.index("python")}')

        else:
            log.debug('La palabra no se encuentra en el texto')


if __name__ == '__main__':

    texto = input('Ingrese el texto : ')
    letters = input('Ingrese el las letras que desea separadas en , : ')

    diccionario = Analizador.analisis_texto(texto, letters)

    Analizador.contador_letra_texto()
    Analizador.contador_palabras()
    Analizador.primera_ultima_letra()
    Analizador.texto_invertido()
    Analizador.encontrar_python()

    # log.debug(type(diccionario['LETRAS_USUARIO']))
