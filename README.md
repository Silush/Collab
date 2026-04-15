# Collab — Bot de DM Automático no Instagram

Quando alguém comenta em qualquer postagem da Collab no Instagram, este bot envia automaticamente uma mensagem direta (DM) para essa pessoa.

---

## Como funciona

```
Alguém comenta no post
        ↓
Meta envia webhook → este servidor
        ↓
Bot envia DM automático para o comentador
```

---

## Pré-requisitos

- Conta **Business ou Creator** no Instagram
- Página do Facebook conectada ao perfil
- App criado no [Meta for Developers](https://developers.facebook.com/)
- Python 3.11+
- Servidor com IP público (ou ngrok para testes locais)

### Permissões necessárias no App Meta

| Permissão | Para quê |
|---|---|
| `instagram_manage_comments` | Receber notificações de comentários |
| `instagram_manage_messages` | Enviar DMs |
| `pages_messaging` | Acesso à API de mensagens |

---

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/silush/collab.git
cd collab

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure as credenciais
cp .env.example .env
# Edite o .env com seus tokens reais
```

---

## Configuração (`.env`)

```env
PAGE_ACCESS_TOKEN=...   # Token da sua Página do Facebook
IG_USER_ID=...          # ID numérico do seu perfil no Instagram
WEBHOOK_VERIFY_TOKEN=...# Qualquer texto secreto (você define)
PORT=5000
```

### Como obter o `IG_USER_ID`

```bash
curl "https://graph.facebook.com/v21.0/me/accounts?access_token=SEU_TOKEN"
# Pegue o id da conta IG vinculada à Página
```

---

## Rodando o servidor

```bash
# Desenvolvimento
python app.py

# Produção
gunicorn app:app --bind 0.0.0.0:5000
```

---

## Configurando o Webhook no Meta

1. Acesse seu App em [developers.facebook.com](https://developers.facebook.com/)
2. Vá em **Instagram → Webhooks**
3. Adicione o endpoint: `https://seu-dominio.com/webhook`
4. Coloque o mesmo `WEBHOOK_VERIFY_TOKEN` do seu `.env`
5. Inscreva-se no campo **`comments`**

### Teste local com ngrok

```bash
ngrok http 5000
# Use a URL gerada (ex: https://abc123.ngrok.io/webhook) no painel do Meta
```

---

## Personalizando a mensagem (`config.py`)

Edite o arquivo `config.py`:

```python
DM_MESSAGE = (
    "Oi, {username}! Obrigado pelo comentário! "
    "Fique à vontade para entrar em contato. 😊"
)

# True  → cada usuário recebe DM apenas uma vez
# False → envia DM a cada comentário novo
SEND_ONCE_PER_USER = True
```

Variáveis disponíveis na mensagem:
- `{username}` — nome do usuário que comentou
- `{comment}` — texto do comentário

---

## Estrutura do projeto

```
collab/
├── app.py              # Servidor webhook (Flask)
├── instagram_bot.py    # Chamadas à Instagram Graph API
├── config.py           # Mensagem e configurações do bot
├── requirements.txt    # Dependências Python
├── .env.example        # Template de variáveis de ambiente
└── README.md
```
