from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import  ReplyKeyboardBuilder, InlineKeyboardBuilder
from rpg_ramin import Hero
from utils import *

old_user = InlineKeyboardBuilder()
old_user.add(InlineKeyboardButton(text='Заново'), InlineKeyboardButton(text='Продолжить'))
old_user.adjust(1)

key_ras = ReplyKeyboardBuilder()
#sel = dbselect('Hero', 'name')
for r in Hero.rasas:
    key_ras.button(text=r)
key_ras.adjust(2, 2)

key_yes = ReplyKeyboardBuilder().add(
    KeyboardButton(text='Да⚔️'),
    KeyboardButton(text='Назад'))

key_fight = ReplyKeyboardBuilder().add(
    KeyboardButton(text='Сразиться'),
    KeyboardButton(text='Убежать')).adjust(2)

