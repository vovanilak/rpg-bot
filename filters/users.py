from aiogram.filters import BaseFilter
from aiogram.types import Message
from utils.db import dbselect
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

class Check_old_user(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id in dbselect('Users', column='userid')


class Check_hero_having(BaseFilter):
    async def __call__(self, state: FSMContext = default_state):
        info = await state.get_data()
        return 'hero' in info