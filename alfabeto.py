from desenho import Desenho
from screen import *

class Alfabeto:
    @staticmethod
    def letra_s(x_origem, y_origem):
        lista_poligono = [
            [x_origem, y_origem, 0, 0],
            [x_origem+16, y_origem, 0, 0],
            [x_origem+16, y_origem+3, 0, 0],
            [x_origem+4, y_origem+3, 0, 0]
        ]
        return lista_poligono
