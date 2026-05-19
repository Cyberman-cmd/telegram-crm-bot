from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    name = State()
    phone = State()
    email = State()
    address = State()
    comment = State()