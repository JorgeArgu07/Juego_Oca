
import pygame,sys
from pygame.locals import *
from BD import BD




class Puntuacion:

    def getPuntuaciones(self):

        bd = BD()
        puntuaciones = bd.getPuntuaciones()
        print(puntuaciones)
        pygame.init()

        imgfondo = pygame.image.load("resources/fondo.jpg")
        imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
        pygame.display.set_caption('Juego de la Oca')
        window = pygame.display.set_mode((1280, 680))

        fuente = pygame.font.SysFont('Calibri Bold', 100)
        fuente2 = pygame.font.SysFont('Calibri', 50)
        txtTitulo = fuente.render("Puntuaciones", 1, (0, 0, 0))

        nombre = fuente.render("Puntuaciones", 1, (0, 0, 0))   

        punt1 = fuente2.render("Puntos: "+str(puntuaciones[0][1])+" Juegos: "+str(puntuaciones[0][2])+" Jugador: "+puntuaciones[0][0], 1, (0, 0, 0))
        punt2 = fuente2.render("Puntos: "+str(puntuaciones[1][1])+" Juegos: "+str(puntuaciones[1][2])+" Jugador: "+puntuaciones[1][0], 1, (0, 0, 0))
        punt3 = fuente2.render("Puntos: "+str(puntuaciones[2][1])+" Juegos: "+str(puntuaciones[2][2])+" Jugador: "+puntuaciones[2][0], 1, (0, 0, 0))
        

        while True:

            
            
            window.blit(imgfondo, (0, 0))
            window.blit(txtTitulo, (300, 50))
            window.blit(punt1, (300, 150))
            window.blit(punt2, (300, 250))
            window.blit(punt3, (300, 350))
            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == QUIT:
                    sys.exit()

            