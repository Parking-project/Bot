from core.domain.entity import Place
import datetime

def place_print(place_list: list[Place], page_index):
    message_text = f"История авторизаций\nСтраница {page_index+1}\n\n"
    message_text += "   Нумерация       Код парковочного места   \n\n"
    
    index = 1
    for place in place_list:
        message_text += f"    {index}        {place.place_code}"
        index += 1
    return message_text