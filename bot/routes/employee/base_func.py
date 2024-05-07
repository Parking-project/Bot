from bot.routes.base_func import update_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.requests import TokenController
from bot.keyboard.reply import BaseRK

LOGIN = "user2"
PASSWORD = "pass123"

async def employee_auth(state: FSMContext, message: Message):
    data = await state.get_data()
    if data.get("access") is None:
        response = TokenController.login(LOGIN, PASSWORD)
        if response.IsException():
            
            await message.reply(
                text=f"Не удалось отправить сообщение! {response.data}",
                reply_markup=BaseRK.help_rk()
            )
            return
        await state.set_data(data={
                "access": response.data["tokens"]["access"],
                "refresh": response.data["tokens"]["refresh"]
            }
        )
    data = await update_state(
        message=None,
        state=state,
        now_state=None
    )
    if data is None:
        return
    return data["access"]