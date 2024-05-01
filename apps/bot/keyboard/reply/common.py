from aiogram.utils.keyboard import ReplyKeyboardBuilder

class ButtonRK:
    AUTH = "Авторизация"
    REG = "Регистрация"
    
    SEND_HELP = "Отправка сообщения техподдержке"
    RESERVE_REQUEST = "Просмотр заявки"
    EXIT = "Выход из аккаунта"

def base_rk():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text=ButtonRK.AUTH
    )
    builder.button(
        text=ButtonRK.REG
    )
    return builder.as_markup(resize_keyboard=True)

def auth_rk():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text=ButtonRK.RESERVE_REQUEST
    )
    builder.button(
        text=ButtonRK.SEND_HELP
    )
    builder.button(
        text=ButtonRK.EXIT
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
