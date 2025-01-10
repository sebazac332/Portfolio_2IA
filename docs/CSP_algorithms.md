# Algoritmos de satisfação de condições

## Algoritmo AC-3

O algoritmo mais popular para reforçar a consistência do arco é chamado AC-3. Para tornar cada variável consistente com o arco, o algoritmo AC-3 mantém uma fila de arcos a serem considerados. Inicialmente, a fila contém todos os arcos do CSP. (Cada restrição binária se transforma em dois arcos, um em cada direção.) Em seguida, o AC-3 retira um arco arbitrário (Xi,Xj) da fila e torna Xi consistente com o arco em relação a Xj. Se isso deixar Di inalterado, o algoritmo simplesmente passa para o próximo arco. Mas se isso revisar Di (tornar o domínio menor), adicionaremos à fila todos os arcos (Xk,Xi) em que Xk é um vizinho de Xi. Precisamos fazer isso porque a alteração em Di pode permitir mais reduções em Dk, mesmo que tenhamos considerado Xk anteriormente. Se Di for revisado para zero, saberemos que todo o CSP não tem solução consistente e o AC-3 pode retornar imediatamente uma falha. Caso contrário, continuaremos a verificação, tentando remover valores dos domínios das variáveis até que não haja mais arcos na fila. [1]

## Algoritmo de retrocesso

O algoritmo de backtracking é um método de busca em profundidade usado para explorar sistematicamente as possíveis soluções em CSPs. Ele opera atribuindo valores a variáveis e retrocede se alguma atribuição violar uma restrição. [5]

**Funcionamento:**

- O algoritmo seleciona uma variável e atribui a ela um valor. [5]
- Ele atribui valores recursivamente às variáveis subsequentes. [5]
- Se surgir um conflito (ou seja, não for possível atribuir um valor válido a uma variável), o algoritmo volta à variável anterior e tenta um valor diferente. [5]
- O processo continua até que uma solução válida seja encontrada ou todas as possibilidades tenham sido esgotadas. [5]

Esse método é amplamente usado devido à sua simplicidade, mas pode ser ineficiente para problemas grandes com muitas variáveis. [5]


## Algoritmo de verificação progressiva

O algoritmo de verificação de avanço é um aprimoramento do algoritmo de retrocesso que visa reduzir o espaço de pesquisa aplicando verificações de consistência local. [5]

**Funcionamento:**

- Para cada variável não atribuída, o algoritmo mantém o controle dos valores válidos restantes. [5]
- Quando um valor é atribuído a uma variável, as restrições locais são aplicadas às variáveis vizinhas, eliminando os valores inconsistentes de seus domínios. [5]
- Se um vizinho não tiver mais valores válidos após a verificação de encaminhamento, o algoritmo retrocede. [5]

Esse método é mais eficiente do que o backtracking puro porque evita alguns conflitos antes que eles ocorram, reduzindo cálculos desnecessários. [5]

## Algoritmos de propagação de restrições

Os algoritmos de propagação de restrições reduzem ainda mais o espaço de pesquisa ao impor a consistência local em todas as variáveis. [5]

**Funcionamento:**

- As restrições são propagadas entre variáveis relacionadas. [5]
- Os valores inconsistentes são eliminados dos domínios das variáveis, aproveitando as informações obtidas de outras variáveis. [5]
- Esses algoritmos refinam o espaço de pesquisa fazendo inferências, removendo valores que levariam a conflitos. [5]

A propagação de restrições é comumente usada em conjunto com outros algoritmos de CSP, como o backtracking, para aumentar a eficiência ao restringir o espaço de solução no início do processo de pesquisa. [5]

## Exemplo de implementação de algoritmos de satisfação de condições

Exemplo de algoritmo de backtraking em que se tenta resolver um labirinto, no qual está presa uma ratazana. Este labirinto é representado por uma matriz de tamanho n x n onde 1 são espaços onde o rato pode passar e 0 são espaços bloqueados. O rato é colocado na posição (0, 0) e deve chegar à posição (n-1, n-1). No caso de o rato acabar em uma posição sem saída, ele deve ser capaz de voltar e tentar outro caminho.

```python

class Solution:
    def findPath(self, mat):
        
        n = len(mat)
        visited = set()
        paths = []
        
        def dfs(row, col, path):
            if (row == n-1) and (col==n-1):
                paths.append(''.join(path))
                return
            
            if row < 0 or row >= n or col < 0 or col >= n or mat[row][col] != 1 or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col, path + ['D']) 
            dfs(row, col - 1, path + ['L']) 
            dfs(row - 1, col, path + ['U'])
            dfs(row, col + 1, path + ['R']) 

            
            visited.remove((row, col))
                    
        dfs(0,0,[])
        return sorted(paths)

solution = Solution()
matrix = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
result = solution.findPath(matrix)
print(result)

```