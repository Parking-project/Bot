from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.shared import ChatTypeFilter
from bot.states import LogInState, AuthState
from bot.keyboard.reply import AuthRK, UserRK, AdminRK

from core.requests import TokenController

router = Router(name=__name__)

@router.message(F.text == AuthRK.AUTH,
                ChatTypeFilter(chat_type=["private"]))
@router.message(ChatTypeFilter(chat_type=["private"]),
                Command(BotCommand(command="login", description="Комманда авторизации")))
async def command_login(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(LogInState.login)
    await message.answer(
        "Введите логин",
        reply_markup=AuthRK.rk()
    )

@router.message(LogInState.login)
async def command_login_login(message: Message, state: FSMContext):
    await state.set_data(data={
            "login": message.text
        }
    )
    await state.set_state(LogInState.password)
    await message.answer(
        "Введите пароль",
        reply_markup=AuthRK.rk()
    )

@router.message(LogInState.password)
async def command_login_password(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    response = TokenController.login(data["login"], message.text)
    if response.IsException():
        error = response.data["message"]
        await message.answer(
            f"<b>Авторизация провалилась</b>\n\n{error}",
            reply_markup=AuthRK.rk()
        )
        return
    rk = None
    match(response.data["role"]):
        case "USER":
            await state.set_state(AuthState.user)
            rk = UserRK.rk()
        case "ADMIN":
            await state.set_state(AuthState.admin)
            rk = AdminRK.rk()
        case _:
            await state.clear()
            await message.answer(
                f"<b>Авторизация провалилась</b>",
                reply_markup=AuthRK.rk()
            )
            return
    await state.set_data(data={
            "access": response.data["tokens"]["access"],
            "refresh": response.data["tokens"]["refresh"]
        }
    )
    await message.answer(
        f"Вы авторизировались",
        reply_markup=rk
    )
