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
    animacao_rotacao = 0
    animacao_rotacao_degrade = 0
    while True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        screen_object.clear_screen()
        textura = Texture("gato.jpg")
        desenhar_na_screen = Desenho(screen_object)

        quadrado = Poligono().bloco(350, 350, 100)
        triangulo = Poligono().meio_bloco(200, 200, 300)
        cores_bloco = [
            Color(255, 0, 0, 0),
            Color(0, 255, 0, 0),
            Color(0, 0, 255, 0),
            Color(255, 255, 255, 0)
        ]

        # desenhar_na_screen.desenha_poligono(quadrado, Color(0, 255, 0, 0), cores_triangulo)

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

        transformacao_bloco = Poligono.mover_poligono(-350, -350)
        transformacao_bloco = Poligono.rotacionar_poligono(
            animacao_rotacao_degrade, transformacao_bloco)
        transformacao_bloco = Poligono.mover_poligono(350, 350, transformacao_bloco)
        animacao_rotacao_degrade += 1

        bloco = Poligono(quadrado)
        poligono_custom = Poligono(lista_poligono_customizado)

        transformacao = Poligono.rotacionar_poligono(animacao_rotacao)
        animacao_rotacao += 1
        transformacao = Poligono.mover_poligono(300, 300, transformacao)
        transformacao = Poligono.redimensionar_poligono(
            0.4, 0.4, transformacao)
        poligono_custom.aplicar_transformacao_com_acumulos(transformacao)

        bloco.aplicar_transformacao_com_acumulos(transformacao_bloco)

        desenhar_na_screen.desenha_poligono(
            poligono_custom.lista_poligono_customizado, Color(0, 255, 0, 0), textura)
        # desenhar_na_screen.desenha_poligono(lista_poligono_customizado2, Color(0, 255, 0, 0), textura)
        desenhar_na_screen.desenha_poligono(
            bloco.lista_poligono_customizado, Color(255, 255, 255, 0), cores_bloco)
        # desenhar_na_screen.desenha_poligono(quadrado, Color(0, 255, 0), cores_triangulo)
        if animacao_rotacao > 359:
            animacao_rotacao = 0
        if animacao_rotacao_degrade > 359:
            animacao_rotacao_degrade = 0
        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
