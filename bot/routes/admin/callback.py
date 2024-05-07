from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router

from bot.states import AuthState
from bot.routes.base_func import update_state
from bot.keyboard.inline import (
    InlineAuthHistory,
    InlineReserveHistory,
    InlineTokenBlocList
)
from core.requests import AuthHistoryController, ReserveHistoryController, TokenBlocListController

router = Router(name=__name__)

# region history
@router.callback_query(AuthState.admin,
                       InlineAuthHistory.Callback.filter())
async def page_change_auth( 
    callback_query: CallbackQuery,
    callback_data: InlineAuthHistory.Callback,
    state: FSMContext
):
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        await callback_query.message.delete()
        return
    access = data["access"]
    
    auth_data = AuthHistoryController.get(
        token=access, 
        page_index=callback_data.page_index
    ).data

    await callback_query.message.edit_text(
        text=InlineAuthHistory.print(
            auth_data, 
            page_index=callback_data.page_index
        ),
        reply_markup=InlineAuthHistory.build(callback_data.page_index)
    )

@router.callback_query(AuthState.admin,
                       InlineReserveHistory.Callback.filter())
async def page_change_reserve(
    callback_query: CallbackQuery,
    callback_data: InlineReserveHistory.Callback,
    state: FSMContext
):
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        await callback_query.message.delete()
        return
    access = data["access"]
    
    await callback_query.message.edit_text(
        text=InlineReserveHistory.print(
            ReserveHistoryController.get(
                token=access, 
                page_index=callback_data.page_index
            ).data, 
            page_index=callback_data.page_index
        ),
        reply_markup=InlineReserveHistory.build(callback_data.page_index)
    )

@router.callback_query(AuthState.admin,
                       InlineTokenBlocList.Callback.filter())
async def page_change_token(
    callback_query: CallbackQuery,
    callback_data: InlineTokenBlocList.Callback,
    state: FSMContext
):
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=AuthState.admin
    )
    if data is None:
        await callback_query.message.delete()
        return
    access = data["access"]
    
    await callback_query.message.edit_text(
        text=InlineTokenBlocList.print(
            TokenBlocListController.get(
                token=access, 
                page_index=callback_data.page_index
            ).data, 
            page_index=callback_data.page_index
        ),
        reply_markup=InlineTokenBlocList.build(callback_data.page_index)
    )


@router.callback_query(InlineAuthHistory.Callback.filter())
async def auth_history_message_delete(
    callback_query: CallbackQuery
):
    await callback_query.message.delete()

@router.callback_query(InlineReserveHistory.Callback.filter())
async def reserve_history_message_delete(
    callback_query: CallbackQuery
):
    await callback_query.message.delete()

@router.callback_query(InlineTokenBlocList.Callback.filter())
async def token_history_message_delete(
    callback_query: CallbackQuery
):
    await callback_query.message.delete()
# endregion