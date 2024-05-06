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

@router.message(AuthState.user, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(HelpState.text, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(AuthState.user, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(HelpState.text, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(ReserveState.add, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(ReserveState.delete, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(HelpState.documents, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(ReserveState.get_free, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="set_place", description="Установить парковочное место")))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="set_place", description="Установить парковочное место")))
async def command_set_place(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.set_place_reserve
    )
    if data is None:
        return
    access = data["access"]
    
    # Вывести список доступных бронирований

    message.answer(
        text="Введите номер бронирования",
        reply_markup=UserRK.rk()
    )

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
