from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from utils.states import Reg, Game
from utils.ramin import *
import asyncio
from keyboards import builder, inline, reply
from aiogram.fsm.state import default_state

router = Router()

@router.message(Game.start, F.text == 'Да')
async def start_game(message: Message, state: FSMContext):
    await state.set_state(Game.new_evil)
    await create_evil(message, state)

@router.message(Game.start)
async def error_start_game(message: Message, state: FSMContext):
    await state.set_state(default_state)
    await message.answer("Хочешь заново зарегистрироваться? Используй /reg")

@router.message(Game.new_evil)
async def create_evil(message: Message, state: FSMContext):
    await state.set_state(Game.choose)
    evil = BAD_BOY.create_enemy()
    await state.update_data(evil=evil)
    await message.answer(f'Вы встретили соперника.\n{evil}')
    await asyncio.sleep(1)
    await message.answer(text='Готов с ним сразиться?',
                         reply_markup=builder.inline_builder(["Да","Нет"]))

@router.message(Game.choose, F.data == 'Да')
async def yes_fight(message: Message, state: FSMContext):
    dct = await state.get_data()
    hero = dct['hero']
    evil = dct['evil']
    result = hero.ataka()
    if result:
        await message.answer('Легенда пала')
        await create_evil(message, state)
    else:
        evil.atack(hero)
        await message.answer('')

@router.message(Game.choose, F.data == 'Нет')
async def no_fight(message: Message, state: FSMContext):
    pass
@router.message(Game.choose)
async def yes_fight(message: Message, state: FSMContext):
    pass

