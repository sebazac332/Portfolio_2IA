# Definindo Problemas de Satisfação de Condições

Um problema de satisfação de condições é um problema com representação factorada em que além de encontrar a solução, os valores atribuídos às variáveis devem cumprir uma série de restrições. [5] A ideia principal é eliminar porções do espaço de busca identificando combinações onde o valor das variáveis viola as restrições. [1] Uma vantagem que eles têm é que as ações que podem ser tomadas e o modelo de transições (modelo que mostra a quais estados leva cada ação) pode ser deduzido da descrição do problema. [1]

Algoritmos de problemas de satisfação de condições podem ser usados em:

- Programação: Alocação de recursos como funcionários ou equipes respeitando as restrições de tempo e disponibilidade. [5]
- Planejamento: organização de tarefas com prazos ou sequências específicas. [5]
- Alocação de recursos: Distribuir os recursos de forma eficiente sem usá-los em excesso. [5]

## Componentes

1. **Variáveis:** São os objetos que devem ser avaliados para cumprir as condições, alguns tipos de variáveis são booleanas, inteiras e variáveis categóricas. [5]

2. **Dominios:** Representam o intervalo de valores possíveis que uma variável pode ter, dependendo do problema os domínios podem ser finitos ou infinitos. [5]

    - **Dominio finito:** Contém um número específico de elementos, os quais podem ser listados em um período finito de tempo. [1]

    - **Dominio infinito:** Não há limite no número de valores possíveis, esses valores não podem ser listados em um período de tempo limitado. Para esses domínios, condições implícitas ex: <(A,B), A < B> devem ser usadas em vez de valores específicos ex: <(A,B), {(0,1),(1,2),(2,3),...}>. [1]

    - **Dominio discreto:** Contém valores diferentes ex: {1, 2, 3, 4, 5}. [1]

    - **Dominio contínuo:** Consiste em um intervalo de valores possíveis, por exemplo: números reais no intervalo [0, 1]. [1]

3. **Condições:** São guias que controlam como as variáveis se relacionam umas com as outras, definem os possíveis valores válidos que as variáveis podem ter. Condições unárias, binárias e de maior ordem são alguns exemplos de tipos de condições. [5] As condições são representadas como um par escopo, relação (<escopo, relação>), onde o escopo são as variáveis que participam da condição e a relação são os valores que essas variáveis podem tomar. Ex: <(X1,X2),{(3,1), (3,2), (2,1)}> ou <(X1,X2),X1 > X2>. [1]

## Tipos de condições

1. **Condições duras e suaves:** Conduções duras são aquelas que devem ser obrigatoriamente cumpridas enquanto as condições suaves podem ser violadas, no entanto isso resulta em um custo adicional. [5]

2. **Condições de precedência:** Determina a ordem em que as atividades dentro do problema devem ser realizadas, especificamente determina quais atividades terminam antes das outras. Ex: atividade T1 termina antes de T2 e esta demora um tempo d, a expressão da condição seria esta T1 + d1 ≤ T2. [1]

3. **Condição disjuntiva:** Condições que obrigam a escolher apenas um valor de entre um conjunto, se A ocorre B não pode ocorrer e vice-versa. Ex: (AxleF +10 AxleB) ou (AxleB+10 AxleF), apenas um deles pode ser verdade, não ambos. [1]

4. **Condições lineares:** Condições que não contêm raizes ou potências e cujo valor aumenta ou diminui de forma porporcional, seguem a forma aritmética Y = m X + b. [6]

5. **Condições não lineares:** Condições que contêm raizes ou potências, todas as condições que não se enquadram na definição de linear são automaticamente não lineares. [7]

6. **Condições unárias:** Restringe o valor de uma única variável, geralmente define que valores uma variável não pode tomar, seja colocando limites como >= ou <= ou proibindo totalmente certos valores /= green. [1]

7. **Condições Binarias:** Restringe os valores de duas variáveis, pode ser relacionado um com o outro A <= B ou relacionados com um terceiro valor A + B = 3. [1]

8. **Condições Ternária:** Restringe os valores de três variáveis, podem estar relacionadas entre si A < B < C ou relacionadas com um quarto valor A + B + C = 4. [1]
 
9. **Condições globais:** Restringe os valores de um número arbitrário de variáveis, este pode ser qualquer número maior que quatro incluindo todas as variáveis existentes no problema. Ex: Alldiff, condição que estipula que todas as variáveis devem ter valores diferentes. [1]

10. **Condições de preferência:** Condições não obrigatórias que ajudam a decidir quais soluções escolher, supondo que há múltiplos. Ex: em uma situação se pedem dois números pares, o número de opções foi reduzido a dois números 6 e 4, uma condição de preferência é que esse número seja múltiplo de 3, portanto a solução escolhida será o número 6; se em vez de 6 e 4 as opções fossem 2 e 4 ainda poderia ter sido escolhido uma solução válida mesmo que a condição não fosse cumprida. [1]