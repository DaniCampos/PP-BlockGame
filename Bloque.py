#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Bloque:
    pygame.font.init()

    #Constructor Bloque
    def __init__(self, x, y, vidas,columna, fila):
        self.x = x
        self.y = y
        self.fila = fila
        self.columna = columna
        if(vidas%10 ==0):
            vidas += vidas
        self.vidas = vidas
        self.vida = True
        if(self.vidas >= 20):
            self.color = (255,255,0)
        if((self.vidas >=10 ) & (self.vidas < 20)):
            self.color = (255, 69, 0)
        if((self.vidas >= 5) & (self.vidas < 10)):
            self.color =  (0,245,255)
        if(self.vidas < 5):
            self.color = (208,32,144)

    #Dibuja el bloque y escribe en el su resistencia
    def draw(self, surface):
        pygame.draw.lines(surface,self.color, False, [(self.x, self.y), (self.x + 57, self.y),
            (self.x + 57, self.y + 52), (self.x, self.y + 52), (self.x, self.y) ], 2)
        myfont = pygame.font.SysFont("monospace", 30)
        label = myfont.render(str(self.vidas), 1, (255, 255, 255))
        surface.blit(label, (self.x + 20, self.y + 15))