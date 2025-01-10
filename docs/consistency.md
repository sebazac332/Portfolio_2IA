# Consistência

Os valores dados às variáveis são conhecidos como atribuições, uma atribuição que não viola nenhuma condição é conhecida como consistente, uma atribuição completa é quando todas as variáveis têm um valor e, finalmente, uma solução é uma atribuição consistente e completa. Por outro lado, quando há variáveis que não têm nenhum valor, isso é conhecido como atribuição parcial e uma solução parcial é uma atribuição parcial consistente. [1]

## Consistência de nós

Consistência de nó refere-se a quando o domínio de uma única variável cumpre todas as condições impostas a ela. Ex: A variável A tem um domínio de {2, 4, 6, 8} e tem uma condição que estipula que A não pode ser divisível por 3, para que A possa ter consistência de nó 6 deve ser removido do domínio. Um grafo é dito ter consistência de nó quando todas as variáveis do grafo são consistentes de nó. [1]
 
## Consistência do arco

Uma variável é arco consistente se todos os valores do seu domínio satisfazem suas condições binárias. Ex: A e B possuem um domínio tal que {(1,2),(2,3),(3,4),(6,5)} respetivamente, mas possuem uma condição que estipula que A < B, para que se possa considerar arco consistente a A em relação a B deve-se restringir seu domínio a {1, 2, 3} e para que B possa ser considerado um arco consistente em relação a A, seu domínio deve ser restrito a {2, 3, 4}. Um grafo é considerado consistente se todas as suas variáveis são consistentes entre si. [1]

## Consistência do caminho

Variáveis são consideradas consistência de caminho quando não têm consistência binária entre si, mas também são consistentes com uma terceira variável, por uma condição implícita. Ex: Você tem as variáveis A, B e C com domínios {1, 2, 3}; {2, 3} e {3, 4} respectivamente e têm as condições A < B, A /= C e B /= C para que A e B tenham consistência de caminho em relação a C deve-se reduzir o domínio de A para {1, 2} e o de B para {2}. [1]

## Consistência K

A k-Consistência generaliza o conceito de consistência de arco e caminho para k variáveis. Ela garante que, para cada subconjunto de k-1 variáveis, haja um valor consistente na k-ésima variável. Níveis mais altos de consistência proporcionam mais poda, mas são computacionalmente mais caros. [8]

## Consistência global

As restrições globais ocorrem com frequência em problemas reais e podem ser tratadas por algoritmos para fins especiais que são mais eficientes do que os métodos para fins gerais descritos até agora. O algoritmo é o seguinte: Primeiro, remova qualquer variável da restrição que tenha um domínio único e exclua o valor dessa variável dos domínios das variáveis restantes. Repita o procedimento enquanto houver variáveis singleton. Se em algum momento for produzido um domínio vazio ou se houver mais variáveis do que valores de domínio restantes, então foi detectada uma inconsistência. [1]

Para grandes problemas de recursos limitados com valores inteiros, geralmente não é possível representar o domínio de cada variável como um grande conjunto de números inteiros e reduzir gradualmente esse conjunto por meio de métodos de verificação de consistência. Em vez disso, os domínios são representados por limites superiores e inferiores e são gerenciados pela propagação de limites. Neste caso, o processo altera os limites superiores e inferiores dos intervalos para que estes cumpram as condições. [1]