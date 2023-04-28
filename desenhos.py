import pygame
import numpy as np
import time


class Screen:
    def __init__(self, width, height, background_color):
        self.__screen_matrix = []
        for i in range(height):
            self.__screen_matrix.append([0]*width)
        self.__background_color = background_color
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((self.__width, self.__height), pygame.RESIZABLE)

    # Esse método serve para tratar coordenadas que podem ser maiores que o tamanho
    # da matriz. Portanto, em C++, acessaria lixo na mémória. O set_at do python
    # da lib pygame também deve tratar, mas por precaução, estou fazendo aqui
    # também, como forma didática.
    def get_screen(self):
        return self.__screen

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
            y = (self.__screen.get_height()/2)+5*np.sin(x*0.2)
            y = int(y)
            self.set_pixel(x, y, Color(255, 255, 255))

    def reta_DDA(self, x_inicial, y_inicial, x_final, y_final, color, antialiasing=False):
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
            if antialiasing == True:
                red, green, blue, alpha = color.get_rgba()
                if abs(round(passo_x)) == 1:
                    y_decimal = y - np.floor(y)
                    # TODO: Erro ao multiplicar float com classe Color. O que fazer?
                    # Preciso reduzir em % de acordo com a intensidade da cor cada cor para o antiserrilhado.

                    color_serrilhado_1 = Color(round(
                        (1-y_decimal)*red), round((1-y_decimal)*green), round((1-y_decimal)*blue), alpha)
                    color_serrilhado_2 = Color(
                        round((y_decimal)*red), round((y_decimal)*green), round((y_decimal)*blue), alpha)

                    self.set_pixel(int(round(x)), int(
                        np.floor(y)), color_serrilhado_1)
                    self.set_pixel(int(round(x)), int(
                        np.floor(y+1)), color_serrilhado_2)
                else:
                    x_decimal = x - np.floor(x)

                    color_serrilhado_1 = Color(round(
                        (1-x_decimal)*red), round((1-x_decimal)*green), round((1-x_decimal)*blue), alpha)
                    color_serrilhado_2 = Color(
                        round((x_decimal)*red), round((x_decimal)*green), round((x_decimal)*blue), alpha)

                    self.set_pixel(int(np.floor(x)), int(
                        round(y)), color_serrilhado_1)
                    self.set_pixel(int(np.floor(x+1)),
                                   int(round(y)), color_serrilhado_2)
            else:
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


WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100

screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
screen = screen_object.get_screen()
while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen_object.clear_screen()
    screen_object.set_pixel(50, 50, Color(255, 0, 0, 50))
    # screen.senoide()
    screen_object.reta_DDA(20, 200, 100, 170, Color(255, 0, 0, 50), True)

    screen_object.update()
    clock.tick(60)
