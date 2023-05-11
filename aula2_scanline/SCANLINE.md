# Scanline - Introdução

O algoritmo de scanline é um algoritmo que propõe ser muito mais eficiente que o flood fill para pintar polígonos. Basicamente ele varre linha por linha e sai pintando um polígono, sabendo as coordenadas do polígono. O flood fill é bom quando não temos informações de borda, pois ele sai pintando até encontrar alguma borda por conta própria. Sabendo das informações da borda de um polígono, não há motivos para usar flood fill, pois só é aumento de custo computacional para verificações. Usamos o scanline.

Sabendo a coordenada em y, ele varre x e pinta em retas, utilizando-se de apenas um laço e evitando comparar se o pixel já foi pintado e evitar o uso de desempilhamento e empilhamento.

O algoritmo de scanline é o algoritmo utilizado para pintar a maioria dos polígonos no computador, inclusive de projeções 2D a partir de mundos 3D (jogos). Portanto, para geração de imagens, o scanline é amplamente utilizado e definitivo. O flood fill serve mais para processamento de imagens ou edição em editores de imagens.

# Interseção

Antes de entrar na parte de Scanline, precisamos entender como funciona a interseção de uma reta com outra. Afinal, quando o scanline traça as retas, ela precisa interseccionar com a reta do polígono para saber onde ele deve pintar e onde ele deve parar.

Adotamos então um parâmetro $t$, que é basicamente uma porcentagem que um determinado ponto está no segmento de reta.

![](2023-05-10-21-04-25.png)

## Equação Paramétrica da Reta

A equação paramétrica da reta é basicamente uma função que te retorna um ponto $(x, y)$ ao passar o parâmetro t.

Para isso, baseado na figura anterior, precisamos descobrir para cada reta qual sua equação $P(t)$:

![](2023-05-10-22-28-42.png)

Esse chute de equação inicial é o que precisamos para achar que se $t = 1$, implica achar o ponto final do segmento, e se $t = 0$, implica achar o ponto inicial do segmento. Portanto, podemos trabalhar com porcentagens a partir disso.

Agora suponha uma inserseção:

![](2023-05-11-13-43-10.png)

Perceba que eu tenho todos os valores de y, que é a reta da scanline, pois eu sei a altura que ela está iterando na tela. Ou seja, para toda reta da scanline, eu sei o ponto y que intersecta com a reta do polígono. Ou seja, eu preciso descobrir $\forall y$, um $x \in (x, y)$, onde y é um valor que já sei.

Agora vamos para os casos de exceção:

![](2023-05-11-18-24-25.png)

Veja, um problema ocorre ao interseccionar a scanline sobre um vértice. Se o ponto final de uma reta coincidir com uma inicial de outra reta, a scanline também faz pintura 2 a 2 interseções. O problema é que isso independe do caso, e um triângulo na horizontal também sofrerá disso. Para resolver o problema, usamos a seguinte artimanha: a interseção passa a ignorar agora quando $t = 0$, ou seja, se interseccionar um vértice inicial de alguma reta, ele para de fazer 2 a 2 nesse caso do triângulo horizontal, e será feita a scanline normalmente. Porém,  na figura da montanha, terá o problema de não desenhar tudo. Como resolver isso? Assim:

![](2023-05-11-18-48-13.png)

O que eu fiz aqui? Basicamente eu ignorei a interseção quando t for zero, que é quando a scanline passa por algum vértice inicial. Porém, isso quebra a outra exceção, que já estava bonitinha funcionando. Então para resolver de vez o problema, no próprio algoritmo de interseção, invertemos os valores $P_f$ e $P_i$ quando a construção da aresta do polígono for feita de baixo pra cima. Quando for de cima pra baixo, faz nada. Assim resolvemos o problema, pois sempre que tiver dois vértices coincidindo e a scanline precisa pintar horizontalmente, ela vai pintar sempre em 2 pontos finais, o que é perfeito para fazer pinturas em interseções 2 a 2.

