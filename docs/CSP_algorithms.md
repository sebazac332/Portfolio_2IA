# Algoritmos

## Algoritmo AC-3

## Algoritmo de retrocesso

O algoritmo de backtracking é um método de busca em profundidade usado para explorar sistematicamente as possíveis soluções em CSPs. Ele opera atribuindo valores a variáveis e retrocede se alguma atribuição violar uma restrição.

**Funcionamento:**

- O algoritmo seleciona uma variável e atribui a ela um valor.
- Ele atribui valores recursivamente às variáveis subsequentes.
- Se surgir um conflito (ou seja, não for possível atribuir um valor válido a uma variável), o algoritmo volta à variável anterior e tenta um valor diferente.
- O processo continua até que uma solução válida seja encontrada ou todas as possibilidades tenham sido esgotadas.

Esse método é amplamente usado devido à sua simplicidade, mas pode ser ineficiente para problemas grandes com muitas variáveis.


## Algoritmo de verificação progressiva

O algoritmo de verificação de avanço é um aprimoramento do algoritmo de retrocesso que visa reduzir o espaço de pesquisa aplicando verificações de consistência local.

**Funcionamento:**

- Para cada variável não atribuída, o algoritmo mantém o controle dos valores válidos restantes.
- Quando um valor é atribuído a uma variável, as restrições locais são aplicadas às variáveis vizinhas, eliminando os valores inconsistentes de seus domínios.
- Se um vizinho não tiver mais valores válidos após a verificação de encaminhamento, o algoritmo retrocede.

Esse método é mais eficiente do que o backtracking puro porque evita alguns conflitos antes que eles ocorram, reduzindo cálculos desnecessários.

## Algoritmos de propagação de restrições

Os algoritmos de propagação de restrições reduzem ainda mais o espaço de pesquisa ao impor a consistência local em todas as variáveis.

**Funcionamento:**

- As restrições são propagadas entre variáveis relacionadas.
- Os valores inconsistentes são eliminados dos domínios das variáveis, aproveitando as informações obtidas de outras variáveis.
- Esses algoritmos refinam o espaço de pesquisa fazendo inferências, removendo valores que levariam a conflitos.

A propagação de restrições é comumente usada em conjunto com outros algoritmos de CSP, como o backtracking, para aumentar a eficiência ao restringir o espaço de solução no início do processo de pesquisa.