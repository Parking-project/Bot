from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.routes.base_func import update_state
from bot.keyboard.reply import BaseRK

from core.domain.entity import User
from core.requests import TokenController

LOGIN = "user2"
PASSWORD = "pass123"

async def employee_auth(state: FSMContext, message: Message):
    data = await state.get_data()
    if data.get("access") is None:
        response = TokenController.login(LOGIN, PASSWORD)
        if response.is_exception():
            exception = response.get_exception()
            await message.reply(
                text=f"Произоша ошибка! {exception.message}",
                reply_markup=BaseRK.help_rk()
            )
            return
        
        response_data: User = response.get_data()
        await state.set_data(data={
                "access": response_data.access,
                "refresh": response_data.refresh
            }
        )
    data = await update_state(
        message=None,
        state=state,
        now_state=None
    )
    if data is None:
        return
    return data