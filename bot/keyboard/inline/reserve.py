from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .base_func import build_paginator_action, Inline
from core.domain.entity import Place, Reserve
import datetime

class InlineReserve(Inline):
    class GetReserveAction(IntEnum):
        delete = auto()
        sended = auto()
        accept = auto()
        payed = auto()

    class Callback(CallbackData, prefix='r'):
        page_index: int
        action: IntEnum

    @classmethod
    def create(cls, **kwargs):
        return InlineReserve.Callback(
            action=kwargs.get("kwargs").get("action"),
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, state: GetReserveAction = GetReserveAction.sended, page_index=0):
        obj = {
            InlineReserve.GetReserveAction.delete: "Удаленные",
            InlineReserve.GetReserveAction.sended: "Отправленные",
            InlineReserve.GetReserveAction.accept: "Принятые",
            InlineReserve.GetReserveAction.payed: "Оплаченные",
        }
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls = InlineReserve,
            page_index=page_index,
            kwargs={
                "action": state
            }
        )
        for en in InlineReserve.GetReserveAction:
            if en != state:
                builder.button(
                    text=obj[en],
                    callback_data=InlineReserve.Callback(
                        action=en,
                        page_index=page_index
                    ).pack(),
                )
        if page_index == 0:
            builder.adjust(1)
        else:
            builder.adjust(3, 1, 1, 1)

        return builder.as_markup(resize_keyboard=True)

    @classmethod
    def print(cls, list: list[Reserve], state: GetReserveAction = GetReserveAction.sended, page_index=0):
        message_text = f"История авторизаций\nСтраница {page_index+1}\n\n"
        message_text += " Места      Время начала            Время конца\n\n"
        
        for reserve_data in list:
            message_text += f"    {reserve_data.place_code}         "+\
                datetime.datetime.utcfromtimestamp(
                    reserve_data.reserve_begin
                ).strftime("%d.%m.%Y %H:%M:%S") + "         "+\
                datetime.datetime.utcfromtimestamp(
                    reserve_data.reserve_end
                ).strftime("%d.%m.%Y %H:%M:%S")+"\n"
        return message_text
    
class InlinePlace(Inline):
    class Callback(CallbackData, prefix='inline_place'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlineReserve.Callback(
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
    def print(cls, list: list, page_index=0):
        message_text = f"История авторизаций\nСтраница {page_index+1}\n\n"
        message_text += "   Нумерация       Код парковочного места   \n\n"
        
        index = 1
        for place_data in list:
            message_text += f"    {index}        {place_data.place_code}"
            index += 1
        return message_text
    