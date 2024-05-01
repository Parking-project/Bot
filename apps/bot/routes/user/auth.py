from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from ...states import LogIn_State, Register_State
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import TokenController
from apps.shared import ChatTypeFilter

router = Router(name=__name__)

# region login
@router.message(F.text == ButtonRK.AUTH, ChatTypeFilter(chat_type=["private"]))
@router.message(ChatTypeFilter(chat_type=["private"]), Command(BotCommand(command="login", description="auth command")))
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
    response_json = TokenController.login(data["login"], message.text).json()
    if response_json.get("tokens") is None:
        error = response_json.get("message")
        await message.answer(
            f"<b>Авторизация провалилась</b>\n\n{error}",
            reply_markup=base_rk()
        )
        return
    tokens = response_json["tokens"]
    access = tokens["access"]
    refresh = tokens["refresh"]
    await state.set_data(data={
            "access": access,
            "refresh": refresh
        }
    )
    await state.set_state(LogIn_State.auth)
    await message.answer(
        f"Вы авторизировались\naccess = {access}\nrefresh = {refresh}",
        reply_markup=auth_rk()
    )

# endregion

# region register
@router.message(F.text == ButtonRK.REG, ChatTypeFilter(chat_type=["private"]))
@router.message(ChatTypeFilter(chat_type=["private"]), Command(BotCommand(command="register", description="register command")))
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
    response_json = TokenController.register(data["login"], data["password"], message.text).json()
    if response_json.get("tokens") is None:
        error = response_json.get("message")
        await message.answer(
            f"<b>Регистрация провалилась провалилась</b>\n\n{error}",
            reply_markup=base_rk()
        )
        return
    tokens = response_json["tokens"]
    access = tokens["access"]
    refresh = tokens["refresh"]
    await state.set_data(data={
            "access": access,
            "refresh": refresh
        }
    )
    await state.set_state(LogIn_State.auth)
    await message.answer(
        f"Вы авторизировались\naccess = {access}\nrefresh = {refresh}",
        reply_markup=auth_rk()
    )

# endregion

@router.message(F.text == ButtonRK.EXIT, LogIn_State.auth)
@router.message(LogIn_State.auth, ChatTypeFilter(chat_type=["private"]), Command(BotCommand(command="exit", description="auth command")))
async def command_logout(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    TokenController.logout(token=data["access"])
    TokenController.logout(token=data["refresh"])
    await message.answer(
        "Вы вышли из аккаунта",
        reply_markup=base_rk()
    )