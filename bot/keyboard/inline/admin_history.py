from aiogram.filters.callback_data import CallbackData
from bot.keyboard.inline.base_func import build_paginator_action

class AuthHistoryCallback(CallbackData, prefix='auth_history_callback'):
    page_index: int

class ReserveHistoryCallback(CallbackData, prefix='reserve_history_callback'):
    page_index: int

class TokenBlocListCallback(CallbackData, prefix='token_bloclist_callback'):
    page_index: int

def auth_history_action(page_index=0):
    return build_paginator_action(cls=AuthHistoryCallback, page_index=page_index)

def reserve_history_action(page_index=0):
    return build_paginator_action(cls=ReserveHistoryCallback, page_index=page_index)

def token_bloclist_action(page_index=0):
    return build_paginator_action(cls=TokenBlocListCallback, page_index=page_index)
