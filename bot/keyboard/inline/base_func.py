from aiogram.utils.keyboard import InlineKeyboardBuilder

class Inline:
    @classmethod
    def create(cls, **kwargs):
        pass
    
    @classmethod
    def build(cls, page_index=0):
        pass
    
    @classmethod
    def print(cls, list: list, page_index=0):
        pass

    
def build_paginator_action(cls: Inline, page_index: int, **kwargs):
    builder = InlineKeyboardBuilder()
    def create_button(text, page_index: int):
        builder.button(
            text=text,
            callback_data=cls.create(
                page_index=page_index,
                **kwargs
            ).pack(),
        )
    if page_index != 0:
        create_button(text="<<", page_index=page_index-1)
        create_button(text="Вернуться", page_index=0)
    create_button(text=">>", page_index=page_index+1)

    return builder