from aiogram.fsm.state import State, StatesGroup

class Register_State(StatesGroup):
    LOGIN = State()
    PASSWORD = State()
    DISPLAY_NAME = State()