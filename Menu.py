#!/usr/bin/python

import pygame

#Crea la ventana que alberga el menu
gameDisplay = pygame.display.set_mode((480,640))
clock = pygame.time.Clock()

#Sirve para escribir en la ventana
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

#Funcion que crea el menu
def game_intro():

    intro = True
    while intro:

        #Llena la ventana de negro
        gameDisplay.fill((0, 0, 0))

        #Define los tipos de textos
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        smallText = pygame.font.Font('freesansbold.ttf', 15)


        TextSurf, TextRect = text_objects("Elija una Pelota:", largeText)
        TextRect.center = ((480 / 2), (640 / 3))
        gameDisplay.blit(TextSurf, TextRect)

        #Dibuja las pelotas y escribe sus cualidades
        pygame.draw.circle(gameDisplay, (0, 255, 0), (125, 400), 20, 20)
        TextSurfg, TextRectg = text_objects("x2 destruccion", smallText)
        TextRectg.center = ((125), (450))
        gameDisplay.blit(TextSurfg, TextRectg)

        pygame.draw.circle(gameDisplay, (0, 100, 225), (355, 400), 15, 15)
        TextSurfb, TextRectb = text_objects("x2 puntaje", smallText)
        TextRectb.center = ((355), (450))
        gameDisplay.blit(TextSurfb, TextRectb)

        #Recibe lo que hace el usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0]
                y = mouse_pos[1]
                #Distingue que pelota eligio dependiendo de donde apreto el usuario
                if((x >= 105) & (x <= 145) & (y >= 380) & (y <= 420)):
                    return "green"
                elif ((x >= 340) & (x <= 370) & (y >= 385) & (y <= 415)):
                    return "blue"



        pygame.display.update()
        clock.tick(15)
