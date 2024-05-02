from aiogram.types import InlineKeyboardMarkup, Message
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import IntEnum, auto

class AuthHistoryCallback(CallbackData, prefix='auth_history_callback'):
    page_index: int

class ReserveHistoryCallback(CallbackData, prefix='reserve_history_callback'):
    page_index: int

def auth_history_action(page_index=0):
    return build_action(cls=AuthHistoryCallback, page_index=page_index)

def reserve_history_action(page_index=0):
    return build_action(cls=ReserveHistoryCallback, page_index=page_index)

def build_action(cls, page_index):
    builder = InlineKeyboardBuilder()
    def create_button(text, page_index):
        builder.button(
            text=text,
            callback_data=cls(page_index=page_index).pack(),
        )
    if page_index != 0:
        create_button(text="<<", page_index=page_index-1)
    
    create_button(text="Вернуться", page_index=0)
    create_button(text=">>", page_index=page_index+1)
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)