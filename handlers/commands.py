from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils import db
from keyboards import builder, inline, reply
from data import dictionry

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    us = db.dbselect('Users', 'userid')
    if message.from_user.id in us:
        await message.answer('С Возвращением воин!')
        await message.answer('Хочешь начать игру сначала или продолжить?',
                             reply_markup=builder.create_builder(['Продолжить', "Заново"]))
    else:
        await message.answer('Привет! Представься, воин')
        await state.set_state(St.set_name)