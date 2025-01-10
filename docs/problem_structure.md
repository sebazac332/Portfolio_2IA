# Estrutura de problemas

Quando se trata de resolver problemas de satisfação de condições, a situação ideal é que este seja em forma de arvore, pois são mais fáceis de resolver porque evitam os ciclos, duas variáveis quaisquer estão conectadas por um único caminho e estes podem ser resolvidos em tempo linear O(nd<sup>2</sup>) se a consistência do arco dirigido é assegurada. Um CSP é definido como consistente em arco direcional consistente em arco direcional sob uma ordenação de variáveis X1, X2, . . . ,Xn se e somente se cada Xi for arco-consistente com cada Xj para j > i. Além disso, já temos um algoritmo bastante confiável para resolver esses tipos de problemas. [1]

- **Etapa 1:** Selecione uma variável raiz e faça uma classificação topológica das variáveis com base na estrutura da árvore. [1]
- **Etapa 2:** tornar o gráfico consistente com o arco direcionado em O(nd<sup>2</sup>). [1]
- **Etapa 3:** Atribua valores às variáveis linearmente na lista ordenada sem retrocesso, pois a consistência do arco garante atribuições válidas para os filhos, dadas as atribuições dos pais. [1]

Agora que temos um algoritmo eficiente para árvores, podemos considerar se os gráficos de restrições mais gerais podem ser reduzidos a árvores de alguma forma. Há duas maneiras de fazer isso: removendo os nós ou colapsando os nós. [1]

## Condicionamento de corte

O condicionamento de conjunto de cortes é uma técnica para resolver CSPs quase estruturados em árvore em que algumas variáveis são atribuídas separadamente do restante, removidas do gráfico de restrições e deixando um CSP estruturado em árvore para as variáveis restantes. [9]

Os conjuntos de cortes são alguns conjuntos de variáveis que são cortados (cortando bordas) do gráfico de restrições original e resolvidos separadamente. [9]

O condicionamento é o processo de atribuir um valor a alguma variável em um conjunto de corte, realizar a verificação progressiva em seus domínios vizinhos antes do corte e, por fim, separá-lo do gráfico original. [9]

**Etapas:**

- **Etapa 1:** Escolha algum(ns) conjunto(s) de corte de variáveis que deixe(m) um gráfico restante estruturado em árvore. [9]

- **Etapa 2:** Na forma tradicional de backtracking, condicione o conjunto de corte. [9]

- **Etapa 3:** Resolva o CSP estruturado em árvore restante. [9]

## Decomposição de árvores

Ideia básica da decomposição de árvore:

- Decompor a rede de restrições em subproblemas menores (sobrepostos). [10]
- Encontrar soluções para os subproblemas. [10]
- Criar uma solução geral com base nas subsoluções. [10]

**Requisitos:**

- Cada variável do problema original aparece em pelo menos um dos nós da árvore. [1]
- Se duas variáveis estiverem conectadas por uma restrição no problema original, elas devem aparecer juntas (junto com a restrição) em pelo menos um dos nós da árvore. [1]
- Se uma variável aparecer em dois nós da árvore, ela deverá aparecer em cada nó ao longo do caminho que conecta esses nós. [1]

Quando tivermos um gráfico estruturado em árvore, poderemos aplicar o TREE-CSP-SOLVER para obter uma solução em tempo O(nd<sup>2</sup>), em que n é o número de nós da árvore e d é o tamanho do maior domínio.