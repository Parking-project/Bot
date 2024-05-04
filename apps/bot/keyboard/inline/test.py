from aiogram.filters.callback_data import CallbackData

class TestCallback1(CallbackData, prefix='test_callback'):
    page_index: int
    name: str