from aiogram.fsm.state import State, StatesGroup

class ReserveState(StatesGroup):
    add = State()
    delete = State()
    set_place_reserve = State()
    set_place_place = State()
    get_free = State()
    