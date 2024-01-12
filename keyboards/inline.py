from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

for_old = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Заново",),
            InlineKeyboardButton(text="Продолжить")
         ]
    ]
)
