import pygame
import numpy as np
import math
import time


class Screen:
    # Construtor da classe Screen
    def __init__(self, width, height, background_color):
        self.__screen_matrix = []
        for i in range(height):
            self.__screen_matrix.append([0]*width)
        self.__background_color = background_color
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode(
            (self.__width, self.__height), pygame.RESIZABLE)

    # Método que eu pego a screen para que eu possa fazer alterações nela na main caso eu deseje.

    def get_screen(self):
        return self.__screen

    # Esse método serve para tratar coordenadas que podem ser maiores que o tamanho
    # da matriz. Portanto, em C++, acessaria lixo na mémória. O set_at do python
    # da lib pygame também deve tratar, mas por precaução, estou fazendo aqui
    # também, como forma didática.

    def get_pixel(self, x, y):
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        if x >= self.__screen.get_width():
            x = self.__screen.get_width()-1
        if y >= self.__screen.get_height():
            y = self.__screen.get_height()-1

        return self.__screen.get_at((x, y))

    def set_pixel(self, x, y, color):

        # Se as coordenadas forem negativas, passam a ser no minimo zero.
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        # Truncamento de x e y. Se for maior que o tamanho da matriz, vira as
        # coordenadas do tamanho da matriz.
        if x >= self.__screen.get_width():
            x = self.__screen.get_width()-1
        if y >= self.__screen.get_height():
            y = self.__screen.get_height()-1

        # Setpixel definitivo
        self.__screen.set_at((x, y), color.get_rgba())

    # Desenha uma senóide na matriz. O problema é que ela só itera em x, e quando
    # vai desenhar em y, pontos desenhados no mesmo x não é possível.

    def senoide_com_distorcao(self, color):
        # Para cada x que eu estiver
        for x in range(self.__screen.get_width()):
            # Desenho um y correspondente (Exemplo do que gerará:
            # 50, 51, 52, 51, 50, 49, 48, 49, 50...)
            y = (self.__screen.get_height()/4) + \
                100*np.sin(x*0.05)  # Função seno
            # Para cada y, pode gerar um float. Coverto pra inteiro.
            y = int(y)
            self.set_pixel(x, y, color)

    def senoide_sem_distorcao(self, color):

        # Defino o ponto inicial
        x_anterior = 0
        y_anterior = (self.__screen.get_height()/2) + \
            100*np.sin(x_anterior*0.05)
        y_anterior = int(y_anterior)

        # E para cada x que produzo, seta um pixel em y, e conecto o x anterior e y_anterior ao x atual e y atual.
        for x in range(self.__screen.get_width()):
            y = (self.__screen.get_height()/2) + \
                100*np.sin(x*0.05)  # Função seno
            # Para cada y, pode gerar um float. Coverto pra inteiro.
            y = int(y)
            self.reta_DDA(x_anterior, y_anterior, x, y, color)
            x_anterior = x
            y_anterior = y

    def reta_tradicional(self, x_inicial, y_inicial, x_final, y_final, color):
        delta_x = x_final - x_inicial
        delta_y = y_final - y_inicial

        coeficiente_angular = delta_y/delta_x

        # Se a reta não for de fato variável, é um ponto
        if delta_x == 0 and delta_y == 0:
            self.set_pixel(x_inicial, y_inicial, color)

        # Preciso saber se o ângulo é maior que 45 graus. Se for, troco as
        # variáveis x e y. Obviamente se a altura (y) for maior que a largura (x),
        # trivialmente o ângulo deve ser maior que 45 graus em relação a abscissa.
        trocou = False
        if abs(delta_y) > abs(delta_x):
            delta_x, delta_y = delta_y, delta_x
            trocou = True

        # Caminhho sobre x
        for variacao_em_x in range(delta_x):

            # Delta_y_i = Delta_x_i * a
            variacao_em_y = variacao_em_x * coeficiente_angular

            # Calculo as coordenadas que será setado o pixel
            x = round(x_inicial + variacao_em_x)
            y = round(y_inicial + variacao_em_y)

            # Finalmente coloco.
            if not trocou:
                self.set_pixel(x, y, color)
            else:
                self.set_pixel(y, x, color)

    def reta_DDA(self, x_inicial, y_inicial, x_final, y_final, color, antialiasing=False):
        delta_x = x_final-x_inicial
        delta_y = y_final-y_inicial

        # Defino como passos o percorrimento da variação em x
        passos = abs(delta_x)

        # mas se a variação de y for maior, o percorrimento deve ser em y, parecido com a reta tradicional.
        if abs(delta_y) > abs(delta_x):
            passos = abs(delta_y)
        # pygame.display.update()
        if passos == 0:
            self.set_pixel(x_inicial, y_inicial, color)
            return

        # Quantidade de passos que eu vou dar em x e em y, em porcentagem.
        # Se delta_x > delta_y, então a razão será 1 passo por 1 pixel em x.
        # No caso do y não, será um float, ou seja, uma porcentagem reduzida de passos.
        # Mas se delta_y > delta_x, então a razão será 1 passo por 1 pixel em y.
        passo_x = delta_x/passos
        passo_y = delta_y/passos

        for i in range(passos):

            # Agora para cada passo i, eu multiplico pela % de passo de coordenada
            # para obter quantos pixels em x ou y andou, e depois somo com x_inicial
            # ou y_inicial para obter o segmento de reta
            x = round(x_inicial + i*passo_x)
            y = round(y_inicial + i*passo_y)

            if antialiasing == True:
                red, green, blue, alpha = color.get_rgba()
                if abs(round(passo_x)) == 1:
                    y_decimal = y - np.floor(y)
                    # TODO: Erro ao multiplicar float com classe Color. O que fazer?
                    # Preciso reduzir em % de acordo com a intensidade da cor cada cor para o antiserrilhado.

                    color_serrilhado_1 = Color(round(
                        (1-y_decimal)*red), round((1-y_decimal)*green), round((1-y_decimal)*blue), alpha)
                    color_serrilhado_2 = Color(
                        round((y_decimal)*red), round((y_decimal)*green), round((y_decimal)*blue), alpha)

                    self.set_pixel(int(round(x)), int(
                        np.floor(y)), color_serrilhado_1)
                    self.set_pixel(int(round(x)), int(
                        np.floor(y+1)), color_serrilhado_2)
                else:
                    x_decimal = x - np.floor(x)

                    color_serrilhado_1 = Color(round(
                        (1-x_decimal)*red), round((1-x_decimal)*green), round((1-x_decimal)*blue), alpha)
                    color_serrilhado_2 = Color(
                        round((x_decimal)*red), round((x_decimal)*green), round((x_decimal)*blue), alpha)

                    self.set_pixel(int(np.floor(x)), int(
                        round(y)), color_serrilhado_1)
                    self.set_pixel(int(np.floor(x+1)),
                                   int(round(y)), color_serrilhado_2)

            else:
                self.set_pixel(x, y, color)

    def reta_bresenham(self, x_inicial, y_inicial, x_final, y_final, color):
        delta_x = x_final - x_inicial
        delta_y = y_final - y_inicial

        x = round(x_inicial)
        y = round(y_inicial)

        # Usado pra decrementar se a reta for da direita pra esquerda ou baixo pra cima
        if delta_x < 0:
            fator_multiplicativo_x = -1
        else:
            fator_multiplicativo_x = 1

        if delta_y < 0:
            fator_multiplicativo_y = -1
        else:
            fator_multiplicativo_y = 1

        # Condicional para tratar o caso da reta > 45°
        if abs(delta_x) >= abs(delta_y):

            # P inicial (P0), encontrado no arquivo DESENHOS.md
            p = -abs(delta_x) + (2*abs(delta_y))

            for i in range(round(abs(delta_x))):
                self.set_pixel(round(x), round(y), color)

                # Incremento (ou decremento, depende do fator) em x
                x = x + fator_multiplicativo_x

                # Se a distância d1 for >= d2 (explicado no arquivo DESENHOS.md)
                if p >= 0:
                    # Incremento (ou decremento, depende do fator) em y
                    y = y + fator_multiplicativo_y
                    p = p - (2*abs(delta_x)) + (2*abs(delta_y))
                else:
                    p = p + (2*abs(delta_y))
        else:
            p = -delta_y + (2 * abs(delta_x))

            for i in range(abs(delta_y)):
                self.set_pixel(round(x), round(y), color)

                y = y + fator_multiplicativo_y
                if p >= 0:
                    x = x + fator_multiplicativo_x
                    p = p - (2 * abs(delta_y)) + (2 * abs(delta_x))
                else:
                    p = p + (2 * abs(delta_x))

    def circunferencia(self, x_origem, y_origem, raio, color):
        # 1° Quadrante

        # Procuro guardar o x anterior igual como no alg da senóide. No caso começo o desenho em x_origem+raio.
        x_anterior = x_origem + raio
        y_anterior = y_origem # E começo no y de origem. Ou seja, no primeiro quadrante, é 0° que começo.
        for iterador_em_x in range(raio, -2, -1): # Percorro em x do raio até -2 (-2 é gambiarra pra fechar o circulo), dando passo pra trás (-1)
            x = x_origem + iterador_em_x # E vou percorrendo em x
            y = -np.sqrt(abs(raio**2 - (x - x_origem)**2)) + y_origem # Ao mesmo tempo que produzo um resultado em y
            self.reta_DDA(x_anterior, y_anterior, x, int(y), color) # vou desenhando ponto por ponto no percorrimento
            x_anterior = x # E assim passo o atual para o anterior, e vou desenhadno retas minúsculas aos poucos.
            y_anterior = int(y)

        # 2° Quadrante
        x_anterior = x_origem - raio
        y_anterior = y_origem
        for iterador_em_x in range(raio, -1, -1):
            x = x_origem - iterador_em_x
            y = -np.sqrt(abs(raio**2 - (x - x_origem)**2)) + y_origem
            self.reta_DDA(x_anterior, y_anterior, x, int(y), color)
            x_anterior = x
            y_anterior = int(y)

        # 3° Quadrante
        x_anterior = x_origem - raio
        y_anterior = y_origem
        for iterador_em_x in range(raio, -2, -1):
            x = x_origem - iterador_em_x
            y = +np.sqrt(abs(raio**2 - (x - x_origem)**2)) + y_origem
            self.reta_DDA(x_anterior, y_anterior, x, int(y), color)
            x_anterior = x
            y_anterior = int(y)

        # 4° Quadrante
        x_anterior = x_origem + raio
        y_anterior = y_origem
        for iterador_em_x in range(raio, -1, -1):
            x = x_origem + iterador_em_x
            y = +np.sqrt(abs(raio**2 - (x - x_origem)**2)) + y_origem
            self.reta_DDA(x_anterior, y_anterior, x, int(y), color)
            x_anterior = x
            y_anterior = int(y)

    def elipse(self, x_origem, y_origem, a, b, color):

        x_anterior = x_origem + b
        y_anterior = y_origem
        for iterador_em_x in range(b, -2, -1):
            x = x_origem + iterador_em_x
            y = -np.sqrt(abs((b**2*(a-(x - x_origem))*(a+(x - x_origem)))/a**2)) + y_origem
            self.reta_DDA(x_anterior, y_anterior, x, int(y), color)
            x_anterior = x
            y_anterior = int(y)


    # Uso não recomendado/depreciado (causa estouro na call stack dependendo do tamanho do preenchimento)
    def flood_fill_recursivo(self, x_setar, y_setar, cor_nova, cor_inicial, primeira_vez_executando = True):
        if self.get_pixel(x_setar, y_setar) == cor_nova:
            if primeira_vez_executando:
                self.set_pixel(x_setar, y_setar, cor_nova)
            return

        self.set_pixel(x_setar, y_setar, cor_nova)
        self.flood_fill_recursivo(x_setar, y_setar-1, cor_nova, cor_inicial, False)
        self.flood_fill_recursivo(x_setar+1, y_setar, cor_nova, cor_inicial, False)
        self.flood_fill_recursivo(x_setar, y_setar+1, cor_nova, cor_inicial, False)
        self.flood_fill_recursivo(x_setar-1, y_setar, cor_nova, cor_inicial, False)


    # Dados guardados na heap. É o indicado para uso.
    def flood_fill_iterativo(self, x_setar, y_setar, cor_nova):

        # Capturo a cor que cliquei
        cor_inicial = self.get_pixel(x_setar, y_setar)
        if cor_inicial == cor_nova: # Se for a mesma cor que quero colocar, faz nada.
            self.set_pixel(x_setar, y_setar, cor_nova)
            return

        pilha = [(x_setar, y_setar)]
        while pilha:
            x, y = pilha.pop()
            if self.get_pixel(x, y) != cor_inicial: # Se a cor detectada do próximo da pilha for diferente, para o preenchimento.
                continue
            # Se não, preenche com pixel
            self.set_pixel(x, y, cor_nova)

            # Verifico pra onde vai os próximos pixels, esquerda, direita, cima e baixo.
            if y > 0:
                pilha.append((x, y-1))
            if x < self.__screen.get_width():
                pilha.append((x+1, y))
            if y < self.__screen.get_height():
                pilha.append((x, y+1))
            if x > 0:
                pilha.append((x-1, y))
            if x == 0:
                pilha.append((x, y))
            if y == 0:
                pilha.append((x, y))

    # Daqui pra frente são métodos padrões da própria classe do pygame.

    def clear_screen(self):
        self.__screen.fill(self.__background_color.get_rgba())

    def update(self):
        pygame.display.update()


class Color:

    def __init__(self, red, green, blue, alpha=255):
        if (-1 < red < 256):
            self.__red = red
        else:
            self.__red = 0
        if (-1 < green < 256):
            self.__green = green
        else:
            self.__green = 0
        if (-1 < blue < 256):
            self.__blue = blue
        else:
            self.__blue = 0
        if (-1 < alpha < 256):
            self.__alpha = alpha
        else:
            self.__alpha = 255

    def get_rgba(self):
        return (self.__red, self.__green, self.__blue, self.__alpha)


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
    # screen_object.set_pixel(50, 100, Color(255, 0, 0, 50))
    # screen_object.senoide_sem_distorcao(Color(255, 0, 0, 50))
    # screen_object.senoide_com_distorcao(Color(255, 0, 0, 50))
    # screen_object.reta_tradicional(20, 200, 100, 170, Color(255, 0, 0, 50))
    # screen_object.reta_DDA(20, 200, 100, 170, Color(255, 0, 0, 50), True)
    # screen_object.reta_bresenham(20, 200, 100, 170, Color(255, 0, 0, 50))
    screen_object.set_pixel(600,325,Color(255,255,0))
    #screen_object.circunferencia(400, 325, 50, Color(255, 0, 0, 50))
    screen_object.elipse(600, 325, 50, 40, Color(255, 0, 0, 50))
    #screen_object.flood_fill_iterativo(600, 325, Color(255, 0, 255, 50))
    screen_object.update()
    clock.tick(60)
