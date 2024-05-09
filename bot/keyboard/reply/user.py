from aiogram.utils.keyboard import ReplyKeyboardBuilder

class UserRK:    
    REQUEST_HELP = "Отправка сообщения техподдержке"
    
    GET_RESERVE = "Получить  заявки"
    GET_HISTORY_RESERVE = "Получить историю заявок"
    ADD_RESERVE = "Добавить бронирование"
    DELETE_RESERVE = "Удалить бронирование"
    SET_PLACE_RESERVE = "Выбор парковочного места"

    EXIT = "Выход из аккаунта"

    @classmethod
    def rk(cls):
        builder = ReplyKeyboardBuilder()
        builder.button(
            text=cls.GET_RESERVE
        )
        builder.button(
            text=cls.GET_HISTORY_RESERVE
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
