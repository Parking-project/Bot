from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router

from apps.bot.states import LogIn_State
from apps.bot.keyboard.inline.admin_history import (
    AuthHistoryCallback,
    auth_history_action,
    ReserveHistoryCallback,
    reserve_history_action
)
from core.requests import AuthHistoryController, ReserveHistoryController
from apps.bot.routes.base_func import update_tokens, page_print

router = Router(name=__name__)

@router.callback_query(AuthHistoryCallback,
                       LogIn_State.auth)
async def page_change_auth(
    callback_query: CallbackQuery,
    callback_data: AuthHistoryCallback,
    state: FSMContext
):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data["access"]
    if access is None:
        await callback_query.message.delete()
        return
    
    response_json = AuthHistoryController.get(callback_data.page_index, token=["access"]).json()
    

@router.callback_query(ReserveHistoryCallback,
                       LogIn_State.auth)
async def page_change_auth(
    callback_query: CallbackQuery,
    callback_data: ReserveHistoryCallback,
    state: FSMContext
):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data["access"]
    if access is None:
        await callback_query.message.delete()
        return
    
    ReserveHistoryController.get(callback_data.page_index, token=["access"])

@router.callback_query(AuthHistoryCallback)
async def auth_history_message_delete(
    callback_query: CallbackQuery,
    callback_data: AuthHistoryCallback
):
    await callback_query.message.delete()

@router.callback_query(ReserveHistoryCallback)
async def reserve_history_message_delete(
    callback_query: CallbackQuery,
    callback_data: ReserveHistoryCallback
):
    await callback_query.message.delete()