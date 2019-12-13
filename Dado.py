import pygame, sys
from pygame.locals import *
import random

class Dado:
    def __init__(self):
        imagen = pygame.image.load("resources/dado_uno.png")
        cara = pygame.transform.scale(imagen, [80, 80])
        self.img = cara
        self.num = 0

    def lanzarDado(self):
        num = random.randint(1,6)
        width = 80
        height = 80

        if num == 1:
            self.num = num
            imagen = pygame.image.load("resources/dado_uno.png")
            cara = pygame.transform.scale(imagen, [width, height])
            self.img = cara
        elif num == 2:
            self.num = num
            imagen = pygame.image.load("resources/dado_dos.png")
            cara = pygame.transform.scale(imagen, [width, height])
            self.img = cara

        elif num == 3:
            self.num = num
            imagen = pygame.image.load("resources/dado_tres.png")
            cara = pygame.transform.scale(imagen, [width, height])
            self.img = cara

        elif num == 4:
            self.num = num
            imagen = pygame.image.load("resources/dado_cuatro.png")
            cara = pygame.transform.scale(imagen, [width, height])
            self.img = cara

        elif num == 5:
            self.num = num
            imagen = pygame.image.load("resources/dado_cinco.png")
            cara = pygame.transform.scale(imagen, [width, height])
            self.img = cara

        elif num == 6:
            self.num = num
            imagen = pygame.image.load("resources/dado_seis.png")
            cara = pygame.transform.scale(imagen, [width, height])
            self.img = cara
        return num