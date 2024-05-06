from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.routes.base_func import update_state, send_message
from bot.shared import ChatTypeFilter

from core.requests import TokenController

from bot.keyboard.reply import BaseRK

from config import TelegramConfig

router = Router(name=__name__)

LOGIN = "user2"
PASSWORD = "pass123"

@router.message(F.reply_to_message,
                F.chat.id == int(TelegramConfig.GROUP_ID),
                ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_send_text(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get("access") is None:
        response = TokenController.login(LOGIN, PASSWORD)
        if response.IsException():
            
            await message.reply(
                text=f"Не удалось отправить сообщение! {response_data.data}",
                reply_markup=BaseRK.help_rk()
            )
            return
        await state.set_data(data={
                "access": response.data["tokens"]["access"],
                "refresh": response.data["tokens"]["refresh"]
            }
        )
    data = await update_state(
        message=None,
        state=state,
        now_state=None
    )
    if data is None:
        return
    access = data["access"]

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
