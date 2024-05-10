from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F, Router

from bot.states import HelpState, AuthState, ReserveState
from bot.routes.base_func import update_state
from bot.keyboard.reply import UserRK
from bot.keyboard.inline import (
    InlineProcessReserve, 
    InlineReserve,
    InlineApproveReserve
)

from core.domain.entity import ApiResponse
from core.requests import ReserveController

async def check_user_response_exception(response: ApiResponse, message: Message, state: FSMContext):
    if response.is_exception():
        exception = response.get_exception()
        await message.reply(
            text=exception.message
        )
        await state.set_state(AuthState.user)
        return True
    return False


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
        state=state
    )
    if data is None:
        return
    
    await message.answer(
        text="Введите текст сообщения и прикрепите файлы",
        reply_markup=UserRK.rk()
    )
    await state.set_state(HelpState.text)

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
        state=state
    )
    if data is None:
        return
    
    await message.answer(
        text="Введите длительность бронирования в часах",
        reply_markup=UserRK.rk()
    )
    await state.set_state(ReserveState.add)

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
        state=state
    )
    if data is None:
        return
    access = data["access"]
    
    response = ReserveController.get_state(
        states=[2, 3],
        page_index=0,
        token=access
    )
    
    if await check_user_response_exception(response, message, state):
        return
    if len(response.data) == 0:
        await message.answer(
            "Бронирований для удаления не найдено"
        )
        await state.set_state(AuthState.user)
        return
    message = await message.answer(
        text=InlineProcessReserve.print(
            list=response.data,
            page_index=0,
        ),
        reply_markup=InlineProcessReserve.build()
    )
    await state.update_data(message_id=message.message_id)
    await state.set_state(ReserveState.delete)

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
        states=[2],
        page_index=0,
        token=access
    )
    
    if await check_user_response_exception(response, message, state):
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
        states=[2],
        page_index=0,
        token=access
    )

    if await check_user_response_exception(response, message, state):
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
    
    response = ReserveController.get_state(
        states=[3],
        page_index=0,
        token=access
    )
    if await check_user_response_exception(response, message, state):
        return
    if len(response.data) == 0:
        await message.answer(
            "Доступных бронирований для указания парковочного места не найдено"
        )
        await state.set_state(AuthState.user)
        return
    
    message = await message.answer(
        text=InlineApproveReserve.print(
            list=response.data,
            page_index=0,
        ),
        reply_markup=InlineApproveReserve.build()
    )
    await state.update_data(message_id=message.message_id)
    await state.set_state(ReserveState.set_place_reserve)
    message.answer(
        text="Введите номер бронирования",
        reply_markup=UserRK.rk()
    )
