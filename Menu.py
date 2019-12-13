from random import shuffle
import pygame,sys
from pygame.locals import *
from Tablero import Tablero
from Button import Button
from main import *


class Menu:
    def __init__(self):
        self.imgfondo = pygame.image.load("resources/fondo.jpg")
        self.ColorVerde = (150,243,23)
        self.ColorBlanco = (255,255,255)
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

        fuente = pygame.font.SysFont('Calibri Bold', 100)
        txtTitulo = fuente.render("JUEGO DE LA OCA", 1, (0, 0, 0))
        btnStart = Button(ColorVerde, 490, 200, 300, 100, "Iniciar Juego")
        btnScore = Button(ColorVerde, 490, 340, 300, 100, "Puntuaciones")

        while True:
            window.blit(imgfondo, (0, 0))

            window.blit(txtTitulo, (300, 50))
            btnStart.draw(window, (255, 255, 255))
            btnScore.draw(window, (255, 255, 255))

            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == QUIT:
                    sys.exit()

                elif event.type == MOUSEMOTION:
                    if btnStart.isOver(pos):
                        btnStart.color = (135, 218, 29)
                    else:
                        btnStart.color = ColorVerde

                    if btnScore.isOver(pos):
                        btnScore.color = (135, 218, 29)
                    else:
                        btnScore.color = ColorVerde
                elif event.type == MOUSEBUTTONDOWN:
                    if btnStart.isOver(pos):
                        pass
                        main = main()
                        main.iniciar()

menu = Menu()
menu.dibujarmenu()