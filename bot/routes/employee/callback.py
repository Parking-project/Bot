from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router, F

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
    data = await employee_auth(
        message=callback_query.message,
        state=state
    )
    if data is None:
        await callback_query.answer()
        return
    access = data["access"]
    response = ReserveController.approve(
        reserve_id=callback_data.reserve_id,
        token=access
    )
    if response.is_exception():
        exception = response.get_exception()
        await callback_query.message.reply(
            text=f"Произоша ошибка! ({exception.message})",
            reply_markup=BaseRK.help_rk()
        )
        return

    if callback_data.chat_id is not None and\
       callback_data.message_id is not None:
        await callback_query.bot.edit_message_text(
            chat_id=callback_data.chat_id,
            message_id=callback_data.message_id,
            text="Заявка на бронирование была одобрена",
        )
    await callback_query.message.delete()

@router.callback_query(InlineBotReserve.Callback.filter(F.action == ReserveAction.delete))
async def reserve_delete( 
    callback_query: CallbackQuery,
    callback_data: InlineBotReserve.Callback,
    state: FSMContext
):
    print("\n\n\nmessage_id = ", callback_query.message.message_id, "\n\n\n")
    data = await employee_auth(
        message=callback_query.message,
        state=state
    )
    if data is None:
        await callback_query.answer()
        return
    access = data["access"]

    response = ReserveController.delete(
        reserve_id=callback_data.reserve_id,
        token=access
    )
    if response.is_exception():
        exception = response.get_exception()
        await callback_query.message.reply(
            text=f"Произоша ошибка! {exception.message}",
            reply_markup=BaseRK.help_rk()
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