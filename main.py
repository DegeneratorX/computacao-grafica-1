import pygame
from pygame.locals import *
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

    opcoes_menu = ["Jogar", "Sair"]
    opcao_selecionada = 0

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

        textura = Texture("gato.jpg")
        font_tiles = Texture("font.png")

        desenha_titulo(desenhar_na_screen)

        screen_object.update()
        clock.tick(60)

def começar_jogo():
    player_x = 400
    player_y = 300
    player_speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            player_x -= player_speed
        if keys[K_RIGHT]:
            player_x += player_speed
        if keys[K_UP]:
            player_y -= player_speed
        if keys[K_DOWN]:
            player_y += player_speed

        screen.fill((0, 0, 0))  # Clear the screen
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(player_x, player_y, 50, 50))  # Draw the player rectangle

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS

    pygame.quit()

if __name__ == '__main__':
    main()