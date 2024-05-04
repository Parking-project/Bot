from aiogram.fsm.state import State, StatesGroup

class HelpState(StatesGroup):
    text = State()
    documents = State()