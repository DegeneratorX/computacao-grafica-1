from desenho import Desenho
from screen import Color
import numpy as np

class Poligono(Desenho):
    def __init__(self, lista_poligono, color):
        self.__lista_poligono = lista_poligono
        self.desenhapoligono(color)

    @staticmethod
    def insere_ponto(poligono, x, y):
        poligono.append([x, y])
    
    def desenhapoligono(self, color):
        x = self.__lista_poligono[0][0]
        y = self.__lista_poligono[0][1]
        for i in range(1, len(self.__lista_poligono)):
            self.reta_DDA(x, y, self.__lista_poligono[i][0], self.__lista_poligono[i][1], color)
            x = self.__lista_poligono[i][1]
            y = self.__lista_poligono[i][2]
        self.reta_DDA(x, y, self.__lista_poligono[0][0], self.__lista_poligono[0][1], color)

    # Quadrado
    @staticmethod
    def bloco(origem, lado, color):
        pol = [
            [origem-lado/2, origem+lado/2],
            [origem+lado/2, origem+lado/2],
            [origem+lado/2, origem-lado/2],
            [origem-lado/2, origem-lado/2],
        ]
        return Poligono(pol, color)

    # Triângulo retângulo metade de um quadrado
    @staticmethod
    def meio_bloco(origem, lado, color):

        pol = [
            [origem-lado/2, origem+lado/2],
            [origem+lado/2, origem-lado/2],
            [origem-lado/2, origem-lado/2],
        ]
        return Poligono(pol, color)

    @staticmethod
    def retangulo(origem, base, altura, color):
        pol = [
            [origem-base/2, origem+altura/2],
            [origem+base/2, origem+altura/2],
            [origem+base/2, origem-altura/2],
            [origem-base/2, origem-altura/2],
        ]
        return Poligono(pol, color)

    @staticmethod
    def trapezio_simetrico(origem, base_maior, base_menor, altura, color):
        pol = [
            [origem-base_menor/2, origem+altura/2],
            [origem+base_menor/2, origem+altura/2],
            [origem+base_maior/2, origem-altura/2],
            [origem-base_maior/2, origem-altura/2],
        ]
        return Poligono(pol, color)

    @staticmethod
    def triangulo_equilatero(origem, lado, color):
        altura = (np.sqrt(3)/2)*lado
        pol = [
            [origem-lado/2, origem+altura/2],
            [origem+lado/2, origem+altura/2],
            [origem+lado/2, origem-altura/2],
            [origem-lado/2, origem-altura/2],
        ]
        return Poligono(pol, color)

    def losango(origem, lado, color):
        pass
    
    # TODO
    @staticmethod
    def pentagono_equilatero(origem, lado, color):
        base = lado * np.sqrt(5-2*np.sqrt(5))/2
        pol = [
            [origem-lado/2, origem+altura/2],
            [origem+lado/2, origem+altura/2],
            [origem+lado/2, origem-altura/2],
            [origem-lado/2, origem-altura/2],
        ]
    
    # TODO
    @staticmethod
    def hexagono_equilatero(origem, lado, color):
        pass
