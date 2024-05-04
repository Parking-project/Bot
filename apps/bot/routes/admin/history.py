from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import datetime

from apps.bot.keyboard.inline import *
from apps.bot.states import LogInState
from apps.bot.routes.base_func import *
from apps.bot.keyboard.inline.admin_history import (
    auth_history_action,
    reserve_history_action,
    token_bloclist_action
)

from core.requests import AuthHistoryController, ReserveHistoryController, TokenBlocListController

from ..base_func import update_tokens
from .base_func import auth_history_print, reserve_history_print, token_bloclist_print

router = Router(name=__name__)


@router.message(LogInState.auth, Command(BotCommand(command="auth_history", description="auth command")))
async def command_auth_hostory(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        return
    await message.answer(
        text=auth_history_print(
            AuthHistoryController.get(
                token=access, 
                page_index=0
            ).data, 
            page_index=0
        ),
        reply_markup=auth_history_action()
    )

@router.message(LogInState.auth, Command(BotCommand(command="reserve_history", description="auth command")))
async def command_reserve_hostory(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        return
    await message.answer(
        text=reserve_history_print(
            ReserveHistoryController.get(
                token=access, 
                page_index=0
            ).data, 
            page_index=0
        ),
        reply_markup=reserve_history_action()
    )

@router.message(LogInState.auth, Command(BotCommand(command="token_bloclist", description="auth command")))
async def command_reserve_hostory(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        return
    await message.answer(
        text=token_bloclist_print(
            TokenBlocListController.get(
                token=access, 
                page_index=0
            ).data, 
            page_index=0
        ),
        reply_markup=token_bloclist_action()
    )
