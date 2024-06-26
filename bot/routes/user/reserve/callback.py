from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.states import AuthState
from bot.keyboard.reply import UserRK
from bot.routes.base_func import update_state

from bot.keyboard.inline import (
    InlineReserve,
    InlineUserReserve,
    InlineProcessReserve,
    InlineApproveReserve,
    InlinePlace
)
from core.requests import ReserveController

from config import TelegramConfig

from ..base_handlers import check_user_response_exception

router = Router(name=__name__)

@router.callback_query(InlineUserReserve.Callback.filter())
async def user_reserve_action( 
    callback_query: CallbackQuery,
    callback_data: InlineUserReserve.Callback,
    state: FSMContext
):
    now_state = await state.get_state()
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=now_state
    )
    if data is None:
        return
    access = data["access"]
    
    response = ReserveController.delete(
        reserve_id=callback_data.reserve_id,
        token=access
    )
    if await check_user_response_exception(response, callback_query.message, state):
        return

    await callback_query.message.edit_text(
        text="Заявка на бронирование была удалена"
    )
    await callback_query.answer()

@router.callback_query(InlineReserve.Callback.filter())
async def page_change_reserve( 
    callback_query: CallbackQuery,
    callback_data: InlineReserve.Callback,
    state: FSMContext
):
    now_state = await state.get_state()
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=now_state
    )
    if data is None:
        return
    access = data["access"]

    if callback_data.page_index:
        response = ReserveController.get_actual_state(
            states=[callback_data.action],
            page_index=callback_data.page_index,
            token=access
        )
    else:
        response = ReserveController.get_state(
            states=[callback_data.action],
            page_index=callback_data.page_index,
            token=access
        )
    if await check_user_response_exception(response, callback_query.message, state):
        return

    await callback_query.message.edit_text(
        text=InlineReserve.print(
            list=response.data,
            is_actual=callback_data.is_actual,
            state=callback_data.action,
            page_index=callback_data.page_index
        ),
        reply_markup=InlineReserve.build(
            is_actual=callback_data.is_actual,
            state=callback_data.action,
            page_index=callback_data.page_index
        )
    )

@router.callback_query(InlineProcessReserve.Callback.filter())
async def page_change_delete_reserve( 
    callback_query: CallbackQuery,
    callback_data: InlineProcessReserve.Callback,
    state: FSMContext
):
    now_state = await state.get_state()
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=now_state
    )
    if data is None:
        return
    access = data["access"]

    response = ReserveController.get_state(
        states=[2, 3],
        page_index=callback_data.page_index,
        token=access
    )
    if await check_user_response_exception(response, callback_query.message, state):
        return
    
    await callback_query.message.edit_text(
        text=InlineProcessReserve.print(
            list=response.data,
            page_index=callback_data.page_index,
        ),
        reply_markup=InlineProcessReserve.build(
            page_index=callback_data.page_index
        )
    )

@router.callback_query(InlineApproveReserve.Callback.filter())
async def page_change_set_place_reserve( 
    callback_query: CallbackQuery,
    callback_data: InlineApproveReserve.Callback,
    state: FSMContext
):
    now_state = await state.get_state()
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=now_state
    )
    if data is None:
        return
    access = data["access"]

    response = ReserveController.get_state(
        states=[3],
        page_index=callback_data.page_index,
        token=access
    )
    if await check_user_response_exception(response, callback_query.message, state):
        return
    
    await callback_query.message.edit_text(
        text=InlineApproveReserve.print(
            list=response.data,
            page_index=callback_data.page_index,
        ),
        reply_markup=InlineApproveReserve.build(
            page_index=callback_data.page_index
        )
    )


@router.callback_query(InlinePlace.Callback.filter())
async def page_change_set_place_reserve( 
    callback_query: CallbackQuery,
    callback_data: InlinePlace.Callback,
    state: FSMContext
):
    now_state = await state.get_state()
    data = await update_state(
        message=callback_query.message,
        state=state,
        now_state=now_state
    )
    if data is None:
        return
    access = data["access"]

    response = ReserveController.get_state(
        states=[3],
        page_index=callback_data.page_index,
        token=access
    )
    if await check_user_response_exception(response, callback_query.message, state):
        return
    
    await callback_query.message.edit_text(
        text=InlineApproveReserve.print(
            list=response.data,
            page_index=callback_data.page_index,
        ),
        reply_markup=InlineApproveReserve.build(
            page_index=callback_data.page_index
        )
    )
