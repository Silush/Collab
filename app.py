"""
Servidor webhook para o bot da Collab no Instagram.

Fluxo:
  1. Meta envia um POST com dados do novo comentário.
  2. O servidor extrai o IGSID e username do comentador.
  3. O bot envia automaticamente um DM personalizado.
"""

import logging
import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, jsonify, request

import config
from instagram_bot import send_dm

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Conjunto de IDs que já receberam DM nesta sessão (deduplicação em memória)
_already_messaged: set[str] = set()


# ─── Webhook de verificação (GET) ──────────────────────────────────────────────

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """
    O Meta faz um GET para verificar o endpoint quando você o cadastra
    no painel de desenvolvedores. Responde com o hub.challenge se o token bater.
    """
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == os.environ.get("WEBHOOK_VERIFY_TOKEN"):
        logger.info("Webhook verificado com sucesso.")
        return challenge, 200

    logger.warning("Tentativa de verificação falhou. Token inválido.")
    return "Token inválido", 403


# ─── Webhook de eventos (POST) ─────────────────────────────────────────────────

@app.route("/webhook", methods=["POST"])
def receive_event():
    """Recebe notificações de novos comentários e dispara o DM."""
    data: dict[str, Any] = request.get_json(silent=True) or {}

    if data.get("object") != "instagram":
        return jsonify({"status": "ignored"}), 200

    for entry in data.get("entry", []):
        for change in entry.get("changes", []):
            if change.get("field") != "comments":
                continue

            value = change.get("value", {})
            _handle_comment(value)

    return jsonify({"status": "ok"}), 200


# ─── Lógica interna ────────────────────────────────────────────────────────────

def _handle_comment(value: dict[str, Any]) -> None:
    """Processa um comentário recebido e envia o DM se necessário."""
    commenter = value.get("from", {})
    igsid: str = commenter.get("id", "")
    username: str = commenter.get("username", "você")
    comment_text: str = value.get("value", "")
    comment_id: str = value.get("id", "")

    if not igsid:
        logger.warning("Comentário recebido sem IGSID, ignorando. payload=%s", value)
        return

    logger.info(
        "Novo comentário | id=%s | user=%s | texto=%r",
        comment_id, username, comment_text,
    )

    # Deduplicação: pula se já enviou DM para este usuário
    if config.SEND_ONCE_PER_USER and igsid in _already_messaged:
        logger.info("Usuário %s já recebeu DM, pulando.", username)
        return

    message = config.DM_MESSAGE.format(username=f"@{username}", comment=comment_text)
    success = send_dm(igsid, message)

    if success and config.SEND_ONCE_PER_USER:
        _already_messaged.add(igsid)


# ─── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info("Bot da Collab rodando na porta %d", port)
    app.run(host="0.0.0.0", port=port)
