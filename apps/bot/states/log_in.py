from aiogram.fsm.state import State, StatesGroup

class LogIn_State(StatesGroup):
    login = State()
    password = State()

    auth = State()