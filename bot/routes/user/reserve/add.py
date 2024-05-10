from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router

from bot.states import AuthState, ReserveState
from bot.keyboard.inline import InlineUserReserve
from bot.keyboard.reply import UserRK
from bot.routes.base_func import update_state

from core.requests import ReserveController
from core.domain.entity import ApiResponse


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
from core.domain.entity import ReserveAction

from ..base_handlers import check_user_response_exception

router = Router(name=__name__)

@router.message(ReserveState.add)
async def command_add_hours(message: Message, state: FSMContext):
    await state.set_state(AuthState.user)
    data = await update_state(
        message, 
        state
    )
    if data is None:
        return
    access = data["access"]
    
    try:
        hours: int = int(message.text)
    except:
        await message.reply(
            text="Необходимо ввести длительность в виде одного только числа",
            reply_markup=UserRK.rk()
        )
        return
    answer = await message.answer(
        text="***Отправка заявки***"
    )
    response: ApiResponse = ReserveController.post(
        chat_id=answer.chat.id,
        message_id=answer.message_id,
        hours=hours,
        token=access
    )
    
    if await check_user_response_exception(response, message, state):
        await answer.edit_text(
            text="Отправка заявки провалилась"
        )
    else:
        response_data: ReserveAction = response.get_data()
        await answer.edit_text(
            text="Заявка отправлена",
            reply_markup=InlineUserReserve.build(
                message_id=response_data.message_id,
                reserve_id=response_data.reserve_id
            )
        )
