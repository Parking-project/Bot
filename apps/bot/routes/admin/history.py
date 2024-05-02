from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import datetime

from apps.bot.keyboard.inline import *
from apps.bot.states import LogIn_State
from apps.bot.routes.base_func import *
from apps.bot.keyboard.inline.admin_history import (
    AuthHistoryCallback,
    auth_history_action,
    ReserveHistoryCallback,
    reserve_history_action
)

from core.requests import AuthHistoryController, ReserveHistoryController

from ..base_func import update_tokens
from .base_func import auth_history_print, reserve_history_print

router = Router(name=__name__)


@router.message(LogIn_State.auth, Command(BotCommand(command="auth_history", description="auth command")))
async def command_auth_hostory(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data["access"]
    await message.answer(
        text=auth_history_print(
            AuthHistoryController.get(
                token=access, 
                page_index=0
            ), 
            page_index=0
        ),
        reply_markup=auth_history_action()
    )

@router.message(LogIn_State.auth, Command(BotCommand(command="reserve_history", description="auth command")))
async def command_reserve_hostory(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data["access"]
    await message.answer(
        text=reserve_history_print(
            ReserveHistoryController.get(
                token=access, 
                page_index=0
            ), 
            page_index=0
        ),
        reply_markup=reserve_history_action()
    )
