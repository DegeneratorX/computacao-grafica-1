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

    # Acúmulo = matriz que acumula transformações sucessivas em uma identidade (inicialmente) para depois ser aplicada
    # ao polígono.
    @staticmethod
    def mover_poligono(translacao_x, translacao_y, acumulo=[[1,0,0],[0,1,0],[0,0,1]]):
        return multiplicacao_matrizes([
            [1, 0, translacao_x],
            [0, 1, translacao_y],
            [0, 0 ,           1]
        ], acumulo)
    
    @staticmethod
    def redimensionar_poligono(escala_x, escala_y, acumulo=[[1,0,0],[0,1,0],[0,0,1]]):
        return multiplicacao_matrizes([
            [escala_x, 0, 0],
            [0, escala_y, 0],
            [0, 0,        1]
        ], acumulo)
    
    @staticmethod
    def rotacionar_poligono(angulo, acumulo=[[1,0,0],[0,1,0],[0,0,1]]):
        angulo = angulo*np.pi/180
        return multiplicacao_matrizes([
            [np.cos(angulo), -np.sin(angulo), 0],
            [np.sin(angulo), np.cos(angulo),  0],
            [0, 0,                            1]
        ], acumulo)
    
    """
    # TODO: Erro aqui
    def aplicar_transformacao_com_acumulos(self, acumulo):
        num_colunas = len(self.__lista_poligono_customizado[0])
        for i in range(len(self.__lista_poligono_customizado)):
            ponto_poligono = [self.__lista_poligono_customizado[i][0], self.__lista_poligono_customizado[i][1], 1]
            ponto_poligono = transposta(ponto_poligono)
            
            ponto_poligono = [[0] * num_colunas for _ in range(1)]
            for j in range(num_colunas):
                for k in range(3):
                    ponto_poligono[0][j] += acumulo[k][j] * self.__lista_poligono_customizado[i][k]
            
            ponto_poligono = transposta(ponto_poligono)
            self.__lista_poligono_customizado[i][0], self.__lista_poligono_customizado[i][1] = ponto_poligono[0][0], ponto_poligono[1][0]
    """
    def aplicar_transformacao_com_acumulos(self, acumulo):
        self.__lista_poligono_customizado = np.array(self.__lista_poligono_customizado)
        
        for i in range(self.__lista_poligono_customizado.shape[0]):
            ponto_poligono = np.concatenate((self.__lista_poligono_customizado[i, :2], [1]))
            ponto_poligono = np.transpose(ponto_poligono)
            
            ponto_poligono = np.dot(acumulo, ponto_poligono)
            
            ponto_poligono = np.transpose(ponto_poligono)
            self.__lista_poligono_customizado[i, :2] = ponto_poligono[:2]
        
        return self.__lista_poligono_customizado.tolist()


def transposta(matriz):
    if isinstance(matriz[0], int) or len(matriz) == 1:
        return matriz
    
    linhas = len(matriz)
    colunas = len(matriz[0])

    transposta = [[0 for _ in range(linhas)] for _ in range(colunas)]
    
    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = matriz[i][j]
    
    return transposta

def multiplicacao_matrizes(matriz_1, matriz_2):
    linha_1, coluna_1 = len(matriz_1), len(matriz_1[0])
    linha_2, coluna_2 = len(matriz_2), len(matriz_2[0])
    
    if coluna_1 != linha_2:
        raise ValueError("O número de colunas da matriz 1 deve ser o mesmo do número de linhas da matriz 2")
    
    resultado = [[0] * coluna_2 for _ in range(linha_1)]
    
    for i in range(linha_1):
        for j in range(coluna_2):
            for k in range(coluna_1):
                resultado[i][j] += matriz_1[i][k] * matriz_2[k][j]
    
    return resultado