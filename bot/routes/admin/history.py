from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboard.inline import *
from bot.keyboard.reply import AdminRK
from bot.states import AuthState
from bot.routes.base_func import update_state
from bot.keyboard.inline import (
    InlineAuthHistory,
    InlineReserveHistory,
    InlineTokenBlocList
)

from core.requests import AuthHistoryController, ReserveHistoryController, TokenBlocListController
from core.domain.entity import ApiResponse

router = Router(name=__name__)

@router.message(AuthState.admin, F.text == AdminRK.AUTH_HISTORY)
@router.message(AuthState.admin, Command(BotCommand(command="auth_history", description="auth command")))
async def command_auth_hostory(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        return
    access = data["access"]
    response: ApiResponse = AuthHistoryController.get(
        token=access, 
        page_index=0
    )
    if response.is_exception():
        await message.answer(
            text=f"Операция провалилась ({response.data.message})"
        )
        return

    await message.answer(
        text=InlineAuthHistory.print(
            response.data, 
            page_index=0
        ),
        reply_markup=InlineAuthHistory.build()
    )

@router.message(AuthState.admin, F.text == AdminRK.RESERVE_HISTORY)
@router.message(AuthState.admin, Command(BotCommand(command="reserve_history", description="auth command")))
async def command_reserve_hostory(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        return
    access = data["access"]
    response: ApiResponse = ReserveHistoryController.get(
        token=access, 
        page_index=0
    )
    if response.is_exception():
        await message.answer(
            text=f"Операция провалилась ({response.data.message})"
        )
        return

    await message.answer(
        text=InlineReserveHistory.print(
            list=response.data,
            page_index=0
        ),
        reply_markup=InlineReserveHistory.build()
    )

@router.message(AuthState.admin, F.text == AdminRK.TOKEN_HISTORY)
@router.message(AuthState.admin, Command(BotCommand(command="token_bloclist", description="auth command")))
async def command_token_bloclist(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        return
    access = data["access"]
    response: ApiResponse = TokenBlocListController.get(
        token=access, 
        page_index=0
    )
    if response.is_exception():
        await message.answer(
            text=f"Операция провалилась ({response.data.message})"
        )
        return
    
    await message.answer(
        text=InlineTokenBlocList.print(
            response.data, 
            page_index=0
        ),
        reply_markup=InlineTokenBlocList.build()
    )
