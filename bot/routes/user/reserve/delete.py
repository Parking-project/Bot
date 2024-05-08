from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import HelpState, AuthState, ReserveState
from bot.keyboard.reply import UserRK
from bot.routes.base_func import update_state, send_message
from bot.keyboard.inline import InlineProcessReserve

from core.requests import ReserveController

from config import TelegramConfig

router = Router(name=__name__)

@router.message(AuthState.user, F.text == UserRK.DELETE_RESERVE)
@router.message(HelpState.text, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.add, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.delete, F.text == UserRK.DELETE_RESERVE)
@router.message(HelpState.documents, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.get_free, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.set_place_place, F.text == UserRK.DELETE_RESERVE)
@router.message(ReserveState.set_place_reserve, F.text == UserRK.DELETE_RESERVE)
@router.message(AuthState.user, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(HelpState.text, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.add, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.delete, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(HelpState.documents, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.get_free, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.set_place_place, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
@router.message(ReserveState.set_place_reserve, Command(BotCommand(command="delete_reserve", description="Удалить бронирование")))
async def command_delete(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=ReserveState.delete
    )
    if data is None:
        return
    access = data["access"]
    
    # Вывести список доступных для удаления бронирований
    list = ReserveController.get_process(
        page_index=0,
        token=access
    )
    
    if list.IsException():
        await message.reply(
            text="Операция провалилась"
        )
        return
    message = await message.answer(
        text=InlineProcessReserve.print(
            list=list.data,
            page_index=0,
        ),
        reply_markup=InlineProcessReserve.build()
    )
    await state.update_data(message_id=message.message_id)

@router.message(ReserveState.delete)
async def command_delete_id(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=AuthState.user
    )
    if data is None:
        return
    
    try:
        index = int(message.text)
    except:
        await message.reply(
            text="Необходимо ввести только индекс заявки на бронирование выведенное ранее!"
        )
        return
    
    access = data["access"]


    response = ReserveController.delete_index(
        reserve_index=index,
        token=access
    )
    if response.IsException():
        await message.answer(
            f"Удаление заявки провалилось"
        )
        return
    await message.answer(
        f"Заявка успешно удалена"
    )