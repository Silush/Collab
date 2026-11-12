# Rotinas da Collab Agêntica (revisado em 12/11/2026)

Cada rotina vira tarefa agendada, cadastrada só após aprovação da fase. A Torre foi descontinuada.

| Rotina | Frequência | Agente | Modelo | Entrega | Etapa |
|---|---|---|---|---|---|
| Resumo do dia (no lugar da Torre) | Dias úteis, 7h | chefe-de-gabinete | Haiku | App Claude e Telegram | 1 |
| Alertas do Trello | A cada 4h em horário comercial | chefe-de-gabinete | Haiku | App Claude e Telegram | 1 |
| Auditoria semanal | Sexta, 17h | auditor | Haiku | Notion e aviso | 1 |
| Leitura da fila de pedidos | 3x ao dia (ajustável) | chefe-de-gabinete | Haiku | Distribui aos agentes | 2 |
| Pauta mensal | Mensal | copy | Sonnet | Trello, para aprovação | 2 |
| Checagem das redes | 2x ao dia (9h e 17h) | social-metricas | Haiku | App Claude | 2 |
| Relatório de métricas | Segunda, 8h | social-metricas | Sonnet | Notion e aviso | 2 |
| Benchmark e referências | Mensal, junto com a pauta | inteligencia | Sonnet | Notion | 4 |
| Higiene do CRM | Dias úteis, 8h | crm-jornada | Haiku | App Claude | 3 |
| Saúde do site e GMB | Mensal | site | Sonnet | Notion | 4 |

## Regras
- Começar com 2 ou 3 rotinas e medir o consumo do plano por 2 semanas antes de ligar as próximas
- Toda rotina registra execução no log
- Rotina que falhar 2 vezes seguidas é pausada e vira incidente
- Pedidos extras o Sam faz manualmente, a qualquer hora
- Resumo e alertas usam só o necessário. Dado confidencial de cliente não vai para o Telegram

## Ponto técnico em aberto
O envio pelo Telegram precisa ser implementado. Hoje não há conector dele nesta sessão.
