from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboard.inline import *
from bot.states import AuthState
from bot.routes.base_func import *
from bot.keyboard.inline.admin_history import (
    auth_history_action,
    reserve_history_action,
    token_bloclist_action
)

from core.requests import AuthHistoryController, ReserveHistoryController, TokenBlocListController

from ..base_func import update_state
from .base_func import auth_history_print, reserve_history_print, token_bloclist_print

router = Router(name=__name__)

@router.message(AuthState.admin, 
                Command(BotCommand(command="auth_history", description="auth command")))
async def command_auth_hostory(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        return
    access = data["access"]

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

@router.message(AuthState.admin, 
                Command(BotCommand(command="reserve_history", description="auth command")))
async def command_reserve_hostory(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        return
    access = data["access"]

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

@router.message(AuthState.admin, 
                Command(BotCommand(command="token_bloclist", description="auth command")))
async def command_reserve_hostory(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        return
    access = data["access"]
    
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
