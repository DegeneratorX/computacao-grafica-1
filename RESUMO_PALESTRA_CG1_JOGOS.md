https://vimeo.com/842318468/8fd617e7b2

# Desenvolvimento de Jogos: Desafios e Perspectivas na Criação de Personagens Inteligentes

Essa palestra foi ministrada pelo discente Matheus, aluno de doutourado pela Universidade Federal do Ceará, no dia 4 de julho de 2023, as 18:00. Esses são os principais tópicos de sua palestra.

Feito por: Victor Medeiros Martins - 401339

# Jogo - do que eles são feitos?

### Planejamento básico

Qualquer jogo básico hoje precisa de um roteiro, áudio, design, modelagem 2D/3D e lógica de programação. Sem esses pilares, é difícil atender a demanda do mercado de jogos modernos hoje em dia. Porém existem casos raros de jogos sem roteiro que deram certo. É o caso do Minecraft, que não possui um objetivo concreto, e cabe ao jogador criar seu próprio roteiro, ou o BeamNG Drive, que é um simulador de batidas de carro.

### Planejamento avançado

Para produções em larga escala de jogos, é necessário seguir tópicos mais avançados de planejamento, e por isso irei separar eles aqui:

- Pré-Produção
    - Ideia
        - Trata-se de uma ideia inicial para a elaboração de um jogo.
    - Análise de Requisitos e Pré-Venda
    - Game Concept
        - Seria um esborço inicial do jogo, com descrição e objetivos

- Produção: Projeto
    - Game Design
        - Trata-se da parte de desenhar o jogo, implementar o gráfico inicial dele
    - Protótipos
        - Versões diferentes do mesmo esborço aplicados, um deles será escolhido para uma versão de implementação.
    - Testes Intermediários
        - Testes de protótipos para ter uma ideia de como será o jogo e sua receptividade

- Produção: Implementação
    - Implementação de Arte, Programação e Música
    - Testes Intermediários
        - Serve para testar game-breaking glitches, bugs gráficos, bugs de física, bugs de som ou bugs de lógica de programação

- Pós-Produção
    - Testes Finais
        - Voltado para beta-testers, mídia especializada de jogos (pré-receptividade do jogo), resolver problemas de otimização, melhorar a qualidade de vida (QoL) e detalhes não resolvidos que podem passar despercebidos
    - Entrega
    - Pós-Venda
        - Pode incluir a avaliação do sucesso do jogo, ver se existe a possibilidade de uma sequência, ou correções de bugs com patches de correção.

Atualmente existe um desafio que precisaremos enfrentar: como usar a inteligência artificial crescente a nosso favor, de forma que possamos aumentar a interação e a imersão nos games?

# Imersão

Será que apenas jogos com gráficos realistas são suficientes? Afinal, o jogo recebe um input, e esse input depende do usuário. Um filme de alto orçamento normalmente também possui gráficos bem realistas quando se trata de CGI, mas as interações e comportamentos são pre-renderizados, o que não necessita de um input de quem assiste. Nos jogos, há essa necessidade do input, e por isso a imersão é maior, pois existe uma resposta para cada ação do jogador.

Porém, se os inputs geram outputs que não correspondem ao que o usuário esperava, o jogo tende a perder a sua imersão. As vezes nem precisa de inputs, pois coisas não naturais nos jogos também podem ocorrer de repente. Como melhorar?

> Curiosidade: A 40 anos atrás era surreal o fato de que poderíamos controlar os gráficos de nossa televisão com controles de videogame, pois as pessoas estavam acostumadas a ver coisas prontas sendo exibidas. Porém, finalmente você poderia interagir com algo que de fato aparecia na tela da sua TV, e isso é um fator chave para aumentar a imersão do usuário com o que está sendo exibido na tela. Por isso os home consoles passaram a se popularizar drasticamente. Hoje as pessoas já se acostumaram, mas na época isso era revolucionário.

# Vale da Estranheza

Na computação gráfica, quando estamos muito focados em realismo gráfico, é possível que quando se mistura o excesso de realismo com coisas que não estamos habituados a ver ou são impossíveis de acontecer ou existir, gere estranheza nas pessoas. O nome disso é **Uncanny Valley**, ou **Vale da Estranheza**.

O Vale da Estranheza é bastante comum também na robôtica, pois a tentativa de se criar humanóides que possuem características realistas próximas aos seres humanos, mas suficientemente identificáveis que são robôs, geram estranheza ou repulsa. 

Esse é um tema muito recente e ainda precisará ser estudado ao longo das décadas (e até séculos), pois ainda não se sabe se esse é um evento decorrente da falta de costume de interagir com robôs, ou a cultura do cinema hollywoodiano influenciou as pessoas a sentirem repulsa de casos dessa natureza.

# NPCs (Non-Playable Character)

São uma classe de entidades nos jogos que não podem ser diretamente controladas pelo jogador.

Todo NPC possui minimamente em um jogo de qualidade:
- Malha poligonal (quadrados ou triangulares) que irá dar a forma geométrica
- Textura (mapeado para cada parte do corpo)
- Sensores (envolve lógica de programação, detecção de outros objetos ou entidades próximos)
- Atuadores (mãos e pernas, servem para fazer ações)
- Graus de liberdade (o que ele pode fazer ou não)
- Motor de física (pode ou não ter)
- Animação (movimentação pre-programada, pode substituir a física em alguns casos)
- Roteiro (seu papel no jogo)
- Recursos (emitir áudio, eventos específicos)

# Problema

O nosso problema principal é tentar pular esse vale da estranheza. O uso de ifs e elses não gera comportamentos complexos. Na verdade pode aumentar a complexidade do problema. A ideia seria simplificar a geração de comportamentos complexos. Como fazer isso?

### Regras

A ideia de criar regras para um NPC ou entidade não gera comportamentos elaborados, pois para isso seria preciso criar milhares, se não centenas de milhares de regras para chegar próximo do comportamento humano.

### Aprendizado

A ideia de aprendizado de máquina é muito boa, porém para criar uma boa base de dados baseado no que apenas um NPC aprendeu pode levar tempo e um alto custo de memória, e mesmo nessa época de corridas da inteligência artificial, nenhum jogo foi capaz de levar isso pra frente com tanta ênfase, pois ainda existem muitos fatores limitantes.

# Soluções

Aqui estão algumas soluções para tentar chegar ao ideal do realismo dos NPCs em torno de um ambiente nos jogos.

### Agente racional

Age em um ambiente, maximizando sua medida de desempenho para atingir o objetivo.

Ele possui sensores que ajudam a atuar nesse ambiente, e cada vez que o ambiente é modificado, os sensores percebem as alterações e os agentes passam a atuar de forma melhorada e adaptada ao novo ambiente.

Isso também é chamado de IA Corporificada.


### NPCs com Heurísticas

Existem algumas técnicas que implementam isso. As mais conhecidas são:

- Máquinas de estado finito
    - São tomadas de decisão através de autômatos de acordo com o estado da máquina para chegar ao objetivo
- Redes Neurais
    - Simula um cérebro humano, faz parte do processo de aprendizado de máquina
- Árvores de decisão
    - Normalmente são árvores binárias que executam de acordo com os objetivos que o NPC foi programado.
- Lógica Fuzzy
    - São tomadas de decisão, mas com pesos, para tentar simular um erro humano.

### NPCs com Plano e Mapa

Essa ideia implementa aos NPCs um mapa próprio em formato de caminhos, onde eles o utilizam para descobrir caminhos mínimos, fluxos máximos ou fazer buscas, tudo utilizando a ideia de grafos.

Sim, NPCs podem ter uma representação de um mapa programado para si, e nesse mapa "próprio" possui grafos.

### NPCs com Controlador Neural

São NPCs dotados de uma rede neural que recebem o estado na entrada e classificam a melhor ação.

Se o NPC fizer um estado certo, a gente recompensa ele. Por exemplo, um NPC vê uma escada. Se o NPC (controlado por uma rede neural) escalar, então ele ganha uma recompensa, e ele é programado para perceber que, se ele receber uma recompensa, sempre que ele ver outras escadas, ele pode ganhar outra recompensa, e assim associa positivamente a escada com o ato de escalar.

Isso é feito através do que chamamos de **Aprendizado por Reforço Profundo**, que basicamente treina por tentativa e erro, recompensando o agente quando ele escolher a ação certa.

### Neuroevolução

Essa solução é comparada com a seleção natural.

São utilizadas múltiplas cópias de agentes, os melhores sobrevivem, se adaptam e "reproduzem", ou seja, combinam seus pesos de rede neural.

# Visão Artificial

Todas essas soluções anteriores possuem algo em comum: sensores, que enxergam.

Essas soluções são comparadas com a diversidade evolutiva na vida real:

- O surgimento dos olhos foi uma nova dinâmica entre predadores e presas
- Olhos na frente do crânio costumam ser associados a animais predadores no reino animal. Ajudam na focalização de uma presa.
- Olhos nas laterais do crânio costumam ser associados aos animais herbívoros, muitas vezes sendo a presa de animais predadores. Funcionam como sentinela, e ajudam no escape de predadores.

Um desafio nos campos de pesquisa de inteligência artificial seria o uso do Córtex Visual Artificial, que gera uma forte conexão entre a mente e o ambiente ao qual o agente está localizado. É um avanço na inteligência artificial que permite que robôs interajam com o mundo real assim como humanos. E poderia não ser diferente quando agentes visualizam um ambiente virtual. Uma das features seria o uso da visão do agente, que funciona como uma câmera virtual acoplada, que recebe inputs visuais de alta dimensão desse ambiente para tomar decisões.

# XAI

XAI deriva de Inteligência Artificial Explicativa. É utilizada quando a decisão tomada não é direta. Por exemplo, se tem a foto de um gato, a IA normalmente diz: é um gato. Mas A IA explicativa diz:
- É um gato
    - Pois na foto tem orelhas únicas pontudas
    - Tem garras

A IA explicativa observa detalhes únicos que darão mais probabilidade de conclusão. Só olhando pro corpo de um animal é inconclusivo, e por isso a tomada de decisão precisa ser melhorada.

# Vida Artificial e Autonomia

Um dos desafios utilizando inteligência artificial é recriar fenômenos biológicos em computadores.

Alguns comportamentos incluem as necessidades de fome, sede, ou até mesmo a simulação da criação de uma vida autônoma.

O ChatGPT, por exemplo, não é um agente 100% autônomo, pois ele usa exemplos da internet para tomada de decisões baseado no input do usuário. Porém, se quisermos dar autonomia para alguma IA, precisaremos estabelecar alguns fatores e características a IA, como

- Recompensa Intrínseca: ao invés de recompensar por fazer algo certo, recompensar se ele faz o certo baseado no que ele observou que deu errado em casos passados;

- Agentes Emocionais: recompensar baseado no sentimento legítimo de medo, fome e tristeza;

- Curiosidade Artificial: se trata do agente sentir motivação natural de explorar novas coisas ou ambientes;

- Hedonísmo: se trata do agente que busca sua sobrevivência e seu prazer acima de tudo.