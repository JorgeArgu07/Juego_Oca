from random import shuffle
import pygame,sys
from pygame.locals import *

class Menu:
    def __init__(self):
        self.imgfondo = pygame.image.load("resources/fondo.jpg")
        self.ColorVerde = (150,243,23)


    def dibujarmenu(self):
        color = pygame.Color(200, 200, 200)
        pygame.init()
        window = pygame.display.set_mode((1280, 680))
        pygame.display.set_caption('Juego de la Oca')
        while True:
            window.fill(color)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            pygame.display.update()