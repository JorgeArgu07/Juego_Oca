import pygame,sys
from pygame.locals import *
from Tablero import Tablero

ColorBlanco = (255,255,255)
pygame.init()
#pygame.transform_scale(imagen, tamaño)
running = True
display = pygame.display.set_mode((1280, 680))
pygame.display.set_caption("Juego de la Oca")
tablero = Tablero()

while running:
    display.fill(ColorBlanco)
    tablero.dibujar(display, 30,30)
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()