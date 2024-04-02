import pygame, os
from dotenv import load_dotenv


load_dotenv()

class Pantalla:

 
    def __init__(self) -> None:
        self.__tamanio = (1024, 768)
        self.__icono = os.getenv("ICONO")
        self.__nombre_icono = "Clearing"

    @property 
    def tamanio(self):
        return self.__tamanio
    @property
    def icon(self):
        return self.__icono
    @property
    def nom_icon(self):
        return self.__nombre_icono

    def pantalla_aplicativo(self):
        pantalla = pygame.display.set_mode(self.tamanio).fill((93, 148, 243))
        pygame.display.set_icon(pygame.image.load(self.icon))
        pygame.display.set_caption(self.nom_icon)
        return pantalla
        

