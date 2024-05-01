import logging
from typing import Any, Dict

from aiogram import F, Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from ...states import LogIn_State, Register_State
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import TokenController

router = Router(name=__name__)

@router.message(F.text == ButtonRK.AUTH)
@router.message(Command(BotCommand(command="login", description="auth command")))
async def command_login_help(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(LogIn_State.login)
    await message.answer(
        "Введите логин",
        reply_markup=base_rk()
    )

@router.message(LogIn_State.login)
async def command_login_help(message: Message, state: FSMContext):
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
async def command_login_help(message: Message, state: FSMContext):
    data = await state.get_data()
    print(f"\n\n\n{data}\n\n\n")
    login = data.get("login")
    access, refresh = TokenController.login(login, message.text)
    await state.clear()
    # await state.set_data(access=access)
    # await state.set_data(refresh=refresh)
    await state.set_state(LogIn_State.auth)
    await message.answer(
        f"Вы авторизировались\naccess = {access}\nrefresh = {refresh}",
        reply_markup=auth_rk()
    )