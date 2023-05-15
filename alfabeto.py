class Alfabeto:
    def __init__(self, size) -> None:
        self.__size = size

    def poligonos_palavra(self, origem, palavra:str):
        # Ler a string passada e transformar a palavra em polígonos com suas 
        # respectivas letras
        for i in range(len(palavra)):
            if palavra[i].upper() == "A":
                # desenhar polígono A
                pass