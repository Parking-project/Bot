from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.shared import ChatTypeFilter
from bot.states import AuthState, HelpState
from bot.keyboard.reply import AuthRK, UserRK

from core.requests import TokenController

router = Router(name=__name__)

@router.message(F.text == UserRK.EXIT, AuthState.user)
@router.message(F.text == UserRK.EXIT, AuthState.admin)
@router.message(F.text == UserRK.EXIT, HelpState.text)
@router.message(F.text == UserRK.EXIT, HelpState.documents)
@router.message(Command(BotCommand(command="exit", description="Команда выхода из аккаунта")),
                ChatTypeFilter(chat_type=["private"]), HelpState.text)
@router.message(Command(BotCommand(command="exit", description="Команда выхода из аккаунта")),
                ChatTypeFilter(chat_type=["private"]), AuthState.admin)
@router.message(Command(BotCommand(command="exit", description="Команда выхода из аккаунта")),
                ChatTypeFilter(chat_type=["private"]), AuthState.user)
@router.message(Command(BotCommand(command="exit", description="Команда выхода из аккаунта")),
                ChatTypeFilter(chat_type=["private"]), HelpState.documents)
async def command_logout(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    if data.get("access") is not None:
        TokenController.logout(token=data["access"])
    if data.get("refresh") is not None:
        TokenController.logout(token=data["refresh"])
    await message.answer(
        "Вы вышли из аккаунта",
        reply_markup=AuthRK.rk()
    )