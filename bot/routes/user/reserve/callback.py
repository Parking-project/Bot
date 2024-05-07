from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.states import AuthState
from bot.routes.base_func import update_state

from bot.keyboard.inline import (
    InlineReserve,
    InlineUserReserve
)
from core.requests import ReserveController

from config import TelegramConfig

router = Router(name=__name__)

@router.callback_query(InlineUserReserve.Callback.filter())
async def page_change_auth( 
    callback_query: CallbackQuery,
    callback_data: InlineUserReserve.Callback,
    state: FSMContext
):
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]
    
    response = ReserveController.delete(
        reserve_id=callback_data.reserve_id,
        token=access
    )
    if response.IsException():
        await callback_query.message.reply(
            text="Операция провалилась"
        )
        return

    await callback_query.message.edit_text(
        text="Заявка на бронирование была удалена"
    )
    await callback_query.bot.delete_message(
        chat_id=TelegramConfig.RESERVETION_GROUP_ID,
        message_id=callback_data.message_id
    )
    await callback_query.answer()


@router.callback_query(InlineReserve.Callback.filter())
async def page_change_reserve( 
    callback_query: CallbackQuery,
    callback_data: InlineReserve.Callback,
    state: FSMContext
):
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]

    await callback_query.message.edit_text(
        text=InlineReserve.print(
                list=ReserveController.get_state(
                state=callback_data.action,
                page_index=callback_data.page_index,
                token=access
            ).data,
            state=callback_data.action,
            page_index=callback_data.page_index
        ),
        reply_markup=InlineReserve.build()
    )
    await callback_query.answer()

    
@router.callback_query()
async def page_change_reserve( 
    callback_query: CallbackQuery,
    state: FSMContext
):
    await callback_query.message.reply(
        text = callback_query.data
    )

    await callback_query.answer()