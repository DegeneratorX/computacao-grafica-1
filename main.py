import pygame
from desenho import *
from poligono import *
from screen import *


def main():

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
    screen = screen_object.get_screen()
    textura_gato = Texture("gato.jpg")

    while True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        screen_object.clear_screen()
        desenhar_na_screen = Desenho(screen_object)

        triangulo = Poligono().bloco(200, 200, 300)
        cores_triangulo = [
            Color(255, 0, 0, 0),
            Color(0, 255, 0, 0),
            Color(0, 0, 255, 0),
            Color(255, 255, 255, 0)
        ]
        desenhar_na_screen.desenha_poligono(triangulo, Color(0, 255, 0), cores_triangulo)

        textura = Texture("gato.jpg")
        pixel = textura.get_pixel_texture(1, 0)
        print(pixel)

        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
