#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

import pygame
pygame.font.init()


class PowerUp:
    def __init__(self, x, y, columna, fila):
        self.x = x
        self.y = y
        self.columna = columna
        self.fila = fila
        self.choice = randint(1,7)
        self.vida = True

    #Dibuja los PowerUps
    def draw(self, screen):

        if(self.choice == 1):#ExtraBall
            pygame.draw.circle(screen, (255, 255, 0), (self.x + 30, self.y + 30), 25)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 30, self.y + 15), (self.x + 30, self.y + 43)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 15, self.y + 30), (self.x + 43, self.y + 30)], 3)

        if(self.choice == 2):#VerticalLaser
            pygame.draw.circle(screen, (255, 255, 0), (self.x + 30, self.y + 30), 25)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 30, self.y + 10), (self.x + 30, self.y + 48)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 20, self.y + 20), (self.x + 30, self.y + 10)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 40, self.y + 20), (self.x + 30, self.y + 10)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 20, self.y + 38), (self.x + 30, self.y + 48)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 40, self.y + 38), (self.x + 30, self.y + 48)], 3)


        if(self.choice == 3):#HorizontalLaser
            pygame.draw.circle(screen, (255, 255, 0), (self.x + 30, self.y + 30), 25)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 10, self.y + 30), (self.x + 48, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 20, self.y + 40), (self.x + 10, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 20, self.y + 20), (self.x + 10, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 38, self.y + 40), (self.x + 48, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 38, self.y + 20), (self.x + 48, self.y + 30)], 3)

        if(self.choice == 4):#ChangePath
            pygame.draw.circle(screen, (255, 255, 0), (self.x + 30, self.y + 30), 25)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 10, self.y + 35), (self.x + 20, self.y + 25)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 20, self.y + 25), (self.x + 30, self.y + 35)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 30, self.y + 35), (self.x + 40, self.y + 25) ], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 40, self.y + 25), (self.x + 50, self.y + 35)], 3)

        if (self.choice == 5):#Horizontal&VerticalLaser BONUS
            pygame.draw.circle(screen, (255, 255, 0), (self.x + 30, self.y + 30), 25)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 30, self.y + 10), (self.x + 30, self.y + 48)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 25, self.y + 15), (self.x + 30, self.y + 10)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 35, self.y + 15), (self.x + 30, self.y + 10)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 25, self.y + 43), (self.x + 30, self.y + 48)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 35, self.y + 43), (self.x + 30, self.y + 48)], 3)

            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 10, self.y + 30), (self.x + 48, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 15, self.y + 35), (self.x + 10, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 15, self.y + 25), (self.x + 10, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 43, self.y + 35), (self.x + 48, self.y + 30)], 3)
            pygame.draw.lines(screen, (0, 0, 0), False, [(self.x + 43, self.y + 25), (self.x + 48, self.y + 30)], 3)

        if (self.choice == 6):  #ExplosionBonus BONUS
            pygame.draw.circle(screen, (255, 255, 0), (self.x + 30, self.y + 30), 25)
            myfont = pygame.font.SysFont("monospace", 20)
            label = myfont.render("BUM", 1, (255,0, 0))
            screen.blit(label, (self.x + 12, self.y + 18))

        if (self.choice == 7): #DoublePuntuation BONUS
            pygame.draw.circle(screen,(0,245,255), (self.x + 30, self.y + 30), 25)
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("$", 1, (0, 0, 0))
            screen.blit(label, (self.x + 21, self.y + 15))



