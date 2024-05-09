from aiogram.types import Message, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F, Router

from bot.keyboard.reply import AuthRK, UserRK, AdminRK
from bot.states import LogInState, AuthState
from bot.shared import ChatTypeFilter

from core.requests import TokenController
from core.domain.entity import ApiResponse, ApiMessage

router = Router(name=__name__)

@router.message(F.text == AuthRK.AUTH,
                ChatTypeFilter(chat_type=["private"]))
@router.message(Command(BotCommand(command="login", description="Комманда авторизации")),
                ChatTypeFilter(chat_type=["private"]))
async def command_login(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(LogInState.login)
    await message.answer(
        "Введите логин",
        reply_markup=AuthRK.rk(True)
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
        reply_markup=AuthRK.rk(True)
    )

@router.message(LogInState.password)
async def command_login_password(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    response: ApiResponse = TokenController.login(data["login"], message.text)
    if response.is_exception():
        exception: ApiMessage = response.get_exception()
        await message.answer(
            f"<b>Авторизация провалилась</b>\n\n{exception.message}",
            reply_markup=AuthRK.rk()
        )
        return
    rk = None
    match(response.data.role):
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
            "access": response.data.access,
            "refresh": response.data.refresh
        }
    )
    await message.answer(
        f"Вы авторизировались",
        reply_markup=rk
    )
