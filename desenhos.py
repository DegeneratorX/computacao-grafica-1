import pygame
import numpy
import time

class Screen:
    def __init__(self, width, height, background_color):
        self.__screen = pygame.display.set_mode((width, height),pygame.HWSURFACE | pygame.DOUBLEBUF)
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
        self.__screen.set_at((x,y),color.get_rgba())

        #self.__screen.set_at((x,y),color.get_rgba())
    
    def senoide(self):
        for x in range(self.__screen.get_width()-1):
            y = (self.__screen.get_height()/2)+5*numpy.sin(x*0.2)
            y = int(y)
            self.set_pixel(x, y, Color(255,255,255))

    def clear_screen(self):
        self.__screen.fill(self.__background_color.get_rgba())
        
    def update(self):
        pygame.display.update()


class Color:
    def __init__(self, red, green, blue, alpha = 0):
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__alpha = alpha

    def get_rgba(self):
        return (self.__red, self.__green, self.__blue, self.__alpha)


largura, altura, background_color = 200, 200, Color(0,0,0)

while True:
    pygame.init()
    screen = Screen(largura, altura, background_color)
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        
    screen.set_pixel(50, 50, Color(255, 255, 0))
    screen.senoide()

    screen.update()
    clock.tick(30)
