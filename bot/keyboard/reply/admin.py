from aiogram.utils.keyboard import ReplyKeyboardBuilder

class AdminRK:
    RESERVE_HISTORY = "История бронирований"
    AUTH_HISTORY = "Истрия авторизаций"
    TOKEN_HISTORY = "История токенов"
    EXIT = "Выход из аккаунта"

    @classmethod
    def rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=cls.RESERVE_HISTORY
        )
        builder.button(
            text=cls.AUTH_HISTORY
        )
        builder.button(
            text=cls.TOKEN_HISTORY
        )
        builder.button(
            text=cls.EXIT
        )
        builder.adjust(1)
        return builder.as_markup(resize_keyboard=True)
