from aiogram.fsm.context import FSMContext
from core.requests import TokenController
from core.domain.entity import ApiResponse

async def update_tokens(state: FSMContext) -> str:
    data = await state.get_data()
    response: ApiResponse = TokenController.check(access=data["access"], refresh=data["refresh"])
    if response.IsException():
        await state.clear()
        return
    await state.set_data(
        data={
            "access": response.data["access"],
            "refresh": response.data["refresh"]
        }
    )

