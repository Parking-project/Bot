from aiogram.utils.keyboard import ReplyKeyboardBuilder

class UserRK:    
    REQUEST_HELP = "Отправка сообщения техподдержке"
    RESERVE_REQUEST = "Просмотр заявки"
    EXIT = "Выход из аккаунта"

    @classmethod
    def rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=UserRK.RESERVE_REQUEST
        )
        builder.button(
            text=UserRK.REQUEST_HELP
        )
        builder.button(
            text=UserRK.EXIT
        )
        builder.adjust(1)
        return builder.as_markup(resize_keyboard=True)
