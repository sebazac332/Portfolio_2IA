# Agente de soluções de problemas

(geeksforgeeks e skillvertex - Hridhya Manoj)
São um tipo de agente projetado para perceber seu ambiente e agir para atingir um objetivo, ao contrário de um agente reflexo que só reage a estímulos, um agente de solução de problemas é especializado em identificar e resolver situações sistematicamente. Alguns usos para esses agentes são encontrados em algoritmos de jogo, robótica e sistemas de tomada de decisão.

## Características

- **Percepção:** Têm a capacidade de obter informação do seu ambiente.
- **Raciocínio:** Capacidade de processar informações, fazer inferências e decidir quais são as ações mais adequadas baseadas na percepção e no conhecimento prévio.
- **Planejamento:** Consideração de múltiplas sequências de ações para atingir objetivos, geralmente usado para problemas complexos.
- **Feedback:** Capacidade de receber feedback do ambiente que eles usam para ajustar suas ações e estratégias.
- **Aprendizagem:** Incorporam estratégias de aprendizado de máquina para melhorar seu desempenho ao longo do tempo.

## Passos para resolução de problemas

1. **Definição do problema:** Nesta primeira fase, deve-se especificar claramente quais são as possíveis situações e soluções aceitáveis para o sistema.
2. **Análise de problema:** Nesta fase, os componentes e restrições do problema são cuidadosamente analisados, verificando quais soluções são viáveis.
3. **Representação do conhecimento:** Nesta fase, todas as informações obtidas sobre o problema são coletadas para definir quais técnicas podem ser usadas.
4. **Resolução do problema:** As melhores técnicas para a solução do problema são coletadas e comparadas para determinar qual é o melhor método.

## Componentes

- **Estado inicial:** Estado inicial para o agente, estabelecendo o contexto do problema, aqui também inicializam-se os métodos para a resolução de problemas.
- **Ação:** Aqui é onde todas as ações possíveis são identificadas com base no estado inicial.
- **Transição:** Verifica como as ações afetam o estado do problema e leva-o para a próxima fase do processo de solução.
- **Teste de objetivo:** Verifica se o estado alvo foi alcançado usando o módulo de transição, se este é o caso, interrompe as ações e se concentra em calcular o custo para atingir esse objetivo.
- **Custo de trajeto:** Este componente atribui um valor numérico à solução alcançada, leva em conta o uso de hardware, software e recursos humanos.

## Dificuldades

- **Complexidade:** Problemas complexos exigem uma grande quantidade de tempo e recursos computacionais.
- **Qualidade de dados:** A qualidade das soluções é muito dependente da qualidade dos dados que são fornecidos ao sistema.
- **Interpretabilidade:** Vários modelos de IA atuam como "caixas pretas" o que impede a compreensão do seu processo de tomada de decisão.
- **Ética e preconceito:** Preconceitos encontrados na data podem ser refletidos no agente o que pode alterar a qualidade das soluções.