from aiogram.fsm.state import StatesGroup, State

class Reg(StatesGroup):
    name = State()
    rasa = State()
    choose = State()
    static = State()

class Game(StatesGroup):
    start = State()
    new_evil = State()
    choose = State()
    run = State()