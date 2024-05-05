from aiogram.utils.keyboard import ReplyKeyboardBuilder

class AuthRK:
    AUTH = "Авторизация"
    REG = "Регистрация"

    @classmethod
    def rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=AuthRK.AUTH
        )
        builder.button(
            text=AuthRK.REG
        )
        return builder.as_markup(resize_keyboard=True)
