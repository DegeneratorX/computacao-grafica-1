import pygame
from desenho import *
from poligono import *
from screen import *


def main():

    WINDOW_WIDTH = 60
    WINDOW_HEIGHT = 30

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
        
        poligono_custom = Poligono()
        poligono_custom.insere_ponto(5, 10)
        poligono_custom.insere_ponto(15, 5)
        poligono_custom.insere_ponto(20, 15)
        poligono_custom.insere_ponto(5, 10)

        desenhar_na_screen.desenha_poligono(poligono_custom.lista_poligono_customizado, Color(0, 255, 0), Color(255, 0, 0))

        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
