#!/usr/bin/env bash
# Despacha as mensagens da caixa de saída (~/.collab/saida/*.html) ao Telegram.
# Roda pelo launchd do Mac, fora do sandbox de rede do agente.
# Nada é apagado: enviadas vão para enviadas/, com 2 falhas vão para falhas/.
set -u
BASE="${COLLAB_DIR:-$HOME/.collab}"
ENVIAR="${COLLAB_ENVIAR:-$BASE/telegram-enviar.sh}"
SAIDA="$BASE/saida"; ENVIADAS="$BASE/enviadas"; FALHAS="$BASE/falhas"; LOG="$BASE/despacho.log"
mkdir -p "$SAIDA" "$ENVIADAS" "$FALHAS"

LOCK="$BASE/.despacho.lock"
mkdir "$LOCK" 2>/dev/null || exit 0
trap 'rmdir "$LOCK"' EXIT

agora() { date '+%Y-%m-%d %H:%M:%S'; }

for f in "$SAIDA"/*.html; do
  [ -f "$f" ] || continue
  nome="$(basename "$f")"
  if "$ENVIAR" < "$f" >/dev/null 2>"$BASE/.ultimo_erro"; then
    mv "$f" "$ENVIADAS/$nome"
    rm -f "$f.tentativas"
    echo "$(agora) enviado $nome" >> "$LOG"
  else
    n=0; [ -f "$f.tentativas" ] && n="$(cat "$f.tentativas")"
    n=$((n + 1)); echo "$n" > "$f.tentativas"
    erro="$(tr '\n' ' ' < "$BASE/.ultimo_erro" | cut -c1-200)"
    echo "$(agora) falha $n $nome $erro" >> "$LOG"
    if [ "$n" -ge 2 ]; then
      mv "$f" "$FALHAS/$nome"; mv "$f.tentativas" "$FALHAS/$nome.tentativas"
      echo "$(agora) movido para falhas $nome (2 falhas seguidas, abrir incidente)" >> "$LOG"
    fi
  fi
done
