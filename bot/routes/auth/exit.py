from aiogram.types import Message, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F, Router

from bot.states import AuthState, HelpState, LogInState, RegisterState, ReserveState
from bot.keyboard.reply import AuthRK, UserRK
from bot.shared import ChatTypeFilter

from core.requests import TokenController

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

@router.message(AuthState.admin, F.text == UserRK.EXIT)
@router.message(AuthState.user, F.text == UserRK.EXIT)
@router.message(HelpState.text, F.text == UserRK.EXIT)
@router.message(HelpState.documents, F.text == UserRK.EXIT)
@router.message(ReserveState.add, F.text == UserRK.EXIT)
@router.message(ReserveState.delete, F.text == UserRK.EXIT)
@router.message(ReserveState.set_place_place, F.text == UserRK.EXIT)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.EXIT)
@router.message(ReserveState.get_free, F.text == UserRK.EXIT)
@router.message(AuthState.admin, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(AuthState.user, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(HelpState.text, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(HelpState.documents, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(ReserveState.add, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(ReserveState.delete, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
@router.message(ReserveState.get_free, Command(BotCommand(command="exit", description="Команда выхода из аккаунта")), ChatTypeFilter(chat_type=["private"]))
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