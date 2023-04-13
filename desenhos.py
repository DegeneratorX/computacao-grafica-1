import pygame
import numpy
import time


class Screen:
    def __init__(self, width, height, background_color):
        self.__screen = pygame.display.set_mode((width, height))
        self.__background_color = background_color

    def set_pixel(self, x, y, color):
        x = x + 1
        y = y + 1
        if x < 1:
            x = 1
        if y < 1:
            y = 1
        if x > self.__screen.get_width():
            x = self.__screen.get_width()
        if y > self.__screen.get_height():
            y = self.__screen.get_height()
        self.__screen.set_at((x, y), color.get_rgba())


    def senoide(self):
        for x in range(self.__screen.get_width()-1):
            y = (self.__screen.get_height()/2)+5*numpy.sin(x*0.2)
            y = int(y)
            self.set_pixel(x, y, Color(255, 255, 255))

    def reta_DDA(self, x_inicial, y_inicial, x_final, y_final, color):
        variacao_x = x_final-x_inicial
        variacao_y = y_final-y_inicial

        passos = abs(variacao_x)
        if abs(variacao_y) > abs(variacao_x):
            passos = abs(variacao_y)

        if passos == 0:
            self.set_pixel(x_inicial, y_inicial, color)
            return
        
        passo_x = variacao_x/passos
        passo_y = variacao_y/passos

        for i in range(passos):
            x = round(x_inicial + i*passo_x)
            y = round(y_inicial + i*passo_y)
            self.set_pixel(x, y, color)

    def clear_screen(self):
        self.__screen.fill(self.__background_color.get_rgba())

    def update(self):
        pygame.display.update()


class Color:
    def __init__(self, red, green, blue, alpha=255):
        if (-1 < red < 256):
            self.__red = red
        else:
            self.__red = 0
        if (-1 < green < 256):
            self.__green = green
        else:
            self.__green = 0
        if (-1 < blue < 256):
            self.__blue = blue
        else:
            self.__blue = 0
        if (-1 < alpha < 256):
            self.__alpha = alpha
        else:
            self.__alpha = 255

    def get_rgba(self):
        return (self.__red, self.__green, self.__blue, self.__alpha)


WINDOW_WIDTH = 250
WINDOW_HEIGHT = 250

screen = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(0, 0, 0))

while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen.clear_screen()
    screen.set_pixel(50, 50, Color(255, 255, 0))
    screen.senoide()
    screen.reta_DDA(20,40,150,170,Color(0,255,100))

    screen.update()
    clock.tick(60)
