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

@router.message(AuthState.user, F.text == UserRK.DELETE_RESERVE)
@router.message(HelpState.text, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.DELETE_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.DELETE_RESERVE)
@router.message(AuthState.user, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(HelpState.text, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.add, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.delete, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(HelpState.documents, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.get_free, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
async def command_delete(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.delete
    )
    if data is None:
        return
    
    # Вывести список доступных для удаления бронирований

    message.answer(
        text="Введите номер бронирования",
        reply_markup=UserRK.rk()
    )

@router.message(ReserveState.delete)
async def command_delete_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]