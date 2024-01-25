from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from utils.states import Reg, Game
from utils.ramin import *
import asyncio
from keyboards import builder, inline, reply
from aiogram.fsm.state import default_state
import random

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
    evil = BAD_BOY.create_enemy()
    await state.update_data(evil=evil)
    await state.set_state(Game.choose)
    await message.answer(f'Вы встретили соперника.\n{evil}')
    await message.answer(text='Готов с ним сразиться?',
                         reply_markup=builder.reply_builder(["Да","Нет"]))

@router.message(Game.choose, F.text == 'Да')
async def yes_fight(message: Message, state: FSMContext):
    print("You are in choose_yes")
    dct = await state.get_data()
    hero = dct['hero']
    evil = dct['evil']
    result = hero.ataka(evil)
    if result:
        print("You are in choose_yes")
        await state.update_data(hero=hero, evil=evil)
        await state.set_state(Game.new_evil)
        await message.answer('Легенда пала')
        await create_evil(message, state)
    else:
        res = evil.atack(hero)
        if res:
            await state.update_data(hero=hero, evil=evil)
            await message.answer('Характеристики злодея {evil}')
            await message.answer('Ваши характеристики {hero}')
            await message.answer(f'Продолжить бой?',
                                 reply_markup=builder.inline_builder(["Да", "Нет"]))
        else:
            await state.update_data(hero=None, evil=None)
            await state.set_state(Game.start)
            await message.answer('Вы проиграли(')
            await message.answer("Хотите выбрать другую расу или сразу начать игру заново?",
                                 reply_markup=builder.inline_builder(["Да", "Нет"]))


@router.message(Game.choose, F.text == 'Нет')
async def no_fight(message: Message, state: FSMContext):
    print("You are in choose_no")
    db = await state.get_data()
    hero, evil = db['hero'], db['evil']
    res = random.randint(0,1)
    if res:
        await state.update_data(hero=hero, evil=evil)
        await message.answer('Характеристики злодея {evil}')
        await message.answer('Ваши характеристики {hero}')
        await message.answer(f'Продолжить бой?',
                             reply_markup=builder.inline_builder(["Да", "Нет"]))
    else:
        await state.set_state(Game.new_evil)
        await message.answer(f'Вам удалось сбежать')
        await create_evil(message, state)



@router.message(Game.choose)
async def yes_fight(message: Message, state: FSMContext):
    await message.answer('No')

