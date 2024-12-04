# Problemas de malha aberta e de malha fechada

Os problemas que um agente IA enfrenta são influenciados por múltiplas circunstâncias do ambiente, estes podem ser classificados em dois tipos de problemas de malha aberta e problemas de malha fechada.

## Problemas de malha aberta

Ocorrem em ambientes totalmente observáveis e determinísticos, o agente realiza ações predefinidas sem nenhum tipo de feedback contínuo, comandos fixos são executados sem ajustes durante a execução. Neste tipo de ambientes a resolução do problema será sempre uma sequência de ações fixas.

### Vantagens

- Desenho e implementação simples.
- Baixo custo de manutenção.
- Alta velocidade de operação.

### Desvantagens

- Baixa precisão e exatidão.
- Vulnerável a variações externas.

## Problemas de malha fechada

Ocorrem em ambientes não-determinísticos ou que possam possuir informações que só são reveladas durante a execução, o agente baseará suas ações no feedback constante obtido através de sensores e atuadores, as ações serão monitoradas constantemente e ajustes em tempo real serão feitos para garantir que o objetivo seja alcançado.

### Vantagens

- Alta precisão e exatidão.
- Resistente a variações externas.

### Desvantagens

- Desenho e implementação complexa.
- Alto custo de manutenção
- Menor velocidade de operação em comparação com agentes projetados para problemas de malha aberta.
