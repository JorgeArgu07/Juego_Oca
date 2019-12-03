import pygame, sys
from pygame.locals import *
import random


class Jugador:

    def __init__(self, pantalla, arregloPosiciones, casilla, color):
        self.pantalla = pantalla
        self.arregloPosiciones = arregloPosiciones
        self.casilla = casilla
        self.color = color

    def moverPosicion(self):
        pygame.draw.circle(self.pantalla, self.color,
                           [self.arregloPosiciones[self.casilla][0], self.arregloPosiciones[self.casilla][1]], 20, 0)

        return self.casilla