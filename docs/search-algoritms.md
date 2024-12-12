# Algoritmos de busca

São algoritmos que recebem um problema de busca como entrada e produzem uma solução, estes usam algo chamado árvore de busca, estes são compostos por nós que representam um estado específico e as bordas que correspondem a ações que levam a diferentes estados; essas árvores formam múltiplas rotas do nó raiz que é o estado inicial do problema, o objetivo do algoritmo de busca é encontrar uma rota que leve ao nó (estado) alvo.
A árvore da busca faz parte de algo conhecido como espaço de estados, estes são os múltiplos e provavelmente infinitos estados que existem no mundo e as ações que levam de um estado para outro; o arvore de busca são caminhos específicos neste espaço de estados que se originam a partir de um único estado raiz.
Em uma árvore de busca existem dois tipos de nós, nós pai, que são os nós a partir dos quais outros nós são gerados, estes nós gerados passam a ser chamados de nós filhos ou sucessores.
A fronteira é conhecida como a separação da região onde todos os nós foram expandidos, ou seja, são mostrados os nós sucessores conectados a este sem escolher nenhum e a região onde estão aqueles nós que ainda não foram alcançados.

### Busca primeiro o melhor

É uma forma de escolher qual dos nós vai expandir, esta baseia-se em escolher o caminho que tem o menor custo possível, esse custo é determinado por uma função de avaliação; o resultado será uma indicação de falha ou um caminho para um nó alvo.

### Estruturas de dados de busca

#### Nós

Para armazenar os nós, uma estrutura de dados com quatro componentes é usada.
- node.STATE: o estado que corresponde ao nó.
- node.PARENT: o nó que gera o nó atual.
- node.ACTION: a ação que foi aplicada ao nó pai para gerar este nó.
- node.PATH-COST: o custo total do caminho do nó inicial ao atual.

#### Fronteira

Para armazenar a fronteira é usada uma fila, as operações nessa fronteira são:
- IS-EMPTY(frontier): só retorna True quando não há nós na fronteira.
- POP(frontier): remove o nó superior da fronteira e apresenta-lo.
- TOP(frontier): apresenta, mas não elimina, o nó superior da fronteira.
- ADD(node, frontier): insere um nó na fronteira.

#### Tipos de filas

- Fila de prioridade: o primeiro nó que usar a função POP será aquele com o custo mínimo determinado pela função de avaliação
- Fila FIFO: o primeiro nó a ser usado pela função POP, será aquele que foi inserido primeiro na fila.
- Fila LIFO: o primeiro nó a ser usado pela função POP será aquele que foi inserido mais recentemente na fila.

### Medir el rendimiento en la resolución de problemas

Critério utilizado para escolher algoritmos de busca, o desempenho pode ser medido em quatro formas:
- Completude: O algoritmo pode encontrar uma solução ou relatar sua falha quando não há uma? O algoritmo deve ser capaz, independentemente do tamanho do espaço, chegar a um estado que esteja conectado com o estado inicial.
- Otimização de custos: Pode encontrar uma solução com o menor custo de todas as soluções?
- Complexidade de tempo: Quanto tempo leva para encontrar uma solução. Pode ser medido em uma unidade de tempo como segundos ou pelo número de ações e estados.
- Complexidade do espaço: Quanta memória é usada para fazer a busca.

## Busca cega

Algoritmos que não possuem informações sobre o espaço de busca, dependem unicamente da estrutura do espaço de busca para encontrar uma solução. Eles são apenas capazes de gerar sucessores e diferenciar entre o estado objetivo e não-objetivo. Os planos para chegar ao estado-alvo a partir do estado inicial são diferenciados apenas pela ordem e duração das ações.

### Busca por amplitude

Estratégia apropriada quando todas as ações têm o mesmo custo, baseia-se em expandir primeiro todos os nós pai antes de expandir seus sucessores, começando com o nó raiz. É uma estratégia de busca sistemática, então funciona mesmo em espaços de estados infinitos. A função de avaliação é o número de ações que são tomadas para chegar a um nó. Para essa estratégia, uma fila FIFO é usada, onde os novos nós vão para o final da fila e os mais antigos ficam no início. Essa estratégia permite verificar se um estado é o alvo antes que ele saia da fila, porque uma vez que um estado foi atingido não será possível encontrar um caminho melhor. Busca por profundidade sempre encontra uma solução com o menor número de ações pois esta gera todos os nós em um "nível" antes de passar ao próximo pelo que se a solução estiver nesse "nível" já teria sido encontrada. Esta estratégia possui uma complexidade de tempo e espaço de O(b<sup>d</sup>) onde b são os nós sucessores e d é a profundidade da árvore de busca.

### Algoritmo de Dijkstra

Também conhecido como busca de custo uniforme é usado quando as ações têm custos diferentes, baseia-se em expandir primeiro o estado que tem o menor custo, esses custos são atribuídos com base no custo que têm todas as ações tomadas para chegar a esse estado. Se durante o processo for encontrado um caminho com menor custo para um estado que já havia sido alcançado, este caminho substituirá o anterior. A complexidade do algoritmo de Dijkstra é de O(b<sup>1 + [C*/e]</sup>) onde C* é o custo da solução ideal, e é o custo mínimo de uma ação com e > 0 e b é o número de vizinhos por nó. Esta estratégia é completa e de custo ótimo, pois a primeira solução que encontrar terá um custo tão baixo quanto o custo de qualquer outro nó.

### Busca por profundidade

Esta estratégia é baseada em expandir primeiro os nós sucessores antes de expandir os nós pai, nesta mente automaticamente "abaixa" tudo o que pode na árvore de busca até encontrar um nó que não tenha sucessores, Então, um nível é elevado e verifica se o nó pai tem outros nós sucessores não expandidos, se este for o caso, passa a expandir estes. Esta estratégia não é eficaz em custo, pois retorna a primeira solução que encontra. Somente é eficaz em espaços finitos que são árvores, em espaços cíclicos pode ficar presa em um loop infinito e em espaços infinitos é possível que termine presa em um caminho infinito mesmo não havendo ciclos, pelo que não é sistemática. Uma das suas principais vantagens e a principal razão pela qual é usado é a baixa quantidade de memória necessária. Sua complexidade espacial, somente em espaços onde é aplicável, é de O(bm) onde b é o fator de ramificação (número de filhos em cada nó) e m é a profundidade máxima da árvore.

### Busca por profundidade limitada

É uma versão de busca por profundidade na qual os nós que estão em uma profundidade l definida anteriormente, serão considerados como se não tivessem sucessores. Isso é feito com o objetivo de que a busca por profundidade não fique presa em um caminho infinito. A complexidade do espaço é O(b<sup>l</sup>) enquanto que a complexidade do tempo é O(bl) onde b é o fator de ramificação (número de filhos em cada nó) e l é a profundidade limite. Escolher o limite certo é muito importante, pois disso depende que o algoritmo possa alcançar a solução. Para aumentar a qualidade do limite definido pode-se usar informação que está disponível sobre o problema. Uma maneira bastante simples de definir esse limite é o número de nós na árvore menos um; no entanto, uma forma muito mais eficaz que é usar o diâmetro do grafo, este é o caminho mais curto entre os nós mais distantes no grafo. Infelizmente, na maioria dos casos, informações como o diâmetro não estarão disponíveis até que o problema seja resolvido.

### Busca iterativa de aprofundamento

### Busca bidirecional

## Busca informada