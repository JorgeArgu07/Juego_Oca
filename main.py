import pygame,sys
from pygame.locals import *
from Tablero import Tablero
from Button import Button
from Dado import Dado

#Variables globales
ColorBlanco = (255, 255, 255)
ColorVerde = (150, 243, 23)
ColorRojo = (218, 29, 40)
ColorMorado = (113, 29, 218)
ColorAzul = (29, 218, 207)
ColorGris = (229, 229, 229)

def iniciar():
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

def dibujarmenu():
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
                    iniciar()


if __name__ == '__main__':
    dibujarmenu()