from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import logging
import asyncio
import os
from handlers import commands, registration, game

load_dotenv()
TOKEN = os.getenv('TOKEN')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(registration.router)
    dp.include_router(game.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
