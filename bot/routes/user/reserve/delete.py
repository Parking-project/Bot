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

router = Router(name=__name__)

@router.message(ReserveState.delete)
async def command_delete_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
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


    response = ReserveController.delete_index(
        reserve_index=index,
        token=access
    )
    if response.is_exception():
        exception = response.get_exception()
        await message.answer(
            text=f"Удаление заявки провалилось ({exception.message})",
            reply_markup=UserRK.rk()
        )
        return
    await message.answer(
        text=f"Заявка успешно удалена",
        reply_markup=UserRK.rk()
    )