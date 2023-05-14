import numpy as np

class Poligono:
    def __init__(self, lista_poligono_customizado=None):
        if lista_poligono_customizado is None:
            lista_poligono_customizado = []
        self.__lista_poligono_customizado = lista_poligono_customizado

    @property
    def lista_poligono_customizado(self):
        return self.__lista_poligono_customizado

    def insere_ponto(self, x, y):
        self.__lista_poligono_customizado.append([x, y])

    # Quadrado
    @staticmethod
    def bloco(origem_x, origem_y, lado):
        metade_lado = int(round(lado/2))
        if lado%2 == 0:
            lista_poligono = [
                [origem_x-metade_lado, origem_y-metade_lado],
                [origem_x+metade_lado-1, origem_y-metade_lado],
                [origem_x+metade_lado-1, origem_y+metade_lado-1],
                [origem_x-metade_lado, origem_y+metade_lado-1],
            ]
        else:
            lista_poligono = [
                [origem_x-metade_lado, origem_y-metade_lado],
                [origem_x+metade_lado, origem_y-metade_lado],
                [origem_x+metade_lado, origem_y+metade_lado],
                [origem_x-metade_lado, origem_y+metade_lado],
            ]
        return lista_poligono

    # Triângulo retângulo metade de um quadrado
    @staticmethod
    def meio_bloco(origem_x, origem_y, lado):
        metade_lado = int(round(lado/2))
        if lado%2==0:
            lista_poligono = [
                [origem_x-metade_lado, origem_y+metade_lado-1],
                [origem_x+metade_lado-1, origem_y-metade_lado],
                [origem_x+metade_lado-1, origem_y+metade_lado-1],
            ]
        else:
            lista_poligono = [
                [origem_x-metade_lado, origem_y+metade_lado],
                [origem_x+metade_lado, origem_y-metade_lado],
                [origem_x+metade_lado, origem_y+metade_lado],
            ]
        return lista_poligono

    @staticmethod
    def retangulo(origem, base, altura):
        lista_poligono = [
            [origem-base/2, origem+altura/2],
            [origem+base/2, origem+altura/2],
            [origem+base/2, origem-altura/2],
            [origem-base/2, origem-altura/2],
        ]
        return lista_poligono

    @staticmethod
    def trapezio_simetrico(origem, base_maior, base_menor, altura):
        lista_poligono = [
            [origem-base_menor/2, origem+altura/2],
            [origem+base_menor/2, origem+altura/2],
            [origem+base_maior/2, origem-altura/2],
            [origem-base_maior/2, origem-altura/2],
        ]
        return lista_poligono

    @staticmethod
    def triangulo_equilatero(origem, lado):
        altura = (np.sqrt(3)/2)*lado
        lista_poligono = [
            [origem-lado/2, origem+altura/2],
            [origem+lado/2, origem+altura/2],
            [origem+lado/2, origem-altura/2],
            [origem-lado/2, origem-altura/2],
        ]
        return lista_poligono

    def losango(origem, lado):
        pass
    
    # TODO
    @staticmethod
    def pentagono_equilatero(origem, lado):
        base = lado * np.sqrt(5-2*np.sqrt(5))/2
        pol = [
            [origem-lado/2, origem+altura/2],
            [origem+lado/2, origem+altura/2],
            [origem+lado/2, origem-altura/2],
            [origem-lado/2, origem-altura/2],
        ]
    
    # TODO
    @staticmethod
    def hexagono_equilatero(origem, lado):
        pass
