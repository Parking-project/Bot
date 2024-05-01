from aiogram.fsm.state import State, StatesGroup

class Register_State(StatesGroup):
    login = State()
    password = State()
    display_name = State()