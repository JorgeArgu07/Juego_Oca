import pygame, sys
from pygame.locals import *
class Tablero:
    def __init__(self):
        self.img = pygame.image.load("resources/tablero.jpg")

    def dibujar(self):
        tablero = pygame.transform.scale(self.img, [800, 600])
        return tablero