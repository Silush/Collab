# Telegram: porta-voz da Collab Agêntica (rascunho N1)

Substitui o Fox da Torre. A função passa para o **Gandalf** (chefe-de-gabinete).

## Decisões do Sam (12/11/2026)

| Tema | Decisão |
|---|---|
| Destino | Grupo "Collab Gestão" |
| Bot | Novo, criado pelo Sam no BotFather, nome "Gandalf Collab" |
| Torre | Desligada de vez. A rotina do Fox sai com ela |
| Formato | Organizado, com quebra de linha, títulos em negrito e listas. Nada bagunçado |

## O que vai e o que não vai

| Vai | Não vai |
|---|---|
| Resumo do dia | Valores financeiros |
| Alertas do Trello (prazo vencido, aprovação pendente) | Nome de cliente |
| Pendências que precisam de decisão do Sam | Nome de lead |
| Entregas concluídas e marcos | Dados pessoais |
| Falhas de rotina (incidente) | Qualquer coisa de classe Confidencial |

O grupo pode ter outras pessoas. Por isso, no grupo só vai o que é Interno ou Público. Leads aparecem só em quantidade (exemplo: "5 leads aguardando decisão").

## Formato da mensagem

O Telegram não renderiza Markdown completo. Usar o modo HTML do Telegram: `<b>` para título, `<i>` para destaque leve, `•` para lista, linha em branco entre blocos. Máximo de 15 linhas.

Modelo:

```
<b>Resumo do dia · 12/11</b>

<b>Precisa de você</b>
• Aprovar pauta da semana (Trello)
• 5 leads aguardando decisão

<b>Hoje</b>
• 08:30 LinkedIn @collabgestao
• 19:30 Instagram @samoraleal

<b>Alertas</b>
• 1 post sem arte para 17/11

<b>Próximo passo:</b> aprovar a pauta.
```

Regras: português do Brasil, sem travessão, sempre terminar com o próximo passo.

## Como funciona

1. O Gandalf (ou outro agente, via Gandalf) grava o aviso na base "Fila de avisos" no Notion (campos: data e hora, agente, texto, status fila, enviado em).
2. Uma rotina no Mac lê a fila, envia ao grupo pelo bot e marca como enviado.
3. Cada envio gera uma linha no log "Log Collab Agêntica".
4. Rotina que falha 2 vezes seguidas pausa e vira incidente.

Por que no Mac: o Telegram exige o token no endereço da chamada. O token fica só no Mac, em arquivo local fora do repositório. Nunca no chat, no Notion, no Drive ou no repositório.

## Como o Sam cria o bot (5 minutos)

1. No Telegram, abra a conversa com **@BotFather**
2. Envie `/newbot`
3. Nome: `Gandalf Collab`
4. Usuário: precisa terminar em `bot`, exemplo `gandalf_collab_bot` (se estiver ocupado, tente outro)
5. O BotFather devolve um **token**. Não cole em nenhum lugar fora do Mac
6. Abra o grupo "Collab Gestão", adicione o bot como membro
7. Avise "bot criado". O cadastro do token e do grupo é feito no Mac

## Onde cada coisa roda hoje

| Rotina | Máquina |
|---|---|
| SDR Instagram, Threads, Fox (Torre) | MacBook do Sam |
| Clara SDR WhatsApp | PC Windows (WhatsApp Business no Chrome) |
| Blog, pauta, métricas, ajustes do cockpit | Nuvem (com Mac para navegador quando preciso) |

## Fase 2: pedir trabalho pelo Telegram

Duas opções, a decidir depois da fase 1:
- Ler as mensagens do bot dentro da rotina da fila (3x ao dia)
- Plugin de canal do Claude Code (resposta mais rápida, mas exige sessão aberta no Mac)

Mensagem recebida pelo Telegram nunca vira aprovação automática de e-mail, contrato, post ou envio a cliente.
