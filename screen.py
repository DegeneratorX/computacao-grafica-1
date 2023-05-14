import pygame

class Screen:
    # Construtor da classe Screen
    def __init__(self, width, height, background_color):
        self.__screen_matrix = []
        for i in range(height):
            self.__screen_matrix.append([0]*width)
        self.__background_color = background_color
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode(
            (self.__width, self.__height), pygame.RESIZABLE)

    # Método que eu pego a screen para que eu possa fazer alterações nela na main caso eu deseje.

    def get_screen(self):
        return self.__screen

    # Esse método serve para tratar coordenadas que podem ser maiores que o tamanho
    # da matriz. Portanto, em C++, acessaria lixo na mémória. O set_at do python
    # da lib pygame também deve tratar, mas por precaução, estou fazendo aqui
    # também, como forma didática.

    def get_pixel(self, x, y, textura):
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        if x >= self.__screen.get_width():
            x = self.__screen.get_width()-1
        if y >= self.__screen.get_height():
            y = self.__screen.get_height()-1

        return self.__screen.get_at((x, y))

    def set_pixel(self, x, y, color):

        # Se as coordenadas forem negativas, passam a ser no minimo zero.
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        # Truncamento de x e y. Se for maior que o tamanho da matriz, vira as
        # coordenadas do tamanho da matriz.
        if x >= self.__screen.get_width():
            x = self.__screen.get_width()-1
        if y >= self.__screen.get_height():
            y = self.__screen.get_height()-1

        # Setpixel definitivo
        self.__screen.set_at((x, y), color.get_rgba())

    # Desenha uma senóide na matriz. O problema é que ela só itera em x, e quando
    # vai desenhar em y, pontos desenhados no mesmo x não é possível.


    # Daqui pra frente são métodos padrões da própria classe do pygame.

    def clear_screen(self):
        self.__screen.fill(self.__background_color.get_rgba())

    @staticmethod
    def update():
        pygame.display.update()


class Color:

    def __init__(self, red, green, blue, alpha=255):
        if -1 < red < 256:
            self.__red = red
        else:
            self.__red = 0
        if -1 < green < 256:
            self.__green = green
        else:
            self.__green = 0
        if -1 < blue < 256:
            self.__blue = blue
        else:
            self.__blue = 0
        if -1 < alpha < 256:
            self.__alpha = alpha
        else:
            self.__alpha = 255

    def get_rgba(self):
        return self.__red, self.__green, self.__blue, self.__alpha
    
    def set_rgba(self, color:tuple):
        red, green, blue, alpha = color
        if -1 < red < 256:
            self.__red = red
        else:
            self.__red = 0
        if -1 < green < 256:
            self.__green = green
        else:
            self.__green = 0
        if -1 < blue < 256:
            self.__blue = blue
        else:
            self.__blue = 0
        if -1 < alpha < 256:
            self.__alpha = alpha
        else:
            self.__alpha = 255