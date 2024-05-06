from aiogram.utils.keyboard import ReplyKeyboardBuilder

class UserRK:    
    REQUEST_HELP = "Отправка сообщения техподдержке"
    
    GET = "Получить заявки"
    GET_FREE_PLACE = "Свободные места"
    ADD_RESERVE = "Добавить"
    DELETE_RESERVE = "Удалить"
    SET_PLACE_RESERVE = "Выбор парковочного места"

    EXIT = "Выход из аккаунта"

    @classmethod
    def rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=cls.GET
        )
        builder.button(
            text=cls.GET_FREE_PLACE
        )
        builder.button(
            text=cls.ADD_RESERVE
        )
        builder.button(
            text=cls.DELETE_RESERVE
        )
        builder.button(
            text=cls.SET_PLACE_RESERVE
        )
        builder.button(
            text=cls.REQUEST_HELP
        )
        builder.button(
            text=cls.EXIT
        )
        builder.adjust(1)
        return builder.as_markup(resize_keyboard=True)
