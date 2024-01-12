from aiogram.utils.keyboard import  ReplyKeyboardBuilder, InlineKeyboardBuilder

def create_builder(names):
    builder = ReplyKeyboardBuilder()
    for n in names:
        builder.button(n)
    return builder.adjust(2).as_markup(resize_keyboard=True)


