from aiogram.utils.keyboard import ReplyKeyboardBuilder

class AuthRK:
    AUTH = "Авторизация"
    REG = "Регистрация"
    END = "Завершить"

    @classmethod
    def rk(cls, in_proccess: bool = False):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=cls.AUTH
        )
        builder.button(
            text=cls.REG
        )
        if in_proccess:
            builder.button(
                text=cls.END
            )
        builder.adjust(1)
        return builder.as_markup(resize_keyboard=True)
