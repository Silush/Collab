"""
Wrapper para a Instagram Graph API.
Responsável por enviar DMs e registrar logs das ações.
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

GRAPH_API_VERSION = "v21.0"
GRAPH_BASE_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


def _access_token() -> str:
    token = os.environ.get("PAGE_ACCESS_TOKEN", "")
    if not token:
        raise EnvironmentError("PAGE_ACCESS_TOKEN não está definido no .env")
    return token


def _ig_user_id() -> str:
    uid = os.environ.get("IG_USER_ID", "")
    if not uid:
        raise EnvironmentError("IG_USER_ID não está definido no .env")
    return uid


def send_dm(recipient_igsid: str, text: str) -> bool:
    """
    Envia um DM (mensagem direta) para um usuário do Instagram.

    Args:
        recipient_igsid: Instagram Scoped User ID do destinatário.
        text: Texto da mensagem a ser enviada.

    Returns:
        True se enviado com sucesso, False caso contrário.
    """
    url = f"{GRAPH_BASE_URL}/{_ig_user_id()}/messages"
    payload = {
        "recipient": {"id": recipient_igsid},
        "message": {"text": text},
    }
    params = {"access_token": _access_token()}

    try:
        response = requests.post(url, json=payload, params=params, timeout=10)
        data = response.json()

        if response.ok:
            logger.info("DM enviado para %s | message_id=%s", recipient_igsid, data.get("message_id"))
            return True

        logger.error(
            "Falha ao enviar DM para %s | status=%d | erro=%s",
            recipient_igsid,
            response.status_code,
            data.get("error", {}).get("message", "desconhecido"),
        )
        return False

    except requests.RequestException as exc:
        logger.exception("Erro de conexão ao enviar DM para %s: %s", recipient_igsid, exc)
        return False
