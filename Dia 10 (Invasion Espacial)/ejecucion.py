import pygame
from src.setup import pantalla


def ejecucion():
    pygame.init()
    pantalla.Pantalla().pantalla_aplicativo()

    running = True

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False                                 
        pygame.display.update()

if __name__ == "__main__":
    ejecucion()