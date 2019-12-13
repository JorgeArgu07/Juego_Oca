import pygame, sys
from pygame.locals import *
import random


class Jugador:

    def __init__(self, pantalla, arregloPosiciones, casilla, color,casillant, turnos,s):
        self.pantalla = pantalla
        self.arregloPosiciones = arregloPosiciones
        self.casilla = casilla
        self.color = color
        self.casillant=casillant
        self.turnos=turnos
        self.s=s

    def moverPosicion(self):
        pygame.draw.circle(self.pantalla, self.color,
                           [self.arregloPosiciones[self.casilla][0], self.arregloPosiciones[self.casilla][1]], 20, 0)
        if self.casilla==12 and self.s==0:
            self.casilla=42
            self.casillant=11
            pygame.draw.circle(self.pantalla, self.color,
                               [self.arregloPosiciones[self.casilla][0], self.arregloPosiciones[self.casilla][1]], 20,
                               0)
        if self.casilla==58 and self.s==0:
            self.casilla=1
            self.casillant=1
            pygame.draw.circle(self.pantalla, self.color,
                               [self.arregloPosiciones[self.casilla][0], self.arregloPosiciones[self.casilla][1]], 20,
                               0)




        return self.casilla