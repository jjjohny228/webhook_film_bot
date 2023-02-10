from aiogram import Bot, Dispatcher
from config import TOKEN_API
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)


async def check_sub_channels(channels, user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
        if chat_member.status == 'left':
            return False
    return True