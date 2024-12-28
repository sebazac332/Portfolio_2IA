# Busca em ambientes complexos

## Busca local

São usados em problemas onde o caminho para a solução não importa, apenas o estado objetivo é importante. Eles buscam começando de um estado inicial para seus vizinhos sem guardar o caminho percorrido ou os estados alcançados, isso significa que não são sistemáticos pois existe a probabilidade de nunca explorarem a porção do espaço de busca onde está a solução. Tem duas vantagens principais, usam pouca memória e podem encontrar soluções razoáveis em espaços infinitos onde algoritmos sistemáticos não funcionam.

## Escalada

Algoritmo que se baseia em escolher sempre o estado que tem maior ou menor valor dependendo do que é necessário, isto faz-o mantendo um registo de um estado específico e em cada iteração movendo-se a um vizinho deste estado que possua o maior/menor valor. A execução termina quando não é possível encontrar um estado com um valor maior/menor que o acutual. Este algoritmo não é capaz de olhar mais além dos vizinhos do estado atual.

Existem algumas situações em que este algoritmo fica preso, estes são:

- **Local maxima:** Estado que possui um valor maior do que todos os seus vizinhos, mas menor do que o valor máximo global.
- **Cristas:** Sequência de local maxima que é muito difícil navegar para o algoritmo.
- **Planaltos:** Área completamente plana no espaço de busca, onde não há valores maiores ou menores, pode ser de dois tipos local máximo plano onde não há forma de prosegir ou um ombro, em que eventualmente se pode conseguir sair e continuar com a busca.

### Variações de Escalada

- **Escalada estocástica:** Escolhe aleatoriamente entre os movimentos de subida.
- **Escalada em colina de primeira escolha:** Implementa o hill climbing estocástico gerando sucessores aleatoriamente até que seja gerado um que seja melhor do que o estado atual.
- **Escalada em colina com reinício aleatório:** Realiza uma série de pesquisas de hill climbing a partir de estados iniciais gerados aleatoriamente, até que um objetivo seja encontrado.

## Recozimento simulado

Uma das fraquezas do algoritmo de escalada é que ele nunca se moverá para um estado que tenha um valor menor/maior mesmo que este seja um movimento necessário para obter o melhor resultado, para lidar com essa fraqueza pode combinar o algoritmo de escalada com uma funcionalidade de aleatoriedade resultando no algoritmo de Recozimento simulado. Neste algoritmo não se escolhe o melhor estado imediatamente, mas um movimento aleatório é realizado, se este melhora a situação (valor maior/menor que o atual) sempre se escolhe, caso contrário o algoritmo aceitará o movimento com uma probabilidade menor a um, isto irá diminuir dependendo de tanto este movimento piora a situação e segundo uma variável conhecida como temperatura (T), que começa com um valor alto e vai diminuindo ao longo do tempo, quanto maior o valor de T mais provável é que se escolha movimentos "ruins".

## Busca de feixe local

Busca local onde em vez de manter um estado, mantém k estados simultaneamente. Preenche-se com k estados gerados aleatoriamente e por cada passo são gerados todos os sucessores de todos os estados, se entre eles estiver o estado alvo a execução termina, se não se escolhem aqueles que têm os melhores valores. Neste algoritmo, as informações são compartilhadas entre todos os busques que são executados em paralelo e se um deles tiver melhores resultados, os outros tentarão chegar à área onde ele está. Isso pode gerar alguns problemas, pois existe a possibilidade de que os busques fiquem todos juntos em uma única área o que faz com que o algoritmo perca eficácia. Para aliviar isso uma variante conhecida como busca de feixe estocástico pode ser usada, onde em vez de escolher os melhores valores é escolhido imediatamente com uma probabilidade que aumenta em relação ao valor.

## Busca local em espaços contínuos

Uma forma de lidar com esses ambientes é discretizá-los, isto é, encontrar a maneira de obter um número limitado de pontos fixos no ambiente contínuo, Uma maneira de fazer isso é dividir o espaço em uma grade retangular com espaçamento k constante e escolher os pontos na grade. Uma vez feito isso, se pode usar qualquer um dos algoritmos de busca local vistos anteriormente.

Alternativamente, poderíamos fazer o fator de ramificação ser finito amostrando estados sucessores aleatoriamente, movendo-nos em uma direção aleatória em uma pequena quantidade, δ. Os métodos que medem o progresso pela mudança no valor da função objetivo entre dois pontos próximos são chamados métodos de gradiente empírico. A busca de gradiente empírico é o mesmo a escalada mais íngreme em uma versão discretizada do espaço de estado.

## Busca com ações não determinísticas

Em ambientes parcialmente observáveis, o agente não sabe em que estado se encontra e, em ambientes não determinísticos, o agente não sabe para qual estado se desloca quando uma ação específica é executada. Por isso, nesses ambientes, é feito uso de estados de crença que são um conjunto de estados que o agente acredita serem possíveis, também a solução do problema não será uma sequência de ações, mas um plano condicional que dirá ao agente quais ações tomar dependendo do que ele receber durante a execução desse plano.

Para encontrar soluções nesses ambientes, são usados arvores de busca e busca, que contêm dois tipos especiais de nós. O primeiro tipo são os nós or que representam as ações escolhidas pelo agente, o segundo time são os nós and que representam como o ambiente reage a essas escolhas, geralmente para nós or deve ser feita uma seleção de qual estado considerar enquanto que para nós and devem ser levados em consideração todos os estados resultantes. Neste tipo de árvores de busca é muito comum que ocorram ciclos, para contrarestar estes se faz uma verificação, se o estado atual for igual a um estado pertencente ao caminho desde o nó raiz, se este for o caso, uma mensagem de falha é retornada, o que significa que existe uma solução não cíclica que deveria ser atingida desde uma encarnação anterior desse estado, e então a nova encarnação pode ser descartada.

Uma solução cíclica é aquela que pode ser encontrada repetindo uma determinada ação até alcançar o estado desejado. Uma condição mínima para que isso funcione é que cada folha (nó que não possua sucessores) seja um alvo e que pelo menos uma folha possa ser atingida a partir de qualquer ponto do plano. Outro ponto a considerar é a causa do não determinismo, se este for devido a algum fato não observado do agente ou ambiente repetir a ação não ajudará.

## Busca sem observações

Em tais situações o agente deve procurar no espaço de crença, que é o conjunto de todos os estados possíveis, Depois disso, o agente deve realizar ações determinísticas que refinam esse espaço de crença diminuindo o número de estados possíveis para tentar chegar ao estado-alvo. Este tipo de busca tem componentes que são:

- **Estados:** O espaço de estado de crença contém todos os subconjuntos possíveis dos estados físicos. Se P tiver N estados, o problema de estado de crença terá 2<sup>N</sup> estados de crença, embora muitos deles possam ser inalcançáveis a partir do estado inicial.
- **Estado inicial:** Normalmente, o estado de crença que consiste em todos os estados em P, embora em alguns casos o agente tenha mais conhecimento do que isso.
- **Ações:** Se for assumido que as ações ilegais não têm efeito no ambiente, todas as ações possíveis podem ser realizadas para todos os estados físicos no estado atual de crença; Pelo contrário, se as ações ilegais poderiam ser catastróficas, só é seguro realizar apenas o conjunto de ações legais para todos os estados físicos atuais.
- **Modelo de transição:** Para ações determinísticas, o novo estado de crença tem um estado de resultado para cada um dos estados possíveis atuais, com o não determinismo, o novo estado de crença consiste em todos os resultados possíveis da aplicação da
a ação a qualquer um dos estados no estado de crença atual.
- **Teste de objetivo:** O agente possivelmente encontrou o alvo se algum estado no espaço de crença satisfaz a teste de objetivo; o agente definitivamente encontrou o alvo se todos os estados no espaço de crença passaram no teste.
- **Custo de ação:** Se a mesma ação pode ter custos diferentes em diferentes estados, então o custo de realizar uma ação em um determinado estado de crença poderia ser um dos vários valores.

## Busca online

Algoritmos de busca online são aqueles que tomam uma ação e esperam para ver como o ambiente reage antes de realizar a próxima ação, isso ao contrário dos algoritmos de busca offline em que se calcula a solução completa antes de tomar o primeiro passo, a maioria dos algoritmos vistos são de busca offline.

As coisas que o agente sabe neste tipo de busca são limitadas, estas são:

- **ACTIONS(s)**, as ações legais no estado s;
- **c(s,a, s′)**, o custo de aplicar a ação a no estado s para chegar ao estado s′. Observe que isso não pode ser usado até que o agente saiba que s′ é o resultado.
- **IS-GOAL(s)**, o teste de meta.

Uma das principais vulnerabilidades desses busques são os becos sem saída, que são estados em que é possível chegar a uma solução, isto é especialmente difícil em explorações, em que certos objetos do terreno como rampas ou penhascos resultam em ações irreversíveis, que é quando não é possível voltar a um estado anterior.

Uma forma de medir a eficácia do algoritmo de busca on-line é através da relação competitiva que é a diferença entre o custo da solução encontrada por meio de pesquisa on-line e o custo da solução se o agente conhecesse o espaço de busca com antecedência, Idealmente, esse valor deve ser o menor possível.

Algoritmos de busca on-line funcionam muito diferente dos algoritmos de busca offline, agentes on-line recebem informações após cada ação que lhes diz em qual estado ele chegou, esta informação é usada para atualizar seu mapa do ambiente e planejar sua próxima ação. Isso significa que em algoritmos on-line você só pode explorar o espaço de busca tomando ações reais, enquanto em algoritmos off-line o espaço de busca pode ser explorado por simulações.

Para fazer buscas em espaços online busca de escalada não é suficiente pois pode deixar o agente preso em um local máximo. Para usar esse algoritmo, aumentar a escalada com memória em vez de aleatoriedade é uma abordagem mais eficaz. A ideia básica é armazenar uma «melhor estimativa atual» H(s) do custo de atingir o objetivo de cada estado visitado. H(s) começa sendo apenas a estimativa heurística
h(s) e é atualizado à medida que o agente ganha experiência no espaço de estados. 

Um agente que implemente esse esquema, chamado de aprendizado em tempo real A* (LRTA*) constrói um mapa do ambiente na tabela de resultados. Atualiza a estimativa de custo para o estado que se acabou de abandonar e, em seguida, escolhe o movimento «aparentemente melhor» com base nas estimativas de custos atuais. Um detalhe importante é que sempre se supõe que as ações que ainda não foram tentadas em um estado s conduzem imediatamente ao objetivo com o menor custo possível, isto é, h(s). No pior dos casos, esse agente é capaz de explorar um ambiente com n estados em O(n<sup>2</sup>) passos, embora na maioria dos casos ele costuma ter melhor desempenho.

Para aprender os agentes de busca online realizam duas etapas, primeiro você deve criar um mapa do ambiente, que será formado por todos os resultados de todas as ações em cada estado, o segundo passo é obter estimativas mais precisas do custo de cada estado usando normas locais de atualização.