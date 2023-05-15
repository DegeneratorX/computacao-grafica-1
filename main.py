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
        textura = Texture("gato.jpg")
        desenhar_na_screen = Desenho(screen_object)

        quadrado = Poligono().bloco(300, 300, 300)
        triangulo = Poligono().meio_bloco(200, 200, 300)
        cores_triangulo= [
            Color(255, 0, 0, 0),
            Color(0, 255, 0, 0),
            Color(0, 0, 255, 0),
            Color(255, 255, 255, 0)
        ]

        #desenhar_na_screen.desenha_poligono(quadrado, Color(0, 255, 0, 0), cores_triangulo)

        lista_poligono_customizado = [
            [50, 60, 0, 0],
            [150, 40, 1, 0],
            [200, 200, 1, 1],
            [20, 200, 0, 1],
        ]

        lista_poligono_customizado2 = [
            [300, 60, 0, 0],
            [400, 40, 0.5, 0],
            [450, 200, 0.5, 1],
            [270, 200, 0, 1],
        ]


        poligono_custom = Poligono(lista_poligono_customizado)
        desenhar_na_screen.desenha_poligono(
            poligono_custom.lista_poligono_customizado, Color(0, 255, 0, 0), textura)
        desenhar_na_screen.desenha_poligono(lista_poligono_customizado2, Color(0, 255, 0, 0), textura)

        # desenhar_na_screen.desenha_poligono(quadrado, Color(0, 255, 0), cores_triangulo)

        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
