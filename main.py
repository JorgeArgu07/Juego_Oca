import pygame, sys
from pygame.locals import *
import Menu
from Tablero import Tablero
from Button import Button
from Dado import Dado
from jugadores import Jugador
import time

#Variables globales
gamers=0
arreglogamers=[]
turno=0
dado1 = Dado()
dado2 = Dado()
dimensiones = [1280, 680]
pantalla = pygame.display.set_mode(dimensiones)
ColorBlanco = (255, 255, 255)
ColorVerde = (150, 243, 23)
ColorRojo = (218, 29, 40)
ColorMorado = (113, 29, 218)
ColorAzul = (29, 218, 207)
ColorGris = (229, 229, 229)
colores=[ColorRojo,ColorAzul,ColorVerde,ColorMorado]
di=0
d2=0



posiciones = [
    [170, 650],
    [200, 560],  # casilla  1
    [265, 560],  # casilla  2
    [334, 560],  # casilla  3
    [403, 560],  # casilla  4
    [468, 560],  # casilla  5
    [536, 560],  # casilla  6
    [604, 560],  # casilla  7
    [669, 560],  # casilla  8
    [724, 540],  # casilla  9
    [748, 495],  # casilla  10

    [752, 438],  # casilla  11
    [752, 374],  # casilla  12
    [752, 309],  # casilla  13
    [752, 243],  # casilla  14
    [752, 180],  # casilla  15
    [742, 140],  # casilla  16
    [693, 110],  # casilla  17
    [637, 110],  # casilla  18
    [580, 110],  # casilla  19
    [526, 110],  # casilla  20

    [468, 110],  # casilla  21
    [408, 110],  # casilla  22
    [348, 110],  # casilla  23
    [288, 110],  # casilla  24
    [230, 110],  # casilla  25
    [174, 110],  # casilla  26
    [138, 125],  # casilla  27
    [118, 160],  # casilla  28
    [110, 213],  # casilla  29
    [110, 280],  # casilla  30

    [110, 340], # casilla  31
    [110, 408],  # casilla  32
    [135, 448],  # casilla  33
    [180, 468],  # casilla  34
    [235, 465],  # casilla  35
    [298, 465],  # casilla  36
    [368, 465],  # casilla  37
    [436, 465],  # casilla  38
    [502, 465],  # casilla  39
    [568, 465],  # casilla  40

    [616, 458],  # casilla  41
    [653, 428],  # casilla  42
    [666, 378],  # casilla  43
    [666, 320],  # casilla  44
    [666, 274],  # casilla  45
    [656, 228],  # casilla  46
    [629, 208],  # casilla  47
    [600, 200],  # casilla  48
    [540, 200],  # casilla  49
    [480, 200],  # casilla  50

    [420, 200],  # casilla  51
    [360, 200],  # casilla  52
    [300, 200],  # casilla  53
    [240, 210],  # casilla  54
    [210, 235],  # casilla  55
    [193, 285],  # casilla  56
    [195, 346],  # casilla  57
    [215, 376],  # casilla  58
    [265, 382],  # casilla  59
    [323, 382],  # casilla  60

    [393, 382],  # casilla  61
    [463, 382],  # casilla  62
    [530, 382],  # casilla  63
    ]
jugador1 = Jugador(pantalla,posiciones,63, ColorAzul,0,0,0,'juab')

def dibijar_mesa():
    panel = pygame.transform.scale(imagen_panel, [1280,680])
    pantalla.blit(panel,[0,0])
    tablero = Tablero()
    display.blit(tablero.dibujar(), (30, 30))

def iniciar():
    p = 0
    actualizar(p)
    running = True
    btnDados = Button(ColorVerde, 985, 200, 150, 50, "Lanzar Dados")


    while running:


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

                    if arreglogamers[p].turnos==0:
                        arreglogamers[p].s=1
                        d1 = dado1.lanzarDado()
                        d2 = dado2.lanzarDado()
                        total = d1 + d2
                        count=0
                        a = posiciones[total]
                        x = a[0]
                        y = a[1]
                        print ("p")
                        print(p)
                        auxi=arreglogamers[p].casilla
                        arreglogamers[p].casillant=auxi
                        aux2=auxi + total
                        if aux2 == 9 or aux2 == 8 or aux2 == 18 or aux2 == 27 or aux2 == 36 or aux2 == 45:
                            total=total+total
                        print(auxi)
                        print(aux2)
                        for auxi in range(total):

                            print(auxi)
                            pi=arreglogamers[p].casilla + 1
                            arreglogamers[p].casilla += 1
                            if pi<=63:
                                arreglogamers[p].moverPosicion()
                                actualizar(p)
                                
                            else:
                                count+=1

                        if arreglogamers[p].casilla==63:
                            Menu.dibujarMenuGanador(arreglogamers[p].nombre)

                        if count>0:
                            arreglogamers[p].casilla = 63
                            actualizar(p)
                            for auxi in range(count):
                                arreglogamers[p].casilla =arreglogamers[p].casilla - 1
                                print(arreglogamers[p].casilla)

                                arreglogamers[p].moverPosicion()
                                actualizar(p)
                        for f in range(gamers):
                            if f!=p:
                                if arreglogamers[p].casilla == arreglogamers[f].casilla:
                                    arreglogamers[f].casilla = arreglogamers[p].casillant
                                    arreglogamers[f].casillant = arreglogamers[f].casilla
                                if arreglogamers[p].casilla==19:
                                    arreglogamers[f].turnos=0
                                    arreglogamers[p].turnos = 2
                                if arreglogamers[p].casilla==42 or arreglogamers[p].casilla==54:
                                    arreglogamers[f].turnos = 0
                                    arreglogamers[p].turnos = 1




                    else:
                        actualizar(p)
                        arreglogamers[p].turnos = 0
                    actualizar(p)
                    arreglogamers[p].s = 0
                    actualizar(p)
                    p = p + 1



                    if p == gamers:
                        p = 0
                    actualizar(p)





def actualizar(p):
    pygame.init()

    # pygame.transform_scale(imagen, tamaño)
    imgfondo = pygame.image.load("resources/fondo.jpg")
    imgfondo = pygame.transform.scale(imgfondo, [1280, 680])
    fuente = pygame.font.SysFont('Calibri', 32)
    nom=arreglogamers[p].nombre
    txtTurno = fuente.render("Jugador en turno "+nom, 1, (0, 0, 0))
    running = True
    display = pygame.display.set_mode((1280, 680))
    pygame.display.set_caption("Juego de la Oca")
    tablero = Tablero()
    btnDados = Button(ColorVerde, 985, 200, 150, 50, "Lanzar Dados")
    rectInt = Button(ColorGris, 870, 70, 390, 570)

    display.blit(imgfondo, (0, 0))
    display.blit(tablero.dibujar(), (30, 30))
    rectInt.draw(display, ColorBlanco)
    btnDados.draw(display, (255, 255, 255))
    display.blit(txtTurno, (960, 280))
    display.blit(dado1.img, (970, 100))
    display.blit(dado2.img, (1070, 100))

    adi = [[985, 400], [1140, 400], [985, 550], [1140, 550]]
    pygame.draw.circle(display, ColorRojo, (985, 400), 50, 0)
    pygame.draw.circle(display, ColorAzul, (1140, 400), 50, 0)
    if gamers==3 or gamers==4:
        pygame.draw.circle(display, ColorVerde, (985, 550), 50, 0)
    if gamers==4:
        pygame.draw.circle(display, ColorMorado, (1140, 550), 50, 0)
    pygame.draw.circle(display, (0, 0, 0), (adi[p][0], adi[p][1]), 50, 5)
    jugador1.moverPosicion()
    for i in range(gamers):
        arreglogamers[i].moverPosicion()
    pygame.display.update()




def jugadores(p, lo):
    print ("sssss")
    for i in range(p):
        color=colores[i]
        nombre=lo[0][i]
        jugador = Jugador(pantalla, posiciones, 0, color,0,0,0, nombre)
        arreglogamers.append(jugador)
        print(arreglogamers[turno].color)


if __name__ == '__main__':
    q=Menu.dibujarmenu()
    gs = []
    if q==1:
        qws=Menu.dibujarmenujugadores()
    if qws == 2:
        gs.append(Menu.dibujarMenuJugadoresNombres(2))
    if qws==3:
        gs.append(Menu.dibujarMenuJugadoresNombres(3))
    if qws==4:
        gs.append(Menu.dibujarMenuJugadoresNombres(4))
    gamers=qws

    print (gs[:])

    print (q)
    print (qws)
    jugadores(gamers, gs)
    iniciar()