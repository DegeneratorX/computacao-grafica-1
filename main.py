import pygame
from desenho import *
from poligono import *
from screen import *
from sprite import *
from alfabeto import *


def main():

    VIEWPORT = [0, 0, 800, 600]
    JANELA = [0, 0, 800, 600]

    WINDOW_WIDTH = 256
    WINDOW_HEIGHT = 224

    screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
    pygame.display.set_caption("Super Dude World")

    # player = Player()
    # conjunto_sprites = pygame.sprite.Group()
    # conjunto_sprites.add(player)

    while True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen_object.clear_screen()
        desenhar_na_screen = Desenho(screen_object)

        textura = Texture("gato.jpg")
        font_tiles = Texture("font.png")

        desenha_titulo(desenhar_na_screen)
        #bloco_mapeado = Projecao(retangulo, [0, 0, 100, 100], [100, 100, 300, 300])
        #desenhar_na_screen.desenha_poligono(bloco_mapeado.get_poligono_mapeado(), Color(0,0,0,0), textura)
        #viewport_objeto = Viewport(100, 100, 300, 300, [bloco_mapeado])
        #viewport_objeto.update_viewport()
        #desenhar_na_screen.desenha_poligono(
        #    viewport_objeto.get_conjunto_poligonos_cortados(0).lista_poligono_customizado, Color(0, 0, 0, 0), textura)

        screen_object.update()
        clock.tick(60)


def lista_poligonos_separar(lista_poligono):
    lista_vertices = [(linha[0], linha[1]) for linha in lista_poligono]
    lista_texturas = [(linha[2], linha[3]) for linha in lista_poligono]

    return lista_vertices, lista_texturas

def coordenadas_viewport(viewport):
    x_inicial = viewport[0]
    y_inicial = viewport[1]
    largura_viewport = viewport[2]-viewport[0]
    altura_viewport  = viewport[3]-viewport[1]

    return x_inicial, y_inicial, largura_viewport, altura_viewport

def converter_obj_cores_em_tuplas(lista_cores):
    tupla_de_cores = []
    for i in range(len(lista_cores)):
        tupla_de_cores.append(lista_cores[i].get_rgba())
    return tupla_de_cores

if __name__ == '__main__':
    main()