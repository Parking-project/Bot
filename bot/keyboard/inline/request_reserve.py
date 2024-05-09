from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto



from .base_func import Inline

class ReserveAction(IntEnum):
    delete = auto()
    approve = auto()

class InlineUserReserve(Inline):
    class Callback(CallbackData, prefix='urr'):
        message_id: int
        reserve_id: str

    @classmethod
    def create(cls, **kwargs):
        return InlineUserReserve.Callback(
            message_id=kwargs.get("message_id"),
            reserve_id=kwargs.get("reserve_id"),
        )
    
    @classmethod
    def build(cls, reserve_id: str, message_id: int):
        builder = InlineKeyboardBuilder()
        builder.button(
            text="Отменить",
            callback_data=InlineUserReserve.create(
                message_id=message_id,
                reserve_id=reserve_id
            ).pack(),
        )
        builder.adjust(1)

        return builder.as_markup(resize_keyboard=True)

class InlineBotReserve(Inline):
    class Callback(CallbackData, prefix='brr'):
        action: ReserveAction
        reserve_id: str
        chat_id: int | None
        message_id: int | None

    @classmethod
    def create(cls):
        pass
    
    @classmethod
    def build(cls):
        pass
