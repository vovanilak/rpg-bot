from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import *
from keyboards import builder, reply, inline
from utils.ramin import *

router = Router()

@router.message(Reg.name)
async def set_name(message: Message, state: FSMContext):
    await state.set_state(Reg.rasa)
    await state.update_data(id=message.from_user.id,
                            username=message.from_user.username,
                            name=message)
    await message.answer(text='Выбери, пожалуйста, расу',
                         reply_markup=builder.reply_builder(Hero.rasas))

@router.message(Reg.rasa, F.text.in_(Hero.rasas))
async def set_ras(message: Message, state: FSMContext):
    dct = await state.get_data()
    hero = Hero.create_hero(dct['name'], message.text)
    await state.update_data(hero=hero, rasa=message.text)
    await state.set_state(Game.start)
    await message.answer(text='Готов начать?',
                         reply_markup=builder.reply_builder(["Да"]))

@router.message(Reg.rasa)
async def error_set_ras(message: Message, state: FSMContext):
    await message.answer('Такой расы не( Выбери из списка',
                         reply_markup=builder.reply_builder(Hero.rasas))


