from aiogram.fsm.state import StatesGroup, State

class Reg(StatesGroup):
    name = State()
    rasa = State()
    choose = State()
    static = State()

class Game(StatesGroup):
    new_evil = State
    yes = State()
    no = State()
    run = State()