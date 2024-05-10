from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import HelpState, AuthState, ReserveState
from bot.keyboard.reply import UserRK
from bot.routes.base_func import update_state, send_message
from bot.keyboard.inline import InlineProcessReserve

from core.requests import ReserveController

from config import TelegramConfig

from ..base_handlers import check_user_response_exception

router = Router(name=__name__)

@router.message(ReserveState.delete)
async def command_delete_id(message: Message, state: FSMContext):
    await state.set_state(AuthState.user)
    data = await update_state(
        message=message,
        state=state
    )
    if data is None:
        return
    
    try:
        index = int(message.text)
    except:
        await message.reply(
            text="Необходимо ввести только индекс заявки на бронирование выведенное ранее!",
            reply_markup=UserRK.rk()
        )
        return
    
    access = data["access"]


    await message.bot.delete_message(
        message.chat.id,
        message_id=data["message_id"]
    )
    response = ReserveController.delete_index(
        reserve_index=index,
        token=access
    )
    if await check_user_response_exception(response, message, state):
        return
    await message.answer(
        text=f"Заявка успешно удалена",
        reply_markup=UserRK.rk()
    )