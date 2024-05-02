from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from apps.shared import ChatTypeFilter
from apps.bot.states import LogIn_State, Register_State
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import TokenController

router = Router(name=__name__)

# region login
@router.message(ChatTypeFilter(chat_type=["private"]),
                F.text == ButtonRK.AUTH)
@router.message(Command(BotCommand(command="login", description="Комманда авторизации")),
                ChatTypeFilter(chat_type=["private"]), )
async def command_login(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(LogIn_State.login)
    await message.answer(
        "Введите логин",
        reply_markup=base_rk()
    )

@router.message(LogIn_State.login)
async def command_login_login(message: Message, state: FSMContext):
    await state.set_data(data={
            "login": message.text
        }
    )
    await state.set_state(LogIn_State.password)
    await message.answer(
        "Введите пароль",
        reply_markup=base_rk()
    )

@router.message(LogIn_State.password)
async def command_login_password(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    response = TokenController.login(data["login"], message.text)
    if response.IsException():
        error = response.data
        await message.answer(
            f"<b>Авторизация провалилась</b>\n\n{error}",
            reply_markup=base_rk()
        )
        return
    await state.set_data(data={
            "access": response.data["access"],
            "refresh": response.data["refresh"]
        }
    )
    await state.set_state(LogIn_State.auth)
    await message.answer(
        f"Вы авторизировались",
        reply_markup=auth_rk()
    )

# endregion

# region register
@router.message(ChatTypeFilter(chat_type=["private"]),
                F.text == ButtonRK.REG)
@router.message(Command(BotCommand(command="register", description="Комманда регистрации")),
                ChatTypeFilter(chat_type=["private"]))
async def command_register(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Register_State.login)
    await message.answer(
        "Введите логин",
        reply_markup=base_rk()
    )

@router.message(Register_State.login)
async def command_register_login(message: Message, state: FSMContext):
    await state.set_data(data={
            "login": message.text
        }
    )
    await state.set_state(Register_State.password)
    await message.answer(
        "Введите пароль",
        reply_markup=base_rk()
    )

@router.message(Register_State.password)
async def command_register_password(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.set_data(data={
            "login": data.get("login"),
            "password": message.text
        }
    )
    await state.set_state(Register_State.display_name)
    await message.answer(
        "Введите отображающее имя",
        reply_markup=base_rk()
    )

@router.message(Register_State.display_name)
async def command_register_display_name(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    response = TokenController.register(data["login"], data["password"], message.text)
    if response.IsException():
        error = response.data
        await message.answer(
            f"<b>Регистрация провалилась провалилась</b>\n\n{error}",
            reply_markup=base_rk()
        )
        return
    await state.set_data(data={
            "access": response.data["access"],
            "refresh": response.data["refresh"]
        }
    )
    await state.set_state(LogIn_State.auth)
    await message.answer(
        f"Вы авторизировались",
        reply_markup=auth_rk()
    )

# endregion

@router.message(F.text == ButtonRK.EXIT,
                LogIn_State.auth)
@router.message(Command(BotCommand(command="exit", description="Команда выхода из аккаунта")),
                ChatTypeFilter(chat_type=["private"]), 
                LogIn_State.auth)
async def command_logout(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    TokenController.logout(token=data["access"])
    TokenController.logout(token=data["refresh"])
    await message.answer(
        "Вы вышли из аккаунта",
        reply_markup=base_rk()
    )