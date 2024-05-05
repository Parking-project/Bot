from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand

from bot.routes.base_func import update_state_tokens, send_message
from bot.shared import ChatTypeFilter

from core.requests import TokenController

from bot.keyboard.reply import BaseRK

router = Router(name=__name__)

LOGIN = "user2"
PASSWORD = "pass123"

@router.message(ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_send_text(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get("access") is None:
        response = TokenController.login(LOGIN, PASSWORD)
        await state.set_data(data={
                "access": response.data["access"],
                "refresh": response.data["refresh"]
            }
        )
    data = await update_state_tokens(
        message=message,
        state=state,
        now_state=None
    )
    if data is None:
        return
    access = data["access"]

    if message.text is None:
        return
    
    if message.reply_to_message is None:
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
