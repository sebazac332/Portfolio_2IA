# Algoritmos genéticos

Algoritmos genéticos usam processos que imitam os comportamentos dos seres vivos, especificamente aqueles comportamentos relacionados com a evolução biológica como reprodução, mutação e recombinação. Para tais algoritmos as soluções mais fracas são eliminadas, enquanto as opções mais fortes e viáveis são mantidas e reavaliadas na evolução seguinte, isto a fim de chegar às ações mais ótimas para alcançar o estado desejado. A forma como isso é feito é de uma lista de indivíduos (estados) escolhe-se aqueles que têm o melhor valor e desses estados selecionados produz-se estados sucessores que serão a lista de indivíduos para a próxima geração, este último processo é conhecido como recombinação. 

Elementos importantes de estos algorimos son:

- O tamanho da população (O número de estados iniciais).
- A representação de cada indivíduo. Nos algoritmos genéticos, cada indivíduo é uma cadeia sobre um alfabeto finito (muitas vezes uma cadeia booleana).
- O número de combinação p, que é o número de estados que se combinam para criar um sucessor, o número mais comum é dois, embora existam situações em que este é maior.
- O processo de seleção que irá selecionar quais estados se tornarão pais na próxima geração, um exemplo deste processo é uma seleção aleatória, outra forma é probabilidades que sejam proporcionais ao quão adequado seu valor seja.
- O processo de recombinação, que é a forma como os estados pai se combinam para criar sucessores, uma abordagem comum é escolher aleatoriamente um ponto onde os estados pai são cortados e as duas partes resultantes são combinadas.
- A taxa de mutação, uma vez que um sucessor é gerado todos os seus bits têm uma probabilidade igual à taxa de mutação de ser virada (1 para 0/0 para 1).
- A composição da próxima geração. Duas práticas comuns são elitismo, em que não apenas sucessores, mas também pais de alto valor compõem a próxima geração; o outro é conhecido como sacrifício no qual estados com valor abaixo de um limite são eliminados.

Um esquema são estados que contêm em que algumas das posições são deixadas sem especificar, a partir destes são criadas instâncias que são estados que compartilham as posições especificadas enquanto as posições não especificadas podem variar, se o valor médio das instâncias for maior que o valor médio total, o número de instâncias do esquema aumentará. Esses esquemas são usados para que blocos úteis sejam combinados com outros blocos para chegar a uma solução.