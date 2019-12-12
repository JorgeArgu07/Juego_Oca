from random import shuffle
import pygame,sys
from pygame.locals import *
from Tablero import Tablero
from Button import Button

class Menu:
    def __init__(self):
        self.imgfondo = pygame.image.load("resources/fondo.jpg")
        self.ColorVerde = (150,243,23)
        self.ColorBlanco = (255,255,255)
        self.ColorVerde = (150,243,23)
        self.ColorRojo =  (218, 29, 40)
        self.ColorMorado = (113, 29, 218)
        self.ColorAzul = (29, 218, 207)
        self.ColorGris = (229, 229, 229)


    def dibujarmenu(self):
        color = pygame.Color(200, 200, 200)
        pygame.init()

        imgfondo = pygame.image.load("resources/fondo.jpg")
        imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
        pygame.display.set_caption('Juego de la Oca')
        window = pygame.display.set_mode((1280, 680))

        btnStart = Button(self.ColorVerde, 985, 200, 150, 50, "Iniciar Juego")
        btnScore = Button(self.ColorVerde, 985, 200, 150, 50, "Puntuaciones")

        while True:
            window.blit(imgfondo, (0, 0))

            btnStart.draw(window, (255, 255, 255))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
