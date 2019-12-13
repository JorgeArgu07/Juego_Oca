import pygame,sys
from pygame.locals import *
from Tablero import Tablero
from Button import Button
import main

#Variables globales
ColorBlanco = (255, 255, 255)
ColorVerde = (150, 243, 23)
ColorRojo = (218, 29, 40)
ColorMorado = (113, 29, 218)
ColorAzul = (29, 218, 207)
ColorGris = (229, 229, 229)
pygame.init()
fuente = pygame.font.SysFont('Calibri Bold', 100)

def dibujarmenu():
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
                    dibujarmenujugadores()

def dibujarmenujugadores():
    pygame.init()

    imgfondo = pygame.image.load("resources/fondo.jpg")
    imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
    pygame.display.set_caption('Juego de la Oca')
    window = pygame.display.set_mode((1280, 680))

    fuente = pygame.font.SysFont('Calibri Bold', 100)
    txtTitulo = fuente.render("JUEGO DE LA OCA", 1, (0, 0, 0))
    btn2jugadores = Button(ColorVerde, 490, 200, 300, 100, "2 jugadores")
    btn3jugadores = Button(ColorVerde, 490, 340, 300, 100, "3 jugadores")
    btn4jugadores = Button(ColorVerde, 490, 480, 300, 100, "4 jugadores")

    while True:
        window.blit(imgfondo, (0, 0))

        window.blit(txtTitulo, (300, 50))
        btn2jugadores.draw(window, (255, 255, 255))
        btn3jugadores.draw(window, (255, 255, 255))
        btn4jugadores.draw(window, (255, 255, 255))

        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                sys.exit()

            elif event.type == MOUSEMOTION:
                if btn2jugadores.isOver(pos):
                    btn2jugadores.color = (135, 218, 29)
                else:
                    btn2jugadores.color = ColorVerde

                if btn3jugadores.isOver(pos):
                    btn3jugadores.color = (135, 218, 29)
                else:
                    btn3jugadores.color = ColorVerde

                if btn4jugadores.isOver(pos):
                    btn4jugadores.color = (135, 218, 29)
                else:
                    btn4jugadores.color = ColorVerde

            elif event.type == MOUSEBUTTONDOWN:
                if btn2jugadores.isOver(pos):
                    pass
                    dibujarMenuJugadoresNombres(2)
                if btn3jugadores.isOver(pos):
                    pass
                    dibujarMenuJugadoresNombres(3)
                if btn4jugadores.isOver(pos):
                    pass
                    dibujarMenuJugadoresNombres(4)


def dibujarMenuJugadoresNombres(NumeroJugadores):

    imgfondo = pygame.image.load("resources/fondo.jpg")
    imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
    pygame.display.set_caption('Juego de la Oca')
    window = pygame.display.set_mode((1280, 680))


    txtTitulo = fuente.render("JUEGO DE LA OCA", 1, (0, 0, 0))

    #Inputs
    input_box = pygame.Rect(300, 300, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    text = ''
    active = False

    iniciarjuego = Button(ColorVerde, 490, 200, 300, 100, 'Iniciar Juego')

    while True:
        window.blit(imgfondo, (0, 0))

        window.blit(txtTitulo, (300, 50))
        iniciarjuego.draw(window, (255, 255, 255))

        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                sys.exit()

            elif event.type == MOUSEMOTION:
                if iniciarjuego.isOver(pos):
                    iniciarjuego.color = (135, 218, 29)
                else:
                    iniciarjuego.color = ColorVerde

            elif event.type == MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                if iniciarjuego.isOver(pos):
                    pass
                    main.iniciar()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = fuente.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(window, color, input_box, 2)

def imput():
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)