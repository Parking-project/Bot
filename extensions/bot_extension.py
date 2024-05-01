from aiogram.enums import ParseMode
from config.telegram_config import TelegramConfig
from aiogram import Bot

def register_bot():
    return Bot(
        token=TelegramConfig.TOKEN_API,
        parse_mode=ParseMode.HTML
    )