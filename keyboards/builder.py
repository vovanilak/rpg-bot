from aiogram.utils.keyboard import  ReplyKeyboardBuilder, InlineKeyboardBuilder

def reply_builder(names):
    builder = ReplyKeyboardBuilder()
    for n in names:
        builder.button(text=n)
    return builder.adjust(2).as_markup(resize_keyboard=True)

def inline_builder(lst):
    builder = InlineKeyboardBuilder()
    for l in lst:
        builder.button(text=l, callback_data=l)
    return builder.adjust(2).as_markup()


