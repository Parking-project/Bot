from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F, Router

from bot.states import HelpState, AuthState, ReserveState
from bot.routes.base_func import update_state
from bot.keyboard.reply import UserRK
from bot.keyboard.inline import (
    InlineProcessReserve, 
    GetReserveAction, InlineReserve
)

from core.requests import ReserveController

router = Router(name=__name__)

@router.message(AuthState.user, F.text == UserRK.REQUEST_HELP)
@router.message(HelpState.text, F.text == UserRK.REQUEST_HELP)
@router.message(HelpState.documents, F.text == UserRK.REQUEST_HELP)
@router.message(ReserveState.add, F.text == UserRK.REQUEST_HELP)
@router.message(ReserveState.delete, F.text == UserRK.REQUEST_HELP)
@router.message(ReserveState.set_place_place, F.text == UserRK.REQUEST_HELP)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.REQUEST_HELP)
@router.message(ReserveState.get_free, F.text == UserRK.REQUEST_HELP)
async def command_send_message(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=HelpState.text
    )
    if data is None:
        return
    
    await message.answer(
        text="Введите текст сообщения и прикрепите файлы",
        reply_markup=UserRK.rk()
    )

@router.message(AuthState.user, F.text == UserRK.ADD_RESERVE)
@router.message(HelpState.text, F.text == UserRK.ADD_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.ADD_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.ADD_RESERVE)
async def command_add_reserve(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.add
    )
    if data is None:
        return
    
    await message.answer(
        text="Введите длительность бронирования в часах",
        reply_markup=UserRK.rk()
    )

@router.message(AuthState.user, F.text == UserRK.DELETE_RESERVE)
@router.message(HelpState.text, F.text == UserRK.DELETE_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.DELETE_RESERVE)
async def command_delete_reserve(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.delete
    )
    if data is None:
        return
    access = data["access"]
    
    response = ReserveController.get_process(
        page_index=0,
        token=access
    )
    
    if response.is_exception():
        exception = response.get_exception()
        await message.reply(
            text=f"Операция провалилась ({exception.message})"
        )
        return
    message = await message.answer(
        text=InlineProcessReserve.print(
            list=response.data,
            page_index=0,
        ),
        reply_markup=InlineProcessReserve.build()
    )
    await state.update_data(message_id=message.message_id)

@router.message(AuthState.user, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(HelpState.text, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.GET_HISTORY_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.GET_HISTORY_RESERVE)
async def command_get_reserve(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]
    
    response = ReserveController.get_state(
        state=GetReserveAction.sended,
        is_actual=False,
        page_index=0,
        token=access
    )
    
    if response.is_exception():
        exception = response.get_exception()
        await message.reply(
            text=f"Операция провалилась ({exception.message})"
        )
        return
    await message.answer(
        text=InlineReserve.print(
            list=response.data,
            page_index=0,
            is_actual=False,
        ),
        reply_markup=InlineReserve.build(
            is_actual=False
        )
    )

@router.message(AuthState.user, F.text == UserRK.GET_RESERVE)
@router.message(HelpState.text, F.text == UserRK.GET_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.GET_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.GET_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.GET_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.GET_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.GET_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.GET_RESERVE)
async def command_get_history_reserve(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]
    
    
    response = ReserveController.get_state(
        state=GetReserveAction.sended,
        is_actual=True,
        page_index=0,
        token=access
    )
    
    if response.is_exception():
        exception = response.get_exception()
        await message.reply(
            text=f"Операция провалилась ({exception.message})"
        )
        return

    await message.answer(
        text=InlineReserve.print(
            is_actual=True,
            page_index=0,
            list=response.data,
        ),
        reply_markup=InlineReserve.build(
            is_actual=True
        )
    )

@router.message(AuthState.user, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(HelpState.text, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.SET_PLACE_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.SET_PLACE_RESERVE)
async def command_set_place(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.set_place_reserve
    )
    if data is None:
        return
    access = data["access"]
    
    # Вывести список доступных бронирований

    message.answer(
        text="Введите номер бронирования",
        reply_markup=UserRK.rk()
    )
