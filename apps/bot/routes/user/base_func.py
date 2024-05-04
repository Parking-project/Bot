from aiogram.types import Message
from core.requests import MessageController

# Отправка собщения пользователем
async def send_mess(message: Message):
    answer_tg_id = None
    if message.reply_to_message:
        answer_tg_id = message.reply_to_message.message_id

    # MessageController.post(
    #     token = 
    # )