# Representação de Objetos

Representamos objetos tridimensionais através de:

- Lista de vértices
- Lista de arestas
- Lista de faces

Podemos subdividir praticamente qualquer objeto tridimensional ou bidimensional em faces triangulares.

Triângulos nunca podem ser não-planares. Ou seja, todo triângulo é obrigatoriamente plano. A partir de um quadrilátero, o objeto pode não ser plano, e isso leva a cálculos mais complexos para renderizar algum modelo tridimensional, pois levaria em consideração a sua curvatura. Quadriláteros são utilizados para modelar rostos.

Por hora irei trabalhar apenas com triângulos.

O triângulo é eficiente em memória e processamento, pois o mínimo de pontos para se definir uma superfície plana são 3, e portanto qualquer forma pode ser simulada através de triângulos.

O processo de conversão de faces não triangulares para triangulares é chamado de **triangulação**. Existem diversos algoritmos eficientes que buscam triangular superfícies de forma automática.

Veja esse cubo por exemplo. As duas figuras mostram ele opaco e transparente para melhor visualização. As linhas laranjas representam a triangulação. A escolha para formar as arestas de triangulação (linhas laranja) são normalmente aleatórias.

- COLOCAR IMAGEM

- Essas são as coordenadas dos vértices (observe o cartesiano 3D).

| Lista de Vértices  | X | Y | Z |
| ------------- | --- | --- | --- |
| ID: 0 | 0 | 0 | 0 |
| ID: 1 | 0 | 0 | 2 |
| ID: 2 | 2 | 0 | 2 |
| ID: 3 | 2 | 0 | 0 |
| ID: 4 | 0 | 2 | 0 |
| ID: 5 | 0 | 2 | 2 |
| ID: 6 | 2 | 2 | 2 |
| ID: 7 | 2 | 2 | 0 |

- Essas são as listas das arestas (não preciso enumerar na imagem, basta fazer uma contagem de todas).
> Nota: para contabilizar arestas, basta eu pegar o início e fim dos vértices que formam ela. O início e fim são escolhidos aleatoriamente. Por convenção e organização, o interessante é contar por faces.

| Lista de Arestas  | Vértice Inicial | Vértice Final |
| ------------- | --- | --- |
| ID: 0 | 0 | 1 |
| ID: 1 | 1 | 2 |
| ID: 2 | 2 | 3 |
| ID: 3 | 3 | 0 |
| ID: 4 | 4 | 5 |
| ID: 5 | 5 | 6 |
| ID: 6 | 6 | 7 |
| ID: 7 | 7 | 4 |
| ID: 8 | 0 | 4 |
| ID: 9 | 1 | 5 |
| ID: 10 | 2 | 6 |
| ID: 11 | 3 | 7 |
| ID: 12 | 2 | 7 |
| ID: 13 | 5 | 7 |
| ID: 14 | 5 | 2 |
| ID: 15 | 1 | 4 |
| ID: 16 | 1 | 3 |
| ID: 17 | 3 | 4 |

- Por fim, as faces.
> Nota: as arestas são contabilizadas no sentido anti-horário.

| Lista de Faces  | Aresta 1 | Aresta 2 | Aresta 3 |
| ------------- | --- | --- | --- |
| ID: 0 | 6 | 10 | 12 |
| ID: 1 | 12 | 2 | 11 |
| ID: 2 | 7 | 4 | 13 |
| ID: 3 | 13 | 5 | 6 |
| ID: 4 | 5 | 14 | 10 |
| ID: 5 | 9 | 1 | 14 |
| ID: 6 | 4 | 15 | 9 |
| ID: 7 | 8 | 0 | 15 |
| ID: 8 | 1 | 16 | 2 |
| ID: 9 | 3 | 16 | 10 |
| ID: 10 | 11 | 17 | 7 |
| ID: 11 | 3 | 8 | 17 |


# Curvas Paramétricas

As **curvas paramétricas** são curvas originadas quando se tem um input para uma função, e resulta em 2 ou mais outputs. 

No caso de uma curva bidimensional, inserir um valor em uma função produz uma coordenada X e uma coordenada Y, e diferentes valores podem gerar diferentes coordenadas, de tal forma que ao ligar todos os pontos, pode produzir um gráfico não linear (curva).

Exemplo: x = 2t e y = t² - 1. Para t = 1, produz x = 2 e y = 0.

## Curvas de Bézier Cúbicas

As **curvas de Bézier Cúbicas** são necessárias para produzir desenhos em 3D. Seguem a seguinte função:

$a+bt+ct^{2}+dt^{3}$

### Condições de contorno