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