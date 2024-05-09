from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import HelpState, AuthState, ReserveState
from bot.keyboard.reply import UserRK
from bot.keyboard.inline import InlineProcessReserve
from bot.routes.base_func import update_state, send_message

from core.requests import DocumentController

from config import TelegramConfig

router = Router(name=__name__)

@router.message(ReserveState.set_place_reserve)
async def command_set_reserve_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.set_place_place
    )
    if data is None:
        return
    access = data["access"]
    # Вывести список доступных для данного бронирования

@router.message(ReserveState.set_place_place)
async def command_set_place_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]
