from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from enum import IntEnum, auto

from .base_func import build_paginator_action, Inline

from core.domain.entity import Reserve

import datetime

class GetReserveAction(IntEnum):
    delete = auto()
    sended = auto()
    accept = auto()
    payed = auto()

class InlineReserve(Inline):
    state = {
        GetReserveAction.delete: "удаленные",
        GetReserveAction.sended: "отправленные",
        GetReserveAction.accept: "принятые",
        GetReserveAction.payed: "оплаченные",
    }

    class Callback(CallbackData, prefix='reserve'):
        is_actual: bool
        page_index: int
        action: GetReserveAction

    @classmethod
    def create(cls, **kwargs):
        return InlineReserve.Callback(
            is_actual=kwargs.get("kwargs").get("is_actual"),
            page_index=kwargs.get("page_index"),
            action=kwargs.get("kwargs").get("action"),
        )
    
    @classmethod
    def build(
        cls,
        is_actual: bool,
        page_index: int=0,
        state: GetReserveAction = GetReserveAction.sended
    ):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls = InlineReserve,
            page_index=page_index,
            kwargs={
                "action": state,
                "is_actual": is_actual,
            }
        )
        for en in GetReserveAction:
            if en != state:
                builder.button(
                    text=InlineReserve.state[en],
                    callback_data=InlineReserve.Callback(
                        action=en,
                        is_actual=is_actual,
                        page_index=0
                    ).pack(),
                )
        if page_index == 0:
            builder.adjust(1, 1)
        else:
            builder.adjust(3, 1)

        return builder.as_markup(resize_keyboard=True)

    @classmethod
    def print(
        cls,
        is_actual: bool,
        list: list[Reserve],
        page_index: int=0,
        state: GetReserveAction = GetReserveAction.sended
    ):
        if is_actual:
            message_text = f"Актуальные бронирования"
        else:
            message_text = f"История бронирований"
        message_text += f" ({InlineReserve.state[state]} заявки)\nСтраница {page_index+1}\n\n"
        message_text += " Места       Время начала                 Время окончания\n\n"
        
        for reserve_data in list:
            message_text += f"  {reserve_data.place_code}         "+\
                datetime.datetime.fromtimestamp(
                    reserve_data.reserve_begin
                ).strftime("%d.%m.%Y %H:%M:%S") + "         "+\
                datetime.datetime.fromtimestamp(
                    reserve_data.reserve_end
                ).strftime("%d.%m.%Y %H:%M:%S")+"\n"
        return message_text

class InlineProcessReserve(Inline):
    class Callback(CallbackData, prefix='process_reserve'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlineProcessReserve.Callback(
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, page_index=0):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls = InlineProcessReserve,
            page_index=page_index
        )
        builder.adjust(3)

        return builder.as_markup(resize_keyboard=True)

    @classmethod
    def print(cls, list: list[Reserve], page_index=0):
        message_text = f"Актуальные бронирования \nСтраница {page_index+1}\n\n"
        message_text += "Индекс   Места       Время начала                 Время окончания\n\n"
        
        index = page_index * 10
        for reserve_data in list:
            message_text += f"       {index}"
            message_text += f"          {reserve_data.place_code}"
            message_text += "         " + datetime.datetime.fromtimestamp(
                    reserve_data.reserve_begin
                ).strftime("%d.%m.%Y %H:%M:%S")
            message_text += "         " + datetime.datetime.fromtimestamp(
                    reserve_data.reserve_end
                ).strftime("%d.%m.%Y %H:%M:%S")
            message_text += "\n"
            index += 1
        return message_text

class InlineApproveReserve(Inline):
    class Callback(CallbackData, prefix='approve_reserve'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlineProcessReserve.Callback(
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, page_index=0):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls = InlineProcessReserve,
            page_index=page_index
        )
        builder.adjust(3)

        return builder.as_markup(resize_keyboard=True)

    @classmethod
    def print(cls, list: list[Reserve], page_index=0):
        message_text = f"Одобренные бронирования \nСтраница {page_index+1}\n\n"
        message_text += "Индекс   Места       Время начала                 Время окончания\n\n"
        
        index = page_index * 10
        for reserve_data in list:
            message_text += f"       {index}"
            message_text += f"          {reserve_data.place_code}"
            message_text += "         " + datetime.datetime.fromtimestamp(
                    reserve_data.reserve_begin
                ).strftime("%d.%m.%Y %H:%M:%S")
            message_text += "         " + datetime.datetime.fromtimestamp(
                    reserve_data.reserve_end
                ).strftime("%d.%m.%Y %H:%M:%S")
            message_text += "\n"
            index += 1
        return message_text
