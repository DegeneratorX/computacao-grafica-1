import pygame
from desenho import *
from poligono import *
from screen import *


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
        desenhar_na_screen = Desenho(screen_object)
        bloco = Poligono.bloco(200, 200, 16)
        desenhar_na_screen.desenha_poligono(bloco, Color(255, 0, 0))
        lista_poligono_custom = []
        Poligono.insere_ponto(poligono_custom, 100, 400)
        Poligono.insere_ponto(poligono_custom, 300, 250)
        Poligono.insere_ponto(poligono_custom, 300, 500)
        Poligono.insere_ponto(poligono_custom, 100, 400)
        poligono_custom = Poligono(desenhar_na_screen, lista_poligono_custom, Color(0, 255,0))

        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
