from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.shared import ChatTypeFilter
from bot.states import AuthState, HelpState, LogInState, RegisterState
from bot.keyboard.reply import AuthRK, UserRK

from core.requests import TokenController
from core.domain.entity import ApiResponse

router = Router(name=__name__)

@router.message(LogInState.login, F.text == AuthRK.END)
@router.message(LogInState.password, F.text == AuthRK.END)
@router.message(RegisterState.login, F.text == AuthRK.END)
@router.message(RegisterState.password, F.text == AuthRK.END)
@router.message(RegisterState.display_name, F.text == AuthRK.END)
@router.message(RegisterState.display_name, F.text == AuthRK.END)
@router.message(LogInState.login, Command(BotCommand(command="cancel", description="Команда выхода из аккаунта")))
@router.message(LogInState.password, Command(BotCommand(command="cancel", description="Команда выхода из аккаунта")))
@router.message(RegisterState.login, Command(BotCommand(command="cancel", description="Команда выхода из аккаунта")))
@router.message(RegisterState.password, Command(BotCommand(command="cancel", description="Команда выхода из аккаунта")))
@router.message(RegisterState.display_name, Command(BotCommand(command="cancel", description="Команда выхода из аккаунта")))
@router.message(RegisterState.display_name, Command(BotCommand(command="cancel", description="Команда выхода из аккаунта")))
async def command_logout(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="<b>Операция прервана</b>",
        reply_markup=AuthRK.rk()
    )

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
        response: ApiResponse = TokenController.logout(token=data["access"])
    if data.get("refresh") is not None:
        TokenController.logout(token=data["refresh"])
    await message.answer(
        "Вы вышли из аккаунта",
        reply_markup=AuthRK.rk()
    )