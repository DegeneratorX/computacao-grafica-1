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
                [origem_x-metade_lado, origem_y-metade_lado, 0, 0],
                [origem_x+metade_lado-1, origem_y-metade_lado, 1, 0],
                [origem_x+metade_lado-1, origem_y+metade_lado-1, 1, 1],
                [origem_x-metade_lado, origem_y+metade_lado-1, 0, 1],
            ]
        else:
            lista_poligono = [
                [origem_x-metade_lado, origem_y-metade_lado, 0, 0],
                [origem_x+metade_lado, origem_y-metade_lado, 1, 0],
                [origem_x+metade_lado, origem_y+metade_lado, 1, 1],
                [origem_x-metade_lado, origem_y+metade_lado, 0, 1],
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

    def mover_poligono(self, translacao_x, translacao_y):
        translacao_matriz = list()

        for _ in range(len(self.__lista_poligono_customizado)):
            translacao_matriz.append(np.array([translacao_x, translacao_y]))

        if not isinstance(self.__lista_poligono_customizado, np.ndarray):
            self.__lista_poligono_customizado = np.array(self.__lista_poligono_customizado)

        self.__lista_poligono_customizado[:, 0:2] = self.__lista_poligono_customizado[:, 0:2] + np.array(translacao_matriz)

        return self.__lista_poligono_customizado
    
    def redimensionar_poligono(self, escala_x, escala_y):
        escala_matriz = list()
        for _ in range(len(self.__lista_poligono_customizado)):
            escala_matriz.append(np.array([escala_x, escala_y]))

        if not isinstance(self.__lista_poligono_customizado, np.ndarray):
            self.__lista_poligono_customizado = np.array(self.__lista_poligono_customizado)

        self.__lista_poligono_customizado[:, 0:2] = self.__lista_poligono_customizado[:, 0:2] * np.array(escala_matriz)

        return self.__lista_poligono_customizado


    @staticmethod
    def mover_poligono(lista_poligono, translacao_x, translacao_y):
        
        translacao_matriz = list()

        for _ in range(len(lista_poligono)):
            translacao_matriz.append(np.array([translacao_x, translacao_y]))

        if not isinstance(lista_poligono, np.ndarray):
            lista_poligono = np.array(lista_poligono)

        lista_poligono[:, 0:2] = lista_poligono[:, 0:2] + np.array(translacao_matriz)

        return lista_poligono

    
