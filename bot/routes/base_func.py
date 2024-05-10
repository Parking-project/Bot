from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.requests import TokenController, MessageController
from core.domain.entity import ApiResponse
from bot.keyboard.reply import AuthRK

def send_message(access: str, text: str, message: Message, answer_tg_id: int):
    return MessageController.post(
        text=text,
        group_id=message.chat.id,
        message_id=message.message_id,
        answer_tg_id=answer_tg_id,
        token=access
    )

async def update_state(message: Message, state: FSMContext, **kwargs) -> dict[str]:
    data = await state.get_data()
    response: ApiResponse = TokenController.check_token(
        access=data.get("access"),
        refresh=data.get("refresh")
    )
    if response.is_exception():
        if message is not None:
            await message.answer(
                text=f"Пожалуйста авторизируйтесь заново",
                reply_markup=AuthRK.rk()
            )
        await state.clear()
        return None

    new_data = {
        "access": response.data.access,
        "refresh": response.data.refresh
    }
    new_data = await state.update_data(
        data=new_data,
        **kwargs
    )

    return new_data
