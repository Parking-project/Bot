from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import HelpState, AuthState, ReserveState
from bot.keyboard.reply import UserRK
from bot.keyboard.inline import InlinePlace
from bot.routes.base_func import update_state, send_message

from core.domain.entity import Reserve, Place
from core.requests import DocumentController, ReserveController, PlaceController

from config import TelegramConfig

from ..base_handlers import check_user_response_exception
import re

router = Router(name=__name__)

@router.message(ReserveState.set_place_reserve)
async def command_set_reserve_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state
    )
    if data is None:
        return
    
    try:
        index = int(message.text)
    except:
        await message.reply(
            text="Необходимо ввести только индекс заявки на бронирование выведенное ранее!",
            reply_markup=UserRK.rk()
        )
        return
    
    access = data["access"]
    
    response = ReserveController.get_index(states=[3], index=index, token=access)
    if await check_user_response_exception(response, message, state):
        return
    
    await message.bot.delete_message(
        chat_id=message.chat.id,
        message_id=data["message_id"]
    )
    reserve: Reserve = response.get_data()

    response = PlaceController.get_free_period(
        reserve_begin=reserve.reserve_begin,
        reserve_end=reserve.reserve_end,
        page_index=0,
        token=access
    )
    if await check_user_response_exception(response, message, state):
        return
    
    response_data: list[Place] = response.get_data()

    if len(response.data) == 0:
        await message.answer(
            "Доступных парковочных мест для указаного бронирования не найдено",
            reply_markup=UserRK.rk()
        )
        await state.set_state(AuthState.user)
        return
    
    message = await message.answer(
        text=InlinePlace.print(
            list=response_data,
            page_index=0,
        ),
        reply_markup=InlinePlace.build()
    )
    await state.update_data(
        reserve_id=reserve.ID,
        message_id=message.message_id
    )
    await state.set_state(ReserveState.set_place_place)
    message.answer(
        text="Введите код парковочного места",
        reply_markup=UserRK.rk()
    )

@router.message(ReserveState.set_place_place)
async def command_set_place_id(message: Message, state: FSMContext):
    await state.set_state(AuthState.user)
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    access = data["access"]

    regexp = re.search("[A-Z][0-9]{3}", message.text)
    if regexp is None:
        await message.reply(
            "Необходимо ввести номер парковочного места"
        )
        return
    
    response = ReserveController.set_place(
        data["reserve_id"], 
        regexp.group(0),
        access
    )

    await check_user_response_exception(response, message, state)
    
    if response.is_exception():
        exception = response.get_exception()
        await message.reply(
            text=exception.message
        )
    else:
        exception = response.get_data()
        await message.reply(
            text=exception.message
        )
