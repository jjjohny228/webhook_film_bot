# bot token
TOKEN_API = ""

# channels to subscribe
CHANNELS = [
    ("channel_name", "channel_id", "channel_url")
]

# message to unsubscribed users
NOT_SUB_MESSAGE = "Для доступа к базе данных фильмов подпишитесь на каналы⬇️⬇️⬇️"


# webhook settings
WEBHOOK_HOST = 'https://your.domain'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3001

# ssl certificate settings
WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key