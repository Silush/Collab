"""
Configurações do bot — edite aqui as mensagens e comportamentos.
"""

# ─── Mensagem automática enviada no DM ─────────────────────────────────────────
#
# Variáveis disponíveis:
#   {username}  → nome de usuário de quem comentou (ex: @joao123)
#   {comment}   → texto do comentário feito pela pessoa
#
DM_MESSAGE = (
    "Oi, {username}! 👋 Obrigado pelo seu comentário! "
    "Ficamos felizes com sua participação. "
    "Se tiver alguma dúvida ou quiser saber mais, é só falar aqui. 😊"
)

# ─── Deduplicação ───────────────────────────────────────────────────────────────
# Se True, cada usuário recebe o DM apenas UMA VEZ por sessão do servidor.
# Se False, envia DM para cada comentário novo (mesmo usuário pode receber vários).
SEND_ONCE_PER_USER = True
