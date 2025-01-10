# Representação Atômica vs. Fatorada

As representações são categorizadas em um eixo de complexidade e capacidade expressiva onde a representação atômica é a menos complexa e também menos expressiva, seguida por representação fatorial e finalmente representação estruturada. [4]

## Representação Atômica

Cada estado do mundo pode ser considerado como uma caixa preta que não tem estrutura interna, sabe-se qual é o estado mas não os elementos que contém. Um exemplo seria tentar traçar uma rota entre duas cidades, em uma representação atômica só se sabe o nome da cidade onde estamos atualmente. [1]

Usada em:

- Algoritmos de busca [3]
- Processos de decisão de Markov [2]
- Modelos ocultos de Markov [2]
- Tarefas de percepção básica [3]

## Representação Fatorada

Estados são divididos em atributos e variáveis que têm um valor, descrevem um problema com uma fidelidade mais alta, no entanto a estrutura interna desses atributos e variáveis está oculta. Enquanto dois estados atômicos não têm nada em comum, pois são caixas pretas, dois estados fatorados podem ter alguns atributos compartilhados, o que ajuda a ver com maior clareza quais ações devem ser realizadas para converter um estado em outro. Um exemplo disso é revisitar o problema da rota entre duas cidades, em representação fatorada pode levar em conta coisas como os gps cordenadas, a quantidade de combustível ou o estado do motor na cidade atual. [1]

Usada em:

- Algoritmos de satisfação de restrições [2]
- Redes bayesianas [2]