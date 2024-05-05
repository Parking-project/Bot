from aiogram.utils.keyboard import ReplyKeyboardBuilder

class AdminRK:
    RESERVE_HISTORY = "История бронирований"
    AUTH_HISTORY = "Истрия авторизаций"
    TOKEN_HISTORY = "История токенов"
    EXIT = "Выход из аккаунта"

    @classmethod
    def rk():
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=AdminRK.RESERVE_HISTORY
        )
        builder.button(
            text=AdminRK.AUTH_HISTORY
        )
        builder.button(
            text=AdminRK.TOKEN_HISTORY
        )
        builder.button(
            text=AdminRK.EXIT
        )
        builder.adjust(1)
        return builder.as_markup(resize_keyboard=True)
