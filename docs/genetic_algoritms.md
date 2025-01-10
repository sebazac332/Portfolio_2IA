# Algoritmos genéticos

Algoritmos genéticos usam processos que imitam os comportamentos dos seres vivos, especificamente aqueles comportamentos relacionados com a evolução biológica como reprodução, mutação e recombinação. [13] Para tais algoritmos as soluções mais fracas são eliminadas, enquanto as opções mais fortes e viáveis são mantidas e reavaliadas na evolução seguinte, isto a fim de chegar às ações mais ótimas para alcançar o estado desejado. [13] A forma como isso é feito é de uma lista de indivíduos (estados) escolhe-se aqueles que têm o melhor valor e desses estados selecionados produz-se estados sucessores que serão a lista de indivíduos para a próxima geração, este último processo é conhecido como recombinação. [5]

Elementos importantes de estos algorimos son:

- O tamanho da população (O número de estados iniciais). [5]
- A representação de cada indivíduo. Nos algoritmos genéticos, cada indivíduo é uma cadeia sobre um alfabeto finito (muitas vezes uma cadeia booleana). [5]
- O número de combinação p, que é o número de estados que se combinam para criar um sucessor, o número mais comum é dois, embora existam situações em que este é maior. [5]
- O processo de seleção que irá selecionar quais estados se tornarão pais na próxima geração, um exemplo deste processo é uma seleção aleatória, outra forma é probabilidades que sejam proporcionais ao quão adequado seu valor seja. [5]
- O processo de recombinação, que é a forma como os estados pai se combinam para criar sucessores, uma abordagem comum é escolher aleatoriamente um ponto onde os estados pai são cortados e as duas partes resultantes são combinadas. [5]
- A taxa de mutação, uma vez que um sucessor é gerado todos os seus bits têm uma probabilidade igual à taxa de mutação de ser virada (1 para 0/0 para 1). [5]
- A composição da próxima geração. Duas práticas comuns são elitismo, em que não apenas sucessores, mas também pais de alto valor compõem a próxima geração; o outro é conhecido como sacrifício no qual estados com valor abaixo de um limite são eliminados. [5]

Um esquema são estados que contêm em que algumas das posições são deixadas sem especificar, a partir destes são criadas instâncias que são estados que compartilham as posições especificadas enquanto as posições não especificadas podem variar, se o valor médio das instâncias for maior que o valor médio total, o número de instâncias do esquema aumentará. Esses esquemas são usados para que blocos úteis sejam combinados com outros blocos para chegar a uma solução. [5]

## Exemplo de implementação de algoritmos genéticos

Exemplo básico de algoritmos genéticos em que se tenta encontrar os valores de x, y e z que farão com que o resultado de uma função específica seja o mais próximo possível de zero. Neste algoritmo, a combinação e mutação são implementadas.

```python

import random

def foo(x, y, z):
    return 6*x**3 + 9*y**2 + 90*z - 25

def fitness(x, y, z):
    ans = foo(x, y, z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
solutions = []
for s in range(1000):
    solutions.append((random.uniform(0,10000),
                      random.uniform(0,10000),
                      random.uniform(0,10000)))
    
for i in range(10000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0],s[0],s[0]),s))
    rankedsolutions.sort
    rankedsolutions.reverse

    print(f"=== Gen {i} best solutions ===")
    print(rankedsolutions[0])

    if rankedsolutions[0][0] > 999:
        break

    bestsolutions = rankedsolutions[:100]

    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
    
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)

        newGen.append((e1, e2, e3))

    solutions = newGen

```