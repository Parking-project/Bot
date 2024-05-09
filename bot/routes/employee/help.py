from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F, Router

from bot.routes.base_func import send_message
from bot.keyboard.reply import BaseRK
from bot.shared import ChatTypeFilter

from .base_func import employee_auth

from config import TelegramConfig

router = Router(name=__name__)

@router.message(F.reply_to_message, F.chat.id == int(TelegramConfig.GROUP_ID), ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_send_text(message: Message, state: FSMContext):
    data = await employee_auth(
        message=message,
        state=state
    )
    if data is None:
        return
    access = data["access"]

    if message.text is None:
        return
    
    answer_tg_id = message.reply_to_message.message_id

    response = send_message(
        access=access,
        text=message.text,
        message=message, 
        answer_tg_id=answer_tg_id
    )
    if response.is_exception():
        exception = response.get_exception()
        await message.reply(
            text=f"Не удалось отправить сообщение! {exception.message}",
            reply_markup=BaseRK.help_rk()
        )
