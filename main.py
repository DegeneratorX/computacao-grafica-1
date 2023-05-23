import pygame
from pygame.locals import *
from desenho import *
from poligono import *
from screen import *
from sprite import *
from alfabeto import *

"""
def iterar_lista_poligonos_cortados(desenhar_na_screen, conjunto_poligonos, textura):
    for pol in range(len(conjunto_poligonos)):
        desenhar_na_screen.desenha_poligono(
            conjunto_poligonos[pol].lista_poligono_customizado, Color(0, 0, 0, 0), textura)
"""

def main():

    VIEWPORT = [0, 0, 256, 224]
    janela_x_inicial = 0
    janela_y_inicial = 0
    janela_x_final = 256
    janela_y_final = 224
    janela = [janela_x_inicial, janela_y_inicial,
              janela_x_final, janela_y_final]

    WINDOW_WIDTH = 256
    WINDOW_HEIGHT = 224

    screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
    pygame.display.set_caption("Super Dude World")

    opcoes_menu = ["Jogar", "Sair"]
    opcao_selecionada = 0
    textura = Texture("tile.jpg")
    running = True
    while running:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    opcao_selecionada = (
                        opcao_selecionada - 1) % len(opcoes_menu)
                elif event.key == K_DOWN:
                    opcao_selecionada = (
                        opcao_selecionada + 1) % len(opcoes_menu)
                elif event.key == K_RETURN:
                    if opcao_selecionada == 0:
                        print("Começando o jogo...")

                        player_x = 128
                        player_y = 112
                        player_speed = 5
                        player = Player(player_x, player_y, player_speed)
                        running_game = True
                        while running_game:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    running_game = False

                            keys = pygame.key.get_pressed()
                            janela = player.mover(keys, janela)
                            lista_de_mapeamentos = list()
                            """
                            for i in range(0,1000, 15):
                                for j in range(0, 1000, 15):
                                    bloco = [
                                        [0+i, 0+j, 0, 0],
                                        [15+i, 0+j, 1, 0],
                                        [15+i, 15+j, 1, 1],
                                        [0+i, 15+j, 0, 1],
                                    ]
                                    bloco_mapeado = Projecao(bloco, JANELA, VIEWPORT)
                                    bloco_mapeado.get_poligono_mapeado()
                                    chao_do_jogo.append(bloco_mapeado)
                            """

                            bloco = [
                                [0, 0, 0, 0],
                                [300, 0, 1, 0],
                                [300, 300, 1, 1],
                                [0, 300, 0, 1],
                            ]
                            bloco_mapeado = Projecao(bloco, janela, VIEWPORT)
                            bloco_mapeado.get_poligono_mapeado()
                            lista_de_mapeamentos.append(bloco_mapeado)
                            
                            player_sprite_mapeado = Projecao(player.get_player_sprite(), janela, VIEWPORT)
                            player_sprite_mapeado.get_poligono_mapeado()
                            lista_de_mapeamentos.append(player_sprite_mapeado)

                            viewport_objeto = Viewport(
                                0, 0, 256, 224, lista_de_mapeamentos)
                            viewport_objeto.update_viewport()

                            lista_cores = [
                                Color(255,0,0,0),
                                Color(0,255,0,0),
                                Color(0,0,255,0),
                                Color(255,255,255,0),
                            ]

                            desenhar_na_screen.desenha_poligono(viewport_objeto.get_conjunto_poligonos_cortados(0).lista_poligono_customizado, Color(0, 0, 0, 0), lista_cores)
                            desenhar_na_screen.desenha_poligono(viewport_objeto.get_conjunto_poligonos_cortados(1).lista_poligono_customizado, Color(255, 255, 255), Color(255,255,255,255))
                            #iterar_lista_poligonos_cortados(
                            #    desenhar_na_screen, viewport_objeto.get_conjunto_poligonos_cortados_sem_indice(), textura)

                            #pygame.draw.rect(screen_object.get_screen(), (255, 255, 255), pygame.Rect(
                            #    player_x-8, player_y-8, 16, 16))
                            pygame.display.update()
                            screen_object.get_screen().fill((0, 0, 0))
                            clock.tick(60)

                        pygame.quit()

                    elif opcao_selecionada == 1:
                        print("Saíndo...")
                        running = False

        screen_object.clear_screen()
        desenhar_na_screen = Desenho(screen_object)

        if opcao_selecionada == 0:
            desenhar_na_screen.circunferencia(90, 154, 4, Color(200, 0, 0, 0))
            desenhar_na_screen.flood_fill_iterativo(
                90, 154, Color(255, 58, 58))
        else:
            desenhar_na_screen.circunferencia(90, 170, 4, Color(200, 0, 0, 0))
            desenhar_na_screen.flood_fill_iterativo(
                90, 170, Color(255, 58, 58))

        desenha_titulo(desenhar_na_screen)
        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
