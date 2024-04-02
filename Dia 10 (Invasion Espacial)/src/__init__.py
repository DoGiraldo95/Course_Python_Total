import pygame


pygame.init()
pantalla = pygame.display.set_mode((1024, 768))

def ejecucion():
    running = True

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

ejecucion()