from aiogram.utils.keyboard import InlineKeyboardBuilder

def build_paginator_action(cls, page_index):
    builder = InlineKeyboardBuilder()
    def create_button(text, page_index):
        builder.button(
            text=text,
            callback_data=cls(page_index=page_index).pack(),
        )
    
    if page_index != 0:
        create_button(text="<<", page_index=page_index-1)
        create_button(text="Вернуться", page_index=0)
    create_button(text=">>", page_index=page_index+1)
    builder.adjust(3)

    return builder.as_markup(resize_keyboard=True)