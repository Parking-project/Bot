from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


from core.domain.entity import Place

from .base_func import build_paginator_action, Inline

class InlinePlace(Inline):
    class Callback(CallbackData, prefix='inline_place'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlinePlace.Callback(
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, page_index=0):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls = InlinePlace,
            page_index=page_index
        )
        builder.adjust(3)

        return builder.as_markup(resize_keyboard=True)

    @classmethod
    def print(cls, list: list[Place], page_index=0):
        message_text = f"Список свободных парковочных мест\nСтраница {page_index+1}\n\n"
        message_text += "  Код парковочного места   \n\n"
        
        for place_data in list:
            message_text += f"    {place_data.place_code}"
        return message_text
