import pygame

class Window:
    pygame.font.init()

    #Constructor Ventana
    def __init__(self,screen,balls,bloques,PowerUps):
        self.balls = balls
        self.bloques = bloques
        self.PowerUps = PowerUps
        self.window = screen
        self.color = (0,0,0)
        self.player = 217
        self.puntuacion = 1
        self.cant = 0
        self.pointerx = -1
        self.pointery = -1

    #Limpia la ventana
    def clean(self):
        self.window.fill(self.color)

    #Dibuja objetos y otros en la ventana
    def draw(self):

        #Dibuja la guia de lanzamiento si es que la pelota se encuentra en el borde inferior
        if((self.pointerx != -1) & (self.pointery != -1)):
            pygame.draw.lines(self.window, (255, 255, 255), False, [(self.balls[0].x, self.balls[0].y), (self.pointerx, self.pointery)],2)

        #Dibuja todas las pelotas con vida
        for ball in self.balls:
            if(ball.viva == True):
                ball.draw(self.window)

        #Dibuja los bloques con vida
        for bloque in self.bloques:
            if((bloque.vida == True) & (bloque.vidas > 0)):
                bloque.draw(self.window)

        #Dibuja los PowerUps con vida
        for PowerUp in self.PowerUps:
            if(PowerUp.vida == True):
                PowerUp.draw(self.window)

        #Muestra la puntuacion
        myfont = pygame.font.SysFont("monospace", 30)
        label = myfont.render(str(self.puntuacion), 1, (255, 255, 255))
        self.window.blit(label, (430, 11))
        pygame.draw.lines(self.window, (255, 255, 255), False, [(420,10), (420,43), (475,43), (475,10), (420,10)], 3)

        #Dibuja los limites donde pueden haber bloques
        pygame.draw.lines(self.window, (255,255,255), False, [(0,530),(480,530)], 2)
        pygame.draw.lines(self.window, (255, 255, 255), False, [(0, 80), (480, 80)], 2)

        #Si es que los bloques atraviezan el limite inferior muestra GAMEOVER
        for bloque in self.bloques:
            if(bloque.y > 510):
                myfont = pygame.font.SysFont("monospace", 80)
                label = myfont.render("GAME OVER", 1, (255, 255, 255))
                self.window.blit(label, (20, 250))

        pygame.display.flip()
