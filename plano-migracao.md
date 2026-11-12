# Collab Agêntica: plano de migração (RASCUNHO N1)

Status: rascunho para aprovação do Sam. Nada foi cadastrado nem executado.
Base: arquivo `rotinas.md` (9 rotinas, 4 fases) e política de governança.

## 1. Estratégico

| Objetivo | Critério de sucesso |
|---|---|
| Tirar a operação recorrente do manual e colocar em tarefas agendadas | Rotinas da Fase 1 rodando por 2 semanas sem incidente |
| Manter controle total do Sam | Zero ação em linha vermelha sem OK explícito |
| Custo previsível | Consumo do plano medido antes de ligar a fase seguinte |

Princípio: começar pequeno, medir, só então ampliar.

## 2. Tático: fases

| Fase | Rotinas | Agente | Modelo | Autonomia inicial |
|---|---|---|---|---|
| 0 Preparação | Base "Log Collab Agêntica" no Notion, arquivos dos 6 agentes, modelo de incidente | todos | n/a | n/a |
| 1 Núcleo | Resumo do dia, Alertas do Trello, Auditoria semanal (sexta) | chefe-de-gabinete, auditor | Haiku | N0 (ler e alertar) |
| 1b Fila | Leitura da fila de pedidos (só após 2 semanas da Fase 1) | chefe-de-gabinete | Haiku | N1 |
| 2 Social | Checagem das redes, Relatório de métricas, Benchmark mensal | social-metricas, inteligencia | Haiku e Sonnet | N0 e N1 |
| 3 Comercial | Higiene do CRM | sdr-comercial | Haiku | N0 |
| 4 Site | Saúde do site e GMB | site | Sonnet | N0 |

Intervalo mínimo entre fases: 2 semanas de medição de consumo e 0 incidente.

## 3. Operacional: passo a passo

1. Criar a base "Log Collab Agêntica" no Notion (data e hora, quem pediu, agente, ação, dados usados, resultado, pendência)
2. Escrever o arquivo de cada agente com nível de autonomia, modelo e limites
3. Cadastrar as rotinas da Fase 1, uma por vez, após OK do Sam
4. Toda execução grava no log
5. Falhou 2 vezes seguidas: rotina pausa e vira incidente (skill `relatorio-incidente`)
6. Dia 14: relatório de consumo e erros. Sam decide a Fase 2
7. Promoção de nível: só após 30 dias sem erro na tarefa, decisão do Sam

## 4. Pontos que precisam de decisão

| # | Ponto | Por que importa |
|---|---|---|
| 1 | A Fase 1 tem 4 rotinas, mas a regra diz começar com 2 ou 3 | Sugestão: Resumo do dia, Alertas do Trello e Auditoria na Fase 1. Fila de pedidos entra depois |
| 2 | Entrega via Telegram não está na lista de ferramentas da política | Aprovar o Telegram e confirmar que não sai dado confidencial por ali |
| 3 | Frequência da fila de pedidos (2h, 4h ou 3x ao dia) | Impacta consumo. Sugestão: 3x ao dia no início |
| 4 | Entrega de resumo e alertas pode citar dados de cliente | Dado confidencial não pode sair. Definir que resumos usam só nome do card, sem valores |
| 5 | Os arquivos dos agentes não existem neste repositório | Preciso do conteúdo ou aprovação para criar do zero |

## 5. Riscos

| Risco | Mitigação |
|---|---|
| Estouro de consumo do plano | Começar com 3 rotinas Haiku e medir |
| Vazamento de dado de cliente por canal externo | Regra do ponto 4 e revisão na auditoria de sexta |
| Rotina com falha silenciosa | Log obrigatório e pausa após 2 falhas |

## Próximo passo

Sam responde os 5 pontos da seção 4. Depois disso, crio a base de log e os arquivos dos agentes como rascunho, e só cadastro as rotinas da Fase 1 com o OK de fase.
