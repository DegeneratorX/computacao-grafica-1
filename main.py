import pygame
from pygame.locals import *
from desenho import *
from poligono import *
from screen import *
from sprite import *
from alfabeto import *

def iterar_lista_poligonos_cortados(desenhar_na_screen, conjunto_poligonos, textura):
    for pol in range(len(conjunto_poligonos)):
        desenhar_na_screen.desenha_poligono(conjunto_poligonos[pol].lista_poligono_customizado, Color(0, 0, 0, 0), textura)


def main():

    VIEWPORT = [0, 0, 256, 224]
    JANELA = [0, 0, 150, 150]

    WINDOW_WIDTH = 256
    WINDOW_HEIGHT = 224

    screen_object = Screen(WINDOW_WIDTH, WINDOW_HEIGHT, Color(255, 255, 255))
    pygame.display.set_caption("Super Dude World")

    opcoes_menu = ["Jogar", "Sair"]
    opcao_selecionada = 0
    textura = Texture("tile.jpg")
    running = True
    jogo = True
    while running:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    opcao_selecionada = (opcao_selecionada - 1) % len(opcoes_menu)  # Move up through the options
                elif event.key == K_DOWN:
                    opcao_selecionada = (opcao_selecionada + 1) % len(opcoes_menu)  # Move down through the options
                elif event.key == K_RETURN:
                    if opcao_selecionada == 0:
                        print("Começando o jogo...")

                        player_x = 10
                        player_y = 10
                        player_speed = 5

                        running_game = True
                        while running_game:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    running_game = False

                            keys = pygame.key.get_pressed()
                            if keys[K_LEFT]:
                                player_x -= player_speed
                            if keys[K_RIGHT]:
                                player_x += player_speed
                            if keys[K_UP]:
                                player_y -= player_speed
                            if keys[K_DOWN]:
                                player_y += player_speed
                
                            chao_do_jogo = list()
                            for i in range(0,1000, 15):
                                bloco = [
                                    [0+i, 0, 0, 0],
                                    [15+i, 0, 1, 0],
                                    [15+i, 15, 1, 1],
                                    [0+i, 15, 0, 1],
                                ]
                                bloco_mapeado = Projecao(bloco, JANELA, VIEWPORT)
                                bloco_mapeado.get_poligono_mapeado()
                                chao_do_jogo.append(bloco_mapeado)

                            viewport_objeto = Viewport(0, 0, 256, 224, chao_do_jogo)
                            viewport_objeto.update_viewport()

                            iterar_lista_poligonos_cortados(desenhar_na_screen,viewport_objeto.get_conjunto_poligonos_cortados_sem_indice(), textura)

                            pygame.draw.rect(screen_object.get_screen(), (255, 255, 255), pygame.Rect(player_x, player_y, 50, 50))
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
            desenhar_na_screen.circunferencia(90, 154, 4, Color(200, 0,0,0))
            desenhar_na_screen.flood_fill_iterativo(90, 154, Color(255,58,58))
        else:
            desenhar_na_screen.circunferencia(90, 170, 4, Color(200, 0,0,0))
            desenhar_na_screen.flood_fill_iterativo(90, 170, Color(255,58,58))


        font_tiles = Texture("font.png")
        desenha_titulo(desenhar_na_screen)

        screen_object.update()
        clock.tick(60)


if __name__ == '__main__':
    main()