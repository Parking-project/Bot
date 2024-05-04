from aiogram.filters.callback_data import CallbackData

class UserReserveCallback(CallbackData, prefix='user_reserve_callback'):
    message_id: int

class BotReserveCallback(CallbackData, prefix='bot_reserve_callback'):
    chat_id: int | None
    message_id: int | None