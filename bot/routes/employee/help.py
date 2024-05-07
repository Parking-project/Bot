from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.routes.base_func import send_message
from bot.shared import ChatTypeFilter

from bot.keyboard.reply import BaseRK

from config import TelegramConfig

from .base_func import employee_auth

router = Router(name=__name__)

@router.message(F.reply_to_message,
                F.chat.id == int(TelegramConfig.GROUP_ID),
                ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_send_text(message: Message, state: FSMContext):
    access = await employee_auth(
        message=message,
        state=state
    )

    if message.text is None:
        return
    
    answer_tg_id = message.reply_to_message.message_id

    response_data = send_message(
        access=access,
        text=message.text,
        message=message, 
        answer_tg_id=answer_tg_id
    )
    if response_data.IsException():
        await message.reply(
            text=f"Не удалось отправить сообщение! {response_data.data}",
            reply_markup=BaseRK.help_rk()
        )
