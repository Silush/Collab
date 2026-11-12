#!/usr/bin/env bash
# Envia uma mensagem (HTML do Telegram) ao grupo Collab Gestão.
# Uso: printf '<b>Titulo</b>\n• item' | scripts/telegram-enviar.sh
# O token e o ID do grupo ficam SÓ em ~/.collab/telegram.env (fora do repositório).
set -euo pipefail

ENV_FILE="${COLLAB_TELEGRAM_ENV:-$HOME/.collab/telegram.env}"
[ -f "$ENV_FILE" ] || { echo "arquivo $ENV_FILE nao encontrado" >&2; exit 1; }
# shellcheck disable=SC1090
source "$ENV_FILE"
: "${TELEGRAM_TOKEN:?token ausente}"
: "${TELEGRAM_CHAT_ID:?id do grupo ausente}"

TEXTO="$(cat)"
[ -n "$TEXTO" ] || { echo "texto vazio" >&2; exit 1; }
[ "${#TEXTO}" -le 4000 ] || { echo "texto acima de 4000 caracteres" >&2; exit 1; }

RESP="$(curl -sS -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
  -d chat_id="$TELEGRAM_CHAT_ID" -d parse_mode=HTML -d disable_web_page_preview=true \
  --data-urlencode text="$TEXTO")"

case "$RESP" in
  *'"ok":true'*) echo "enviado" ;;
  *) echo "falhou: $(printf '%s' "$RESP" | sed -E 's/[0-9]{8,}:[A-Za-z0-9_-]{30,}/[TOKEN]/g')" >&2; exit 1 ;;
esac
