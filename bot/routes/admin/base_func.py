from core.domain.entity import AuthHistory, ReserveHistory, TokenBlocList
import datetime

def auth_history_print(auth_history: list[AuthHistory], page_index):
    message_text = f"История авторизаций\nСтраница {page_index+1}"
    message_text += "\n<b>Код пользователя                                           Дата авторизации\n\n</b>"
                          
    for auth_data in auth_history:
        message_text += auth_data.user_id + "\t|\t" + \
            datetime.datetime.utcfromtimestamp(
                auth_data.auth_date
            ).strftime("%d:%m:%Y %H:%M:%S") + "\n"
   
    return message_text

def reserve_history_print(reserve_history: list[ReserveHistory], page_index):
    message_text = f"История заявок на бронирование\nСтраница {page_index+1}"
    message_text += "\n<b>Код резервации                       Статус заяки\n\n</b>"
                          
    for reserve_data in reserve_history:
        message_text += reserve_data.reserve_id + " | "
        match(reserve_data.reserve_state):
            case 0:
                message_text += "Удален\n"
                break
            case 1:
                message_text += "Отправлен\n"
                break
            case 2:
                message_text += "Одобрен\n"
                break
            case 3:
                message_text += "Оплачен\n"
                break
   
    return message_text

def token_bloclist_print(token_bloclist: list[TokenBlocList], page_index):
    message_text = f"История авторизаций\nСтраница {page_index+1}"
    message_text += "\n<b>Код пользователя                                           Дата авторизации\n\n</b>"
                          
    for token_bloc in token_bloclist:
        message_text += token_bloc.token_jti + "\t|\t" + \
            datetime.datetime.utcfromtimestamp(
                token_bloc.token_create
            ).strftime("%d:%m:%Y %H:%M:%S") + "\n"
   
    return message_text