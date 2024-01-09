from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv
import logging
from dictionry import *
import asyncio
import os
from utils import *
from keyboards import *
from person import Hero, Evil
from rpg_ramin import *

load_dotenv()


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
users = {}
compon = {'name': None, 'hero': None, 'evil': None}

class St(StatesGroup):
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


@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    us = dbselect('Users', 'userid')
    if message.from_user.id in us:
        await message.answer('С Возвращением воин!')
        await message.answer('Хочешь начать игру сначала или продолжить?',
                             reply_markup=old_user.as_markup())
    else:
        await message.answer('Привет! Представься, воин')
        await state.set_state(St.set_name)

@dp.message(StateFilter(St.for_old))
async def next_old(message: Message, state: FSMContext):
    txt = message.text
    if txt == 'Заново':
        await message.answer('Отлично! Введи свой имя')
        await state.set_state(St.set_name)
    elif txt == 'Продолжить':
        await message.answer('Твои характеристики')

@dp.message(StateFilter(St.set_name))
async def step_set_name(message: Message, state: FSMContext):
    global users
    users[message.from_user.id] = compon
    users[message.from_user.id]['name'] = message.text
    await message.answer(f'Выбери расу\n{Hero.rasas}', reply_markup=key_ras.as_markup(resize_keyboard=True))
    await state.set_state(St.set_rasa)


@dp.message(F.text.in_(Hero.rasas), StateFilter(St.set_rasa))
async def step_set_rasa(message: Message, state: FSMContext):
    global users
    users[message.from_user.id]['hero'] = Hero.create_hero(users[message.from_user.id]['name'], message.text)
    #await message.answer(f'Твои характиристики\n{hero.__str__()}') #########################
    await asyncio.sleep(1)
    await message.answer('Отлично! Ты готов к бою?', reply_markup=key_yes.as_markup())
    await state.set_state(Game.start)

@dp.message(StateFilter(St.set_rasa))
async def step_not_set_rasa(message: Message):
    await message.answer('Нет такой расы. Попробуй снова', reply_markup=key_ras.as_markup(resize_keyboard=True))

@dp.message(F.text.in_(('Да⚔️', 'Назад')), StateFilter(Game.start))
async def step_ready(message: Message, state: FSMContext):
    if message.text == 'Да⚔️':
        global users
        users[message.from_user.id]['evil'] = BAD_BOY.create_enemy()
        #await message.answer(f'Тебе попался {evil.__str__()}') ##########################
        await message.answer('Готов с ним сразиться?', reply_markup=key_fight.as_markup())
        await state.set_state(Game.choose)
    elif message.text == 'Назад':
        await state.set_state(St.set_name)

@dp.message(StateFilter(Game.start))
async def step_not_ready(message: Message):
    await message.answer('Ты уверен, воин?', reply_markup=key_yes.as_markup())

@dp.message(F.text.in_(('Сразиться', 'Убежать')),StateFilter(Game.choose))
async def step_choose(message: Message, state: FSMContext):
    global users
    if message.text == 'Сразиться':
        res = users[message.from_user.id]['hero'].ataka(users[message.from_user.id]['evil'])
        if res:
            users[message.from_user.id]['evil'].ataka(users[message.from_user.id]['hero'])
            await message.anwer('Готов с ним сразиться?', reply_markup=key_fight.as_markup())
            await state.set_state(Game.start)
    elif message.text == 'Убежать':
        coin = r.choice([0, 1])
        if coin:
            await message.answer("Игра в Дашу питишественуцу не удолась вас побили ")
            users[message.from_user.id]['evil'].ataka(users[message.from_user.id]['hero'])
            await state.set_state(Game.start)
            await message.answer('Готов с ним сразиться?', reply_markup=key_fight.as_markup())
        else:
            await state.set_state(Game.start)
            await message.answer("ВЫ сбежали пока что. Продолжить?", reply_markup=key_yes.as_markup())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
