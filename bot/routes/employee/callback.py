from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

from core.requests import TokenController
from bot.keyboard.reply import BaseRK

from bot.keyboard.inline.request_reserve import (
    ReserveAction,
    InlineBotReserve
)
from core.requests import ReserveController

from .base_func import employee_auth

router = Router(name=__name__)

@router.callback_query(InlineBotReserve.Callback.filter(F.action == ReserveAction.approve))
async def reserve_approve( 
    callback_query: CallbackQuery,
    callback_data: InlineBotReserve.Callback,
    state: FSMContext
):
    access = await employee_auth(
        message=callback_query.message,
        state=state
    )
    response = ReserveController.approve(
        reserve_id=callback_data.reserve_id,
        token=access
    )
    if response.IsException():
        await callback_query.message.reply(
            text="Операция провалилась"
        )
        return

    if callback_data.chat_id is not None and\
       callback_data.message_id is not None:
        await callback_query.bot.edit_message_text(
            chat_id=callback_data.chat_id,
            message_id=callback_data.message_id,
            text="Заявка на бронирование была одобрена"
        )
    await callback_query.message.delete()

@router.callback_query(InlineBotReserve.Callback.filter(F.action == ReserveAction.delete))
async def reserve_delete( 
    callback_query: CallbackQuery,
    callback_data: InlineBotReserve.Callback,
    state: FSMContext
):
    access = await employee_auth(
        message=callback_query.message,
        state=state
    )
    response = ReserveController.approve(
        reserve_id=callback_data.reserve_id,
        token=access
    )
    if response.IsException():
        await callback_query.message.reply(
            text="Операция провалилась"
        )
        return

    if callback_data.chat_id is not None and\
       callback_data.message_id is not None:
        await callback_query.bot.edit_message_text(
            chat_id=callback_data.chat_id,
            message_id=callback_data.message_id,
            text="Заявка на бронирование была отклонена"
        )
    await callback_query.message.delete()