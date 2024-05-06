from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import HelpState, AuthState, ReserveState
from bot.keyboard.reply import UserRK
from bot.routes.base_func import update_state, send_message

from core.requests import DocumentController

from config import TelegramConfig

router = Router(name=__name__)

@router.message(AuthState.user, F.text == UserRK.ADD_RESERVE)
@router.message(HelpState.text, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.ADD_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.ADD_RESERVE)
@router.message(AuthState.user, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(HelpState.text, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(ReserveState.add, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(ReserveState.delete, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(HelpState.documents, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(ReserveState.get_free, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="add_reserve", description="Добавить бронирование")))
async def command_add(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.add
    )
    if data is None:
        return
    
    message.answer(
        text="Введите длительность бронирования в часах",
        reply_markup=UserRK.rk()
    )

@router.message(ReserveState.add)
async def command_add_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]