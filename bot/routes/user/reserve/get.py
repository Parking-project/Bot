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

@router.message(AuthState.user, F.text == UserRK.GET)
@router.message(HelpState.text, F.text == UserRK.GET)
@router.message(ReserveState.add, F.text == UserRK.GET)
@router.message(ReserveState.delete, F.text == UserRK.GET)
@router.message(HelpState.documents, F.text == UserRK.GET)
@router.message(ReserveState.get_free, F.text == UserRK.GET)
@router.message(ReserveState.set_place_place, F.text == UserRK.GET)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.GET)
@router.message(AuthState.user, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(HelpState.text, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(ReserveState.add, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(ReserveState.delete, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(HelpState.documents, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(ReserveState.get_free, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="get_reserve", description="Получить бронирование")))
async def command_get_reserve(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]

@router.message(AuthState.user, F.text == UserRK.GET_FREE_PLACE)
@router.message(HelpState.text, F.text == UserRK.GET_FREE_PLACE)
@router.message(ReserveState.add, F.text == UserRK.GET_FREE_PLACE)
@router.message(ReserveState.delete, F.text == UserRK.GET_FREE_PLACE)
@router.message(HelpState.documents, F.text == UserRK.GET_FREE_PLACE)
@router.message(ReserveState.get_free, F.text == UserRK.GET_FREE_PLACE)
@router.message(ReserveState.set_place_place, F.text == UserRK.GET_FREE_PLACE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.GET_FREE_PLACE)
@router.message(AuthState.user, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(HelpState.text, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(ReserveState.add, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(ReserveState.delete, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(HelpState.documents, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(ReserveState.get_free, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="get_free_place", description="Получить свободные парковочные места")))
async def command_get_place(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.get_free
    )
    if data is None:
        return
    message.answer(
        text="Введите длительность того насколько парковочное место должно быть свободным в часах",
        reply_markup=UserRK.rk()
    )

@router.message(ReserveState.get_free)
async def command_get_place(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]
