from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils import db
from keyboards import builder, inline, reply
from data import dictionry
from utils.states import Reg, Game
from filters.users import Check_old_user, Check_hero_having
from aiogram.fsm.state import default_state

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет, это игра для таких ноунеймов, как ты')
    await message.answer('Используй /reg для выбора героя\nА /game для начала новой игры')

@router.message(Command('reg'))
async def cmd_reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Напиши имя героя')

@router.message(Command('game'), Check_hero_having())
async def cmd_game_with(message: Message, state: FSMContext):
    await state.set_state(Game.new_evil)
    info = await state.get_state()
    await message.answer(f'Твои показатели:\nЗдоровье: {None}\nУрон: {None}')


@router.message(Command('game'), Check_hero_having())
async def cmd_game_without(message: Message, state: FSMContext):
    await message.answer('У тебя нет героя( Пройди, пожалуйста, регистрацию')
    await cmd_reg(message, state)



