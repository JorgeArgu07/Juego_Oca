import pygame,sys
from pygame.locals import *
from Tablero import Tablero
from Button import Button
from Dado import Dado

class Main:
    def iniciar(self):

        ColorBlanco = (255,255,255)
        ColorVerde = (150,243,23)
        ColorRojo =  (218, 29, 40)
        ColorMorado = (113, 29, 218)
        ColorAzul = (29, 218, 207)
        ColorGris = (229, 229, 229)
        pygame.init()

        #pygame.transform_scale(imagen, tamaño)
        imgfondo = pygame.image.load("resources/fondo.jpg")
        imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
        fuente = pygame.font.SysFont('Arial', 32)
        txtTurno = fuente.render("Jugador en turno", 1, (0, 0, 0))
        running = True
        display = pygame.display.set_mode((1280, 680))
        pygame.display.set_caption("Juego de la Oca")
        tablero = Tablero()
        btnDados = Button(ColorVerde, 985, 200, 150, 50, "Lanzar Dados")
        rectInt = Button(ColorGris, 870, 70, 390, 570)
        dado1 = Dado()
        dado2 = Dado()


        while running:

            
            display.blit(imgfondo, (0,0))
            display.blit(tablero.dibujar(),(30,30))
            rectInt.draw(display, ColorBlanco)
            btnDados.draw(display, (255,255,255))
            display.blit(txtTurno, (960, 280))
            display.blit(dado1.img, (970, 100))
            display.blit(dado2.img, (1070, 100))

            pygame.draw.circle(display, ColorVerde, (985, 400), 50, 0)
            pygame.draw.circle(display, ColorRojo, (1140, 400), 50, 0)
            pygame.draw.circle(display, ColorMorado, (985, 550), 50, 0)
            pygame.draw.circle(display, ColorAzul, (1140, 550), 50, 0)
            pygame.draw.circle(display, (0,0,0), (985, 400), 50, 5)

            pygame.display.update()


            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    if btnDados.isOver(pos):
                        btnDados.color = (135, 218, 29)
                    else:
                        btnDados.color = ColorVerde
                elif event.type == MOUSEBUTTONDOWN:
                    if btnDados.isOver(pos):
                        pass
                        dado1.lanzarDado()
                        dado2.lanzarDado()

main = Main()
main.iniciar()