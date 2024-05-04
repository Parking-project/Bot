from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    login = State()
    password = State()
    display_name = State()