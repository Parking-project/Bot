from aiogram.fsm.state import State, StatesGroup

class AuthState(StatesGroup):
    user = State()
    admin = State()