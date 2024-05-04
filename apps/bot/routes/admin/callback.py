from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router

from apps.bot.states import LogInState
from apps.bot.routes.base_func import update_tokens
from apps.bot.keyboard.inline.admin_history import (
    AuthHistoryCallback,
    auth_history_action,
    ReserveHistoryCallback,
    reserve_history_action,
    TokenBlocListCallback,
    token_bloclist_action
)
from apps.bot.keyboard.inline.test import TestCallback1
from core.requests import AuthHistoryController, ReserveHistoryController, TokenBlocListController
from .base_func import auth_history_print, reserve_history_print, token_bloclist_print

router = Router(name=__name__)

# region history
@router.callback_query(AuthHistoryCallback.filter(),
                       LogInState.auth)
async def page_change_auth(
    callback_query: CallbackQuery,
    callback_data: AuthHistoryCallback,
    state: FSMContext
):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        await callback_query.message.delete()
        return
    
    auth_data = AuthHistoryController.get(
        token=access, 
        page_index=callback_data.page_index
    ).data

    await callback_query.message.edit_text(
        text=auth_history_print(
            auth_data, 
            page_index=callback_data.page_index
        ),
        reply_markup=auth_history_action(callback_data.page_index)
    )

@router.callback_query(ReserveHistoryCallback.filter(),
                       LogInState.auth)
async def page_change_reserve(
    callback_query: CallbackQuery,
    callback_data: ReserveHistoryCallback,
    state: FSMContext
):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        await callback_query.message.delete()
        return
    
    await callback_query.message.edit_text(
        text=reserve_history_print(
            ReserveHistoryController.get(
                token=access, 
                page_index=callback_data.page_index
            ).data, 
            page_index=callback_data.page_index
        ),
        reply_markup=reserve_history_action(callback_data.page_index)
    )

@router.callback_query(TokenBlocListCallback.filter(),
                       LogInState.auth)
async def page_change_token(
    callback_query: CallbackQuery,
    callback_data: ReserveHistoryCallback,
    state: FSMContext
):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        await callback_query.message.delete()
        return
    
    await callback_query.message.edit_text(
        text=token_bloclist_print(
            TokenBlocListController.get(
                token=access, 
                page_index=callback_data.page_index
            ).data, 
            page_index=callback_data.page_index
        ),
        reply_markup=token_bloclist_action(callback_data.page_index)
    )


@router.callback_query(AuthHistoryCallback.filter())
async def auth_history_message_delete(
    callback_query: CallbackQuery,
    callback_data: AuthHistoryCallback
):
    await callback_query.message.delete()

@router.callback_query(ReserveHistoryCallback.filter())
async def reserve_history_message_delete(
    callback_query: CallbackQuery,
    callback_data: ReserveHistoryCallback
):
    await callback_query.message.delete()

@router.callback_query(ReserveHistoryCallback.filter())
async def token_history_message_delete(
    callback_query: CallbackQuery,
    callback_data: ReserveHistoryCallback
):
    await callback_query.message.delete()
# endregion

@router.callback_query()
async def token_history_message_delete(
    callback_query: CallbackQuery,
    callback_data: TestCallback1
):
    if callback_data.page_index is None:
        await callback_query.message.reply(
            text=f"This message Send - {callback_data.name} but We catch None"
        )
        return
    await callback_query.message.reply(
        text=f"This message Send - {callback_data.name}"
    )