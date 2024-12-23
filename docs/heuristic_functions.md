# Funções Heurísticas

Funções heurísticas são aquelas funções usadas para determinar quão próximo um determinado estado está do estado desejado, elas variam e devem ser modificadas para satisfazer problemas específicos. São usadas quando não se tem uma solução fixa ou quando demora muito tempo encontrar uma solução para o problema, seu propósito é encontrar uma solução mais aproximada ou de forma mais rápida. (by simplilearn)

## Características

- **Admissível:** Uma heurística é admissível quando produz uma solução ótima, ou seja, não superestima o custo de chegar ao estado-objetivo.
- **Completa:** Uma heurística é completa se o algoritmo que a usa acaba em uma solução.
- **Propriedade de dominação:** Se houver dois algoritmos heurísticos que usam duas funções heurísticas diferentes, o algoritmo que domina o outro será aquele que usa a melhor heurística para todos os nós.
- **Propriedade de optimalidade:** O algoritmo que produz o melhor resultado será aquele que é minucioso, permissível e domina os outros algoritmos.

## Qualidade

Existem duas propostas para medir a qualidade de uma heurística a primeira é o fator de ramificação efetiva (b*) que é calculado pela seguinte fórmula N + 1 = 1 + b* + (b*)<sup>2</sup> + ... + (b*)<sup>d</sup> em que N é o número de nós gerados pelo algoritmo e d é a profundidade onde a solução está. Quanto melhor a heurística, mais próximo de um estará o valor do fator de ramificação efetivo.

Outra forma de medir a qualidade é a redução da profundidade efetiva comparado com a profundidade real d, que resulta em uma redução do custo de busca O(b<sup>d</sup>) para O(b<sup>d - kh</sup>), quanto maior for a redução melhor será a heurística.

## Geração de heurísticas

### Problemas relaxados

Um problema relaxado é uma versão de um problema já existente com menos restrições nas ações que podem ser realizadas, vendo-o a partir da abordagem de um grafo de estados o problema relaxado é um supergrafo comparado ao problema normal, pois o menor número de restrições resulta em um maior número de bordas. Porque o grafo de estado do problema original está dentro do grafo de estado do problema relaxado qualquer solução do problema original também se aplica ao problema relaxado, mas devido às bordas extras é possível encontrar atalhos que podem resultar em uma melhor solução para o problema original.

### Sub-problemas

Heurísticas também podem ser geradas pelo custo de resolver um subproblema, ou seja, alguns elementos do problema são levados em conta e outros são ignorados. A forma como isso é feito é através de bancos de dados padrão em que todos os custos de solução de todos os possíveis subproblemas são armazenados, depois calcula-se a heurística de um estado simplesmente procurando o subproblema que contém no banco de dados. Se um estado tiver vários subproblemas possíveis que possam ser aplicados para decidir qual heurística usar, todas as heurísticas possíveis serão combinadas e a que tiver o melhor valor será escolhida. Nesses subproblemas os elementos que não fazem parte do subproblema são abstraídos, ou seja, não se levam em conta para a solução mas sim devem ser levados em consideração nos movimentos que se realizam para chegar a esse resultado.

Si es que se quiere aplicar multiples subproblemas a un estado pues estos no se sobreponen se deberá aplicar bases de datos de patrones disjuntos las cuales son similares a las bases de datos de patrones regulares excepto que en lugar de registrar el costo total de resolver el subproblema apenas o custo dos movimentos que envolvem os elementos membros do subproblema é calculado, ou seja, em vez de abstrair elementos que não fazem parte do subproblema estes já não são levados em conta. Isso funciona porque os elementos que não são considerados em um subproblema aplicado serão considerados para outro subproblema que é aplicado ao mesmo estado. No final somam-se os custos de resolução de todos os subproblemas aplicados e isto resulta em um custo menor do que seria necessário resolver todo o problema.

### Pontos de referência

### Experiência