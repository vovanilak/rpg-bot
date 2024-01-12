from aiogram.fsm.state import StatesGroup, State

class Reg(StatesGroup):
    for_old = State()
    set_name = State()
    set_rasa = State()
    static = State()

class Game(StatesGroup):
    start = State()
    choose = State()
    yes = State()
    no = State()
    run = State()