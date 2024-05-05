from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.shared import ChatTypeFilter
from bot.states import RegisterState, AuthState
from bot.keyboard.reply import AuthRK, UserRK

from core.requests import TokenController

router = Router(name=__name__)

@router.message(F.text == AuthRK.REG,
                ChatTypeFilter(chat_type=["private"]))
@router.message(ChatTypeFilter(chat_type=["private"]),
                Command(BotCommand(command="register", description="Комманда регистрации")))
async def command_register(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(RegisterState.login)
    await message.answer(
        "Введите логин",
        reply_markup=AuthRK.rk()
    )

@router.message(RegisterState.login)
async def command_register_login(message: Message, state: FSMContext):
    await state.set_data(data={
            "login": message.text
        }
    )
    await state.set_state(RegisterState.password)
    await message.answer(
        "Введите пароль",
        reply_markup=AuthRK.rk()
    )

@router.message(RegisterState.password)
async def command_register_password(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.set_data(data={
            "login": data.get("login"),
            "password": message.text
        }
    )
    await state.set_state(RegisterState.display_name)
    await message.answer(
        "Введите отображающее имя",
        reply_markup=AuthRK.rk()
    )

@router.message(RegisterState.display_name)
async def command_register_display_name(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    response = TokenController.register(data["login"], data["password"], message.text)
    if response.IsException():
        error = response.data
        await message.answer(
            f"<b>Регистрация провалилась провалилась</b>\n\n{error}",
            reply_markup=AuthRK.rk()
        )
        return
    await state.set_data(data={
            "access": response.data["access"],
            "refresh": response.data["refresh"]
        }
    )
    await state.set_state(AuthState.user)
    await message.answer(
        f"Вы авторизировались",
        reply_markup=UserRK.rk()
    )
