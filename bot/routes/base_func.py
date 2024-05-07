from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.requests import TokenController, MessageController
from core.domain.entity import ApiResponse

def send_message(access: str, text: str, message: Message, answer_tg_id: int):
    return MessageController.post(
        text=text,
        group_id=message.chat.id,
        message_id=message.message_id,
        answer_tg_id=answer_tg_id,
        token=access
    )

async def update_state(message: Message, state: FSMContext, now_state, **kwargs) -> dict[str]:
    data = await state.get_data()
    await state.clear()
    response: ApiResponse = TokenController.check(access=data.get("access"), refresh=data.get("refresh"))
    if response.IsException():
        if message is not None:
            await message.answer(
                text="Пожалуйста авторизируйтесь заново"
            )
        return None
    await state.set_state(
        state=now_state
    )

    new_data = {
        "access": response.data["access"],
        "refresh": response.data["refresh"]
    }
    for key, value in kwargs.items():
        if value is None:
            new_data[key] = data[key]
        else:
            new_data[key] = value
    await state.set_data(
        data=new_data
    )
    return new_data



