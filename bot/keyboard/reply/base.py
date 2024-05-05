from aiogram.utils.keyboard import ReplyKeyboardBuilder

class BaseRK:
    RESERVE = "Описание"
    HELP = "Помощь"

    @classmethod
    def reserve_rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=BaseRK.RESERVE
        )
        return builder.as_markup(resize_keyboard=True)
    
    @classmethod
    def help_rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=BaseRK.HELP
        )
        return builder.as_markup(resize_keyboard=True)
