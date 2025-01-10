# Funções Heurísticas

Funções heurísticas são aquelas funções usadas para determinar quão próximo um determinado estado está do estado desejado, elas variam e devem ser modificadas para satisfazer problemas específicos. São usadas quando não se tem uma solução fixa ou quando demora muito tempo encontrar uma solução para o problema, seu propósito é encontrar uma solução mais aproximada ou de forma mais rápida. [11]

## Características

- **Admissível:** Uma heurística é admissível quando produz uma solução ótima, ou seja, não superestima o custo de chegar ao estado-objetivo. [11]
- **Completa:** Uma heurística é completa se o algoritmo que a usa acaba em uma solução. [11]
- **Propriedade de dominação:** Se houver dois algoritmos heurísticos que usam duas funções heurísticas diferentes, o algoritmo que domina o outro será aquele que usa a melhor heurística para todos os nós. [11]
- **Propriedade de optimalidade:** O algoritmo que produz o melhor resultado será aquele que é minucioso, permissível e domina os outros algoritmos. [11]

## Qualidade

Existem duas propostas para medir a qualidade de uma heurística a primeira é o fator de ramificação efetiva (b*) que é calculado pela seguinte fórmula N + 1 = 1 + b* + (b*)<sup>2</sup> + ... + (b*)<sup>d</sup> em que N é o número de nós gerados pelo algoritmo e d é a profundidade onde a solução está. Quanto melhor a heurística, mais próximo de um estará o valor do fator de ramificação efetivo. [5]

Outra forma de medir a qualidade é a redução da profundidade efetiva comparado com a profundidade real d, que resulta em uma redução do custo de busca O(b<sup>d</sup>) para O(b<sup>d - kh</sup>), quanto maior for a redução melhor será a heurística. [5]

## Geração de heurísticas

### Problemas relaxados

Um problema relaxado é uma versão de um problema já existente com menos restrições nas ações que podem ser realizadas, vendo-o a partir da abordagem de um grafo de estados o problema relaxado é um supergrafo comparado ao problema normal, pois o menor número de restrições resulta em um maior número de bordas. Porque o grafo de estado do problema original está dentro do grafo de estado do problema relaxado qualquer solução do problema original também se aplica ao problema relaxado, mas devido às bordas extras é possível encontrar atalhos que podem resultar em uma melhor solução para o problema original. [5]

### Sub-problemas

Heurísticas também podem ser geradas pelo custo de resolver um subproblema, ou seja, alguns elementos do problema são levados em conta e outros são ignorados. A forma como isso é feito é através de bancos de dados padrão em que todos os custos de solução de todos os possíveis subproblemas são armazenados, depois calcula-se a heurística de um estado simplesmente procurando o subproblema que contém no banco de dados. Se um estado tiver vários subproblemas possíveis que possam ser aplicados para decidir qual heurística usar, todas as heurísticas possíveis serão combinadas e a que tiver o melhor valor será escolhida. Nesses subproblemas os elementos que não fazem parte do subproblema são abstraídos, ou seja, não se levam em conta para a solução mas sim devem ser levados em consideração nos movimentos que se realizam para chegar a esse resultado. [5]

Si es que se quiere aplicar multiples subproblemas a un estado pues estos no se sobreponen se deberá aplicar bases de datos de patrones disjuntos las cuales son similares a las bases de datos de patrones regulares excepto que en lugar de registrar el costo total de resolver el subproblema apenas o custo dos movimentos que envolvem os elementos membros do subproblema é calculado, ou seja, em vez de abstrair elementos que não fazem parte do subproblema estes já não são levados em conta. Isso funciona porque os elementos que não são considerados em um subproblema aplicado serão considerados para outro subproblema que é aplicado ao mesmo estado. No final somam-se os custos de resolução de todos os subproblemas aplicados e isto resulta em um custo menor do que seria necessário resolver todo o problema. [5]

### Pontos de referência

Consiste em criar alguns (10 a 20) pontos de referência dentro do gráfico e calcular o custo da trajetória ótima de cada nó ao ponto de referência e vice-versa C (n, L) e C (L, n); num gráfico não direcionado o cálculo dos dois é igual, em um gráfico não direcionado devem ser calculados separadamente. Depois de calcular a heurística somar o custo de chegar ao ponto de referência e o custo do ponto de referência para o objetivo, finalmente se escolhe o custo mínimo de todos os pontos de referência, isto pode ser visualizado assim hL(n) = min(L∈Landmarks) (C*(n, L) + C*(L, objetivo)). Essa heurística só funciona se o caminho ótimo passa por um ponto de referência, caso contrário é inadmissível. [5]

Uma forma de tornar essa heurística admissível é usando hDH(n) = max(L Landmarks)(|C (n,L) C (goal,L)|) em que se escoge um ponto de referência que este mais longe do que o objetivo para depois traçar o caminho mais ideal ao ponto de referênica, Finalmente, o traço final do alvo ao ponto de referência é removido para obter o custo do caminho de n ao objetivo. Esta heurística é admissível, pois não superestima o custo para o objetivo, no entanto se o objetivo não está no caminho ótimo para o ponto de referência essa heurística será imprecisa. Isso é conhecido como uma heurística diferencial devido à subtracção. [5]

Para escolher pontos de referência é recomendado que estes sejam o mais longe um do outro como possível, uma maneira gananciosa de fazer isso é escolher um ponto de referência aleatório e encontrar o nó que está mais longe desse ponto para depois adicioná-lo à lista de pontos de referência, este processo é repetido até que a quantidade desejada de pontos tenha sido adicionada. Para heurística diferencial é recomendado que os pontos de referência estão distribuídos em torno do perímetro do grafo, para garantir isso é o centro do grafo realizar k "cortes" em forma de pedaço de torta ao redor do centro, e em cada corte selecionar o vértice que está mais longe do centro. [5]

### Experiência

Usar a experiência para obter heurísticas usando exemplos de caminho/objetivo feitos com base em resoluções anteriores de problemas do mesmo tipo. Usando esses exemplos, construa-se uma função h que aproximará o verdadeiro custo de caminho de algum estado/nó que aparecer durante a busca. A aproximação à função heurística desta abordagem é imperfeita, pelo que sempre se faz um compromisso entre o tempo de aprendizagem, o tempo de execução da busca e o custo da solução. [5]

Outra maneira de fazer isso é usando características do problema que são relevantes para prever o valor heurístico do estado. Dependendo do valor dessas características, pode-se encontrar um certo valor médio de resolução do problema. Para melhores resultados, múltiplas características podem ser combinadas usando a fórmula h(n) = c1x1(n) + c2x2(n) onde x1 e x2 são as características e c1 e c2 são constantes que devem ser ajustadas para obter os melhores resultados. [5]