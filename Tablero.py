import pygame, sys
from pygame.locals import *
class Tablero:
    def __init__(self):
        self.img = pygame.image.load("resources/tablero.jpg")

    def dibujar(self, ventana, x, y):
        tablero = pygame.transform.scale(self.img, [800, 600])
        ventana.blit(tablero, (x, y))