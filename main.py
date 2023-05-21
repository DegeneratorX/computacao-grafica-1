import pygame
from desenho import *
from poligono import *
from screen import *
from sprite import *


def main():

    VIEWPORT = [0, 0, 800, 600]
    JANELA = [0, 0, 800, 600]
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
    pygame.display.set_caption("Super Dude World")

    player = Player()
    conjunto_sprites = pygame.sprite.Group()
    conjunto_sprites.add(player)
    
    while True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen_object.clear_screen()
        desenhar_na_screen = Desenho(screen_object)

        textura = Texture("gato.jpg")

        trapezio = [
            [50, 60, 0, 0],
            [150, 40, 1, 0],
            [200, 200, 1, 1],
            [20, 200, 0, 1],
        ]

        trapezio_projetado = Projecao(trapezio, JANELA, VIEWPORT)

        desenhar_na_screen.desenha_poligono(trapezio_projetado.get_poligono_mapeado(), Color(0, 0, 0, 0), textura)

        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
