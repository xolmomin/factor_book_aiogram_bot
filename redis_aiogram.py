import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from redis_dict import RedisDict

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT')
database = RedisDict('users_redis', host=REDIS_HOST, port=REDIS_PORT)
TOKEN = os.getenv("BOT_TOKEN")  # @yangi123bot

dp = Dispatcher()
ADMIN_LIST = [514411336]


@dp.message(CommandStart())
async def start_handler(message: Message):
    database[str(message.from_user.id)] = message.from_user.model_dump(
        include={'first_name', 'last_name', 'username', 'id'}
    )
    await message.answer('Hello user')


@dp.message(F.from_user.id.in_(ADMIN_LIST))
async def start_handler(message: Message):
    ids = '\n'.join(database.keys())
    await message.answer(f'userlar idsi. \n{ids}')


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
