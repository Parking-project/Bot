from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.requests import TokenController, MessageController
from core.domain.entity import ApiResponse

def send_message(access: str, text: str, message: Message, answer_tg_id: int):
    return MessageController.post(
        token=access,
        text=text,
        group_id=message.from_user.id,
        message_id=message.message_id,
        answer_tg_id=answer_tg_id
    )

async def update_state_tokens(message: Message, state: FSMContext, now_state) -> dict[str]:
    data = await state.get_data()
    await state.clear()
    response: ApiResponse = TokenController.check(access=data.get("access"), refresh=data.get("refresh"))
    if response.IsException():
        await message.answer(
            text="Пожалуйста авторизируйтесь заново"
        )
        return None
    data = {
        "access": response.data["access"],
        "refresh": response.data["refresh"]
    }
    await state.set_state(
        state=now_state
    )
    await state.set_data(
        data=data
    )
    return data



