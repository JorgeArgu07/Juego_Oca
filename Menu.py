import pygame,sys
from pygame.locals import *
from Tablero import Tablero
from Button import Button
import main
import Puntuacion

#Variables globales
ColorBlanco = (255, 255, 255)
ColorVerde = (150, 243, 23)
ColorRojo = (218, 29, 40)
ColorMorado = (113, 29, 218)
ColorAzul = (29, 218, 207)
ColorGris = (229, 229, 229)
ColorNegro = (000,000,000)
nombre1 = ''
nombre2 = ''
nombre3 = ''
nombre4 = ''

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
                    return 1
                if btnScore.isOver(pos):
                    pass
                    return 2

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
                    return 2
                if btn3jugadores.isOver(pos):
                    pass
                    return 3
                if btn4jugadores.isOver(pos):
                    pass
                    return 4

def monos():
    return [nombre1,nombre2,nombre3,nombre4]
def dibujarMenuJugadoresNombres(NumeroJugadores):
    pygame.init()
    fuenteTitulo = pygame.font.SysFont('Calibri', 100)
    fuente = pygame.font.SysFont('Calibri', 32)
    imgfondo = pygame.image.load("resources/fondo.jpg")
    imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
    pygame.display.set_caption('Juego de la Oca')
    window = pygame.display.set_mode((1280, 680))


    txtTitulo = fuenteTitulo.render("JUEGO DE LA OCA", 1, (0, 0, 0))

    #Inputs
    input_box1 = pygame.Rect(570, 200, 140, 32)
    input_box2 = pygame.Rect(570, 250, 140, 32)
    input_box3 = pygame.Rect(570, 300, 140, 32)
    input_box4 = pygame.Rect(570, 350, 140, 32)

    color_inactive = pygame.Color(0,0,0)
    color_active = pygame.Color(113, 29, 218)
    color1 = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    color4 = color_inactive
    clock = pygame.time.Clock()
    nombre1 = ''
    nombre2 = ''
    nombre3 = ''
    nombre4 = ''

    active1 = False
    active2 = False
    active3 = False
    active4 = False

    iniciarjuego = Button(ColorVerde, 570, 450, 200, 50, 'Iniciar Juego')
    fondoMenu = pygame.Rect(520, 150, 300, 275)

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
                if input_box1.collidepoint(event.pos):
                    # Toggle the active variable.
                    active1 = not active1
                else:
                    active1 = False

                if input_box2.collidepoint(event.pos):
                    # Toggle the active variable.
                    active2 = not active2
                else:
                    active2 = False

                if input_box3.collidepoint(event.pos):
                    # Toggle the active variable.
                    active3 = not active3
                else:
                    active3 = False

                if input_box4.collidepoint(event.pos):
                    # Toggle the active variable.
                    active4 = not active4
                else:
                    active4 = False

                # Change the current color of the input box.
                color1 = color_active if active1 else color_inactive
                color2 = color_active if active2 else color_inactive
                color3 = color_active if active3 else color_inactive
                color4 = color_active if active4 else color_inactive
                if iniciarjuego.isOver(pos):
                    pass
                    return [nombre1, nombre2, nombre3, nombre4]

            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        nombre1 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        nombre1 = nombre1[:-1]
                    else:
                        nombre1 += event.unicode

                if active2:
                    if event.key == pygame.K_RETURN:
                        nombre2 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        nombre2 = nombre2[:-1]
                    else:

                        nombre2 += event.unicode

                if active3:
                    if event.key == pygame.K_RETURN:
                        nombre3 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        nombre3 = nombre3[:-1]
                    else:
                        nombre3 += event.unicode

                if active4:
                    if event.key == pygame.K_RETURN:
                        nombre4 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        nombre4 = nombre4[:-1]
                    else:
                        nombre4 += event.unicode

        pygame.draw.rect(window, ColorBlanco, fondoMenu, 0)
        if NumeroJugadores == 2:
            txt_surface1 = fuente.render(nombre1, True, color1)
            width = max(200, txt_surface1.get_width() + 10)
            input_box1.w = width
            # Blit the text.
            window.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color1, input_box1, 2)

            txt_surface2 = fuente.render(nombre2, True, color2)
            width = max(200, txt_surface2.get_width() + 10)
            input_box2.w = width
            # Blit the text.
            window.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color2, input_box2, 2)

        if NumeroJugadores == 3:
            txt_surface1 = fuente.render(nombre1, True, color1)
            width = max(200, txt_surface1.get_width() + 10)
            input_box1.w = width
            # Blit the text.
            window.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color1, input_box1, 2)

            txt_surface2 = fuente.render(nombre2, True, color2)
            width = max(200, txt_surface2.get_width() + 10)
            input_box2.w = width
            # Blit the text.
            window.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color2, input_box2, 2)

            txt_surface3 = fuente.render(nombre3, True, color3)
            width = max(200, txt_surface3.get_width() + 10)
            input_box3.w = width
            # Blit the text.
            window.blit(txt_surface3, (input_box3.x + 5, input_box3.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color3, input_box3, 2)

        if NumeroJugadores == 4:
            txt_surface1 = fuente.render(nombre1, True, color1)
            width = max(200, txt_surface1.get_width() + 10)
            input_box1.w = width
            # Blit the text.
            window.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color1, input_box1, 2)

            txt_surface2 = fuente.render(nombre2, True, color2)
            width = max(200, txt_surface2.get_width() + 10)
            input_box2.w = width
            # Blit the text.
            window.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color2, input_box2, 2)

            txt_surface3 = fuente.render(nombre3, True, color3)
            width = max(200, txt_surface3.get_width() + 10)
            input_box3.w = width
            # Blit the text.
            window.blit(txt_surface3, (input_box3.x + 5, input_box3.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color3, input_box3, 2)

            txt_surface4 = fuente.render(nombre4, True, color4)
            width = max(200, txt_surface4.get_width() + 10)
            input_box4.w = width
            # Blit the text.
            window.blit(txt_surface4, (input_box4.x + 5, input_box4.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color4, input_box4, 2)

        pygame.display.flip()
        clock.tick(10)


def dibujarMenuGanador(nombreGanador):
    pygame.init()

    imgfondo = pygame.image.load("resources/fondo.jpg")
    imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
    pygame.display.set_caption('Juego de la Oca')
    window = pygame.display.set_mode((1280, 680))

    fuente = pygame.font.SysFont('Calibri Bold', 100)
    txtTitulo = fuente.render("FELICIDADES", 1, (0, 0, 0))
    txtTitulo1 = fuente.render(nombreGanador, 1, (0, 0, 0))
    txtTitulo2 = fuente.render("HAS GANADO!!", 1, (0, 0, 0))
    btnStart = Button(ColorVerde, 490, 400, 300, 100, "Salir")

    while True:
        window.blit(imgfondo, (0, 0))

        window.blit(txtTitulo, (400, 100))
        window.blit(txtTitulo1, (550, 200))
        window.blit(txtTitulo2, (370, 300))
        btnStart.draw(window, (255, 255, 255))

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

            elif event.type == MOUSEBUTTONDOWN:
                if btnStart.isOver(pos):
                    pass
                    sys.exit()
