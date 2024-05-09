from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from bot.keyboard.inline.base_func import build_paginator_action
from .base_func import Inline

import datetime

class InlineAuthHistory(Inline):
    class Callback(CallbackData, prefix='auth_h'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlineAuthHistory.Callback(
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, page_index=0):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls=InlineAuthHistory,
            page_index=page_index
        )
        builder.adjust(3)

        return builder.as_markup(resize_keyboard=True)
    
    @classmethod
    def print(cls, list: list, page_index=0):
        message_text = f"История авторизаций\nСтраница {page_index+1}"
        message_text += "\n<b>Код пользователя                                           Дата авторизации\n\n</b>"
                            
        for auth_data in list:
            message_text += auth_data.user_id + "\t|\t" + \
                datetime.datetime.fromtimestamp(
                    auth_data.auth_date
                ).strftime("%d.%m.%Y %H:%M:%S") + "\n"
    
        return message_text

class InlineReserveHistory(Inline):
    class Callback(CallbackData, prefix='reserve_h'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlineReserveHistory.Callback(
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, page_index=0):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls=InlineReserveHistory,
            page_index=page_index
        )
        builder.adjust(3)

        return builder.as_markup(resize_keyboard=True)
    
    @classmethod
    def print(cls, list: list, page_index=0):
        message_text = f"История заявок на бронирование\nСтраница {page_index+1}"
        message_text += "\n<b>Код резервации                       Статус заяки\n\n</b>"
                            
        for reserve_data in list:
            message_text += reserve_data.reserve_id + " | "
            match(reserve_data.reserve_state):
                case 1:
                    message_text += "Удален\n"
                case 2:
                    message_text += "Отправлен\n"
                case 3:
                    message_text += "Одобрен\n"
                case 4:
                    message_text += "Оплачен\n"
    
        return message_text

class InlineTokenBlocList(Inline):
    class Callback(CallbackData, prefix='token_h'):
        page_index: int

    @classmethod
    def create(cls, **kwargs):
        return InlineReserveHistory.Callback(
            page_index=kwargs.get("page_index")
        )
    
    @classmethod
    def build(cls, page_index=0):
        builder: InlineKeyboardBuilder = build_paginator_action(
            cls=InlineTokenBlocList,
            page_index=page_index
        )
        builder.adjust(3)

        return builder.as_markup(resize_keyboard=True)
    
    @classmethod
    def print(cls, list: list, page_index=0):
        message_text = f"История авторизаций\nСтраница {page_index+1}"
        message_text += "\n<b>Код пользователя                                           Дата авторизации\n\n</b>"
                            
        for token_bloc in list:
            message_text += token_bloc.token_jti + "\t|\t" + \
                datetime.datetime.fromtimestamp(
                    token_bloc.token_create
                ).strftime("%d:%m:%Y %H:%M:%S") + "\n"
    
        return message_text