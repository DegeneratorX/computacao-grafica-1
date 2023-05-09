import pygame
from desenho import *
from poligono import *

def main():

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 650

    screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
    screen = screen_object.get_screen()
    while True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        screen_object.clear_screen()
        # screen_object.set_pixel(50, 100, Color(255, 0, 0, 50))
        # screen_object.senoide_sem_distorcao(Color(255, 0, 0, 50))
        # screen_object.senoide_com_distorcao(Color(255, 0, 0, 50))
        # screen_object.reta_tradicional(20, 200, 100, 170, Color(255, 0, 0, 50))
        screen_object.reta_DDA(20, 200, 100, 170, Color(255, 0, 0, 0), True)
        # screen_object.reta_bresenham(20, 200, 100, 170, Color(255, 0, 0, 50))
        # screen_object.set_pixel(600, 325, Color(255, 255, 0))
        # screen_object.circunferencia(400, 325, 50, Color(255, 0, 0, 50))
        # screen_object.elipse(600, 325, 100, 200, Color(255, 0, 0, 50))
        # screen_object.flood_fill_iterativo(600, 325, Color(255, 0, 255, 50))
        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
