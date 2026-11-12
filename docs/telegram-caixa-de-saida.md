# Plano B do Telegram: caixa de saída (rascunho, usar só se a rede do agente continuar bloqueando)

## Ideia
O agente não fala com o Telegram. Ele só **escreve** a mensagem num arquivo. Um agendador do próprio Mac (launchd) envia, fora do sandbox de rede do agente, e arquiva.

## Pastas no Mac (`~/.collab/`)
| Pasta | Uso |
|---|---|
| `saida/` | Mensagens à espera de envio (`AAAAMMDD-HHMMSS-nome.html`) |
| `enviadas/` | Mensagens já enviadas (arquivo, nada é apagado) |
| `falhas/` | Mensagens com 2 falhas seguidas. Cada uma vira incidente |
| `despacho.log` | Linha por envio ou falha |

## Instalação (uma vez)

1. Copiar o despachante e dar permissão (a partir da pasta do projeto):

```bash
cp ~/Collab/scripts/telegram-despachar.sh ~/.collab/telegram-despachar.sh && chmod +x ~/.collab/telegram-despachar.sh && mkdir -p ~/.collab/saida ~/.collab/enviadas ~/.collab/falhas
```

2. Criar o agendador (roda a cada 60 segundos):

```bash
cat > ~/Library/LaunchAgents/com.collab.telegram-despachar.plist <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.collab.telegram-despachar</string>
  <key>ProgramArguments</key>
  <array><string>/bin/bash</string><string>/Users/samoraleal/.collab/telegram-despachar.sh</string></array>
  <key>StartInterval</key><integer>60</integer>
  <key>RunAtLoad</key><true/>
</dict>
</plist>
PLIST
```

3. Ligar:

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.collab.telegram-despachar.plist
```

4. Testar:

```bash
printf '<b>🧙 Gandalf · Teste da caixa de saída</b>\n\n• Envio pelo agendador\n\n<b>Próximo passo:</b> confirmar que chegou.' > ~/.collab/saida/teste-$(date +%Y%m%d-%H%M%S).html
```

Em até 1 minuto a mensagem deve chegar ao grupo e o arquivo deve aparecer em `enviadas/`.

Para desligar: `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.collab.telegram-despachar.plist`

## Como o Gandalf passa a enviar
Nas rotinas, trocar o passo de envio por:

```
Em vez de enviar, grave a mensagem pronta em ~/.collab/saida/AAAAMMDD-HHMMSS-<rotina>.html (HTML do Telegram, mesmo formato). O despachante do Mac envia em até 1 minuto. Registre no log "gravado na caixa de saída".
```

## Incidente
Arquivo em `falhas/` ou linha `movido para falhas` no `despacho.log`: o Faramir inclui na auditoria de sexta, e o Gandalf avisa o Sam no app Claude.

Observação: o despachante foi testado com um envio simulado (sucesso, 2 falhas e arquivamento). O envio real ao Telegram depende do `~/.collab/telegram-enviar.sh` e do `telegram.env` já testados pelo Sam.
