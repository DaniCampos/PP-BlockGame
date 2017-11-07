#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import randint
import pygame
from pygame.locals import *
import sys
import math
from Ball import Ball
from Window import Window
from Bloque import Bloque
from PowerUp import PowerUp
from centered_figure import*

#Controlador del juego
class Controller:
    def __init__(self,pelota):

        #Dependiendo de la pelota elegida en el menú principal determina con cual se esta jugando
        if(pelota == "green"):
            self.radio = 20
        if(pelota == "blue"):
            self.radio = 15

        #Determina las dimensiones de la pantalla
        self.height = 640
        self.width = 480
        self.ticks_counter = 0

        #Crea la ventana
        pygame.init()
        self.window = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('PP - Block')

        #Crea las listas que contendran los objetos del juego
        self.balls = []
        self.bloques = []
        self.PowerUps = []

        #Le entrega estos objetos a la ventana para dibujarlos
        self.window = Window(self.window, self.balls, self.bloques, self.PowerUps)

        #Crea la pelota inicial
        self.balls.append(Ball(240, 620, 0, 0, self.radio))


        #Crea los Bloques y PowerUps iniciales
        for i in range(-1,7):
            #for j in range(0,4):
            a = randint(1,4)
            if((a == 1) | (a == 2)):
                self.bloques.append(Bloque(76 + i*68, 81,self.window.puntuacion,i,0))
            if(a == 3):
                self.PowerUps.append(PowerUp(76 + i*68, 81, i, 0))

    #Updetea el juego dependiendo de lo que hace el jugador
    def update(self):

        #Le pide a la ventana que se limpie
        self.window.clean()

        #Si la primera pelota vuelve al suelo la inicializa denuevo
        if(self.balls[0].viva == False):
            self.balls[0].x = self.window.player
            self.balls[0].y = 620
            self.balls[0].speed_x = 0
            self.balls[0].speed_y = 0
            self.balls[0].viva = True

            #Esto evita que a medida que avance el juego las pelotas tomen mas velocidad
            for ball in self.balls:
                ball.t = 0

            #Si es que el PowerUp Extra Ball fue seleccionado agrega una pelota a la lista
            for i in range(0,self.window.cant):
                self.balls.append(Ball(self.window.player, 620, 0,0, self.radio))
            self.window.cant = 0

            #Una vez que la pelota toca el suelo todos los bloques y PowerUps bajan un nivel
            for bloque in self.bloques:
                bloque.y += 62
                bloque.fila +=1

            for P  in self.PowerUps:
                P.y += 62
                P.fila += 1

            #Rellena la primera fila
            for i in range(-1,7):
                d = randint(1,4)
                if ((d == 1) | (d == 2)):
                    self.bloques.append(Bloque(76 + i * 68, 81, self.window.puntuacion, i, 0))
                if (d == 3):
                    self.PowerUps.append(PowerUp(76 + i*68,81,i,0))


        #Le pide a la ventana que se dibuje
        self.window.draw()


        self.window.pointerx = -1
        self.window.pointery = -1


        #Interpreta lo que el usuario quiere hacer
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                final_x = mouse_pos[0]
                final_y = mouse_pos[1]
                for ball in self.balls:
                    #Actualiza la velocidad de las pelotas dependiendo de donde cliqueo el usuario
                    op = abs(final_x - ball.x)
                    ady = abs(final_y - ball.y)
                    hip = math.sqrt(op ** 2 + ady ** 2)
                    vx = float(op) / hip
                    vy = float(ady) / hip
                    if (final_x < ball.x):
                        vx = -vx
                    #Si se cliquea bajo los 440 pixeles se aumenta la velocidad en un 10%
                    if(final_y >= 440):
                        ball.speed_x = vx*1.1
                        ball.speed_y = vy*1.1
                    #Si se cliquea bajo los 240 pero sobre los 440 pixeles se aumenta la velocidad en un 20%
                    if(final_y <440) & (final_y >= 240):
                        ball.speed_x = vx * 1.2
                        ball.speed_y = vy * 1.2
                    #Si se cliquea bajo los 240 pixeles se aumenta la velocidad en un 50%
                    if(final_y <240):
                        ball.speed_x = vx * 1.5
                        ball.speed_y = vy * 1.5

            #Crea una guia de lanzamiento si la pelota se encuentra en el piso
            if (event.type == pygame.MOUSEMOTION) & (self.balls[0].y > 600):
                mouse_pos = pygame.mouse.get_pos()
                self.window.pointerx= mouse_pos[0]
                self.window.pointery = mouse_pos[1]


        #Actualiza la velocidad de la pelota si esta choca con los bordes
        for ball in self.balls:
            if (ball.x <= 0):
                ball.speed_x = -ball.speed_x
            if (ball.x >= 435):
                ball.speed_x = -ball.speed_x
            if (ball.y <= 0):
                ball.speed_y = -ball.speed_y
            if (ball.y > 620):
                player = ball.x
                ball.viva = False

        #Chequea si las pelotas chocan con los bloques, si los destruyen aumenta el puntaje
        for bloque in self.bloques:
            for ball in self.balls:
                if(bloque.vida == True):
                    ball.crash(self.window, bloque)
                    if(bloque.vidas <= 0):
                        bloque.vida = False
                        self.window.puntuacion += 1
                        if (self.radio == 15):
                            self.window.puntuacion += 1

        #Chequea si las pelotas chocan con los PowerUps y si es que los PowerUps deben desaparecer dada la altura
        for P in self.PowerUps:
            if(P.y > 500):
                P.vida = False
            for ball in self.balls:
                if(P.vida == True):
                    ball.crashPowerUp(self.window, P)

        #Lanza las pelotas de manera continua
        for i in range(len(self.balls)):
            for j in range(i + 1):
                if(self.balls[j].viva == True):
                    self.balls[j].update()

        #Si la pelota toca el suelo, guarda la posición donde lo hizo para que la siguiente partidad comience ahí
        if(self.balls[0].viva == False):
            self.window.player = self.balls[0].x
        self.ticks_counter += 1

