import ssl
from create_bot import dp, bot
from handlers.admin import register_admin_handlers
from handlers.client import register_client_handlers
from data_base.data_functions import start_db
from config import WEBHOOK_URL, WEBHOOK_SSL_CERT, WEBHOOK_PATH, WEBHOOK_SSL_PRIV, WEBAPP_HOST,  WEBAPP_PORT
from aiogram.utils.executor import start_webhook


async def on_startup(_):
    print("Бот был запущен")
    start_db()
    await bot.set_webhook(WEBHOOK_URL, certificate=open(WEBHOOK_SSL_CERT, 'rb'))


async def on_shutdown(_):
    await bot.delete_webhook()

register_admin_handlers(dp)
register_client_handlers(dp)

# Generate SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=context
    )
