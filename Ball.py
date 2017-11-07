#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from random import randint
from math import ceil
from shapely.geometry import *
from shapely.geometry.geo import *

class Ball:

    #Constructor Pelota
    def __init__(self, initial_x, initial_y, speed_x, speed_y, radio):
        self.x = initial_x
        self.y = initial_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.t = 0
        self.viva = True
        self.radio = radio
        if (self.radio == 20):
            self.color = (0,255,0)
        if (self.radio == 15):
            self.color = (0,0,255)

    #Updetea la posición de la pelota de acuerdo a su velocidad y el tiempo
    def update(self):
        self.x = self.x + self.speed_x * self.t
        self.y = self.y - self.speed_y * self.t
        self.t += 0.1

    #Dibuja la pelota
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (int(self.x),int(ceil(self.y))),self.radio, self.radio)

    #Chequea si es que se chocó con un bloque
    def crash(self,screen,bloque):
        b1 = Point(self.x,self.y).buffer(self.radio)
        p1 = box(bloque.x, bloque.y, bloque.x + 57, bloque.y+52, ccw=True)
        if p1.intersects(b1):

            if((self.y >= bloque.y + 52)):#choque por abajo
                self.speed_y = - self.speed_y
                bloque.vidas -=1
                if(self.radio == 20):
                    bloque.vidas -=1

            if((self.x <= bloque.x)): #choque por el lado izq
                self.speed_x = -self.speed_x
                bloque.vidas -= 1
                if (self.radio == 20):
                    bloque.vidas -= 1

            if(self.y <= bloque.y):
                self.speed_y = -self.speed_y
                bloque.vidas -= 1
                if (self.radio == 20):
                    bloque.vidas -= 1

            if(self.x >= bloque.x + 57):
                self.speed_x = -self.speed_x
                bloque.vidas -= 1
                if (self.radio == 20):
                    bloque.vidas -= 1

    #Chequea si se chocó con un PowerUp
    def crashPowerUp(self,screen,PowerUp):
        b1 = Point(self.x,self.y).buffer(self.radio)
        b2 = Point(PowerUp.x + 30,PowerUp.y + 30).buffer(25)
        if(b1.intersects(b2)):

            if (PowerUp.choice == 1):
                PowerUp.vida = False
                screen.cant += 1

            if (PowerUp.choice == 2):
                PowerUp.vida = False
                for bloque in screen.bloques:
                    if (bloque.columna == PowerUp.columna):
                        bloque.vidas -= 1

            if (PowerUp.choice == 3):
                PowerUp.vida = False
                for bloque in screen.bloques:
                    if (bloque.fila == PowerUp.fila):
                        bloque.vidas -= 1

            if (PowerUp.choice == 4):
                a = randint(0, 1)
                b = randint(0, 1)
                if (a == 1):
                    self.speed_x = -self.speed_x
                if (b == 1):
                    self.speed_y = -self.speed_y

            if (PowerUp.choice == 5):
                PowerUp.vida = False
                for bloque in screen.bloques:
                    if (bloque.columna == PowerUp.columna):
                        bloque.vidas -= 1
                    if (bloque.fila == PowerUp.fila):
                        bloque.vidas -= 1

            if(PowerUp.choice == 6):
                PowerUp.vida = False
                for bloque in screen.bloques:
                    if(bloque.fila == PowerUp.fila - 1) & ((bloque.columna == PowerUp.columna - 1) |
                            (bloque.columna == PowerUp.columna) | (bloque.columna == PowerUp.columna + 1)):
                        bloque.vidas = 0
                    if(bloque.fila == PowerUp.fila) & ((bloque.columna == PowerUp.columna - 1) |
                                                           (bloque.columna == PowerUp.columna + 1)):
                        bloque.vidas = 0
                    if (bloque.fila == PowerUp.fila + 1) & ((bloque.columna == PowerUp.columna - 1) |
                            (bloque.columna == PowerUp.columna) | (bloque.columna == PowerUp.columna + 1)):
                        bloque.vidas = 0

            if(PowerUp.choice == 7):
                PowerUp.vida = False
                screen.puntuacion += screen.puntuacion







