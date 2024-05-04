from aiogram.fsm.state import State, StatesGroup

class LogInState(StatesGroup):
    login = State()
    password = State()

    auth = State()