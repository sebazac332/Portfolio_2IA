# Consistência

Os valores dados às variáveis são conhecidos como atribuições, uma atribuição que não viola nenhuma condição é conhecida como consistente, uma atribuição completa é quando todas as variáveis têm um valor e, finalmente, uma solução é uma atribuição consistente e completa. Por outro lado, quando há variáveis que não têm nenhum valor, isso é conhecido como atribuição parcial e uma solução parcial é uma atribuição parcial consistente.

## Consistência de nós

Consistência de nó refere-se a quando o domínio de uma única variável cumpre todas as condições impostas a ela. Ex: A variável A tem um domínio de {2, 4, 6, 8} e tem uma condição que estipula que A não pode ser divisível por 3, para que A possa ter consistência de nó 6 deve ser removido do domínio. Um grafo é dito ter consistência de nó quando todas as variáveis do grafo são consistentes de nó.
 
## Consistência do arco

Uma variável é arco consistente se todos os valores do seu domínio satisfazem suas condições binárias. Ex: A e B possuem um domínio tal que {(1,2),(2,3),(3,4),(6,5)} respetivamente, mas possuem uma condição que estipula que A < B, para que se possa considerar arco consistente a A em relação a B deve-se restringir seu domínio a {1, 2, 3} e para que B possa ser considerado um arco consistente em relação a A, seu domínio deve ser restrito a {2, 3, 4}. Um grafo é considerado consistente se todas as suas variáveis são consistentes entre si.

## Consistência do caminho

Variáveis são consideradas consistência de caminho quando não têm consistência binária entre si, mas também são consistentes com uma terceira variável, por uma condição implícita. Ex: Você tem as variáveis A, B e C com domínios {1, 2, 3}; {2, 3} e {3, 4} respectivamente e têm as condições A < B, A /= C e B /= C para que A e B tenham consistência de caminho em relação a C deve-se reduzir o domínio de A para {1, 2} e o de B para {2}.

## Consistência K



## Consistência global

