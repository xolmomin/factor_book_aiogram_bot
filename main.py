import asyncio
import logging
import os
import sys
from typing import Any, Union, Dict, Iterable

from aiogram import Bot, Dispatcher, html, BaseMiddleware, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Filter, Command
from aiogram.types import Message, InlineQuery, InlineQueryResultPhoto, InlineQueryResultArticle, \
    InputTextMessageContent, BotCommand, KeyboardButton, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # @yangi123bot

dp = Dispatcher()
ADMIN_LIST = [514411336]

products = [
    {
        "id": 1,
        "title": "iPhone 9",
        "description": "An apple mobile which is nothing like apple",
        "price": 549,
        "discountPercentage": 12.96,
        "rating": 4.69,
        "stock": 94,
        "brand": "Apple",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/1/1.jpg",
            "https://cdn.dummyjson.com/product-images/1/2.jpg",
            "https://cdn.dummyjson.com/product-images/1/3.jpg",
            "https://cdn.dummyjson.com/product-images/1/4.jpg",
            "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg"
        ]
    },
    {
        "id": 2,
        "title": "iPhone X",
        "description": "SIM-Free, Model A19211 6.5-inch Super Retina HD display with OLED technology A12 Bionic chip with ...",
        "price": 899,
        "discountPercentage": 17.94,
        "rating": 4.44,
        "stock": 34,
        "brand": "Apple",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/2/1.jpg",
            "https://cdn.dummyjson.com/product-images/2/2.jpg",
            "https://cdn.dummyjson.com/product-images/2/3.jpg",
            "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg"
        ]
    },
    {
        "id": 3,
        "title": "Samsung Universe 9",
        "description": "Samsung's new variant which goes beyond Galaxy to the Universe",
        "price": 1249,
        "discountPercentage": 15.46,
        "rating": 4.09,
        "stock": 36,
        "brand": "Samsung",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/3/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/3/1.jpg"
        ]
    }
]


@dp.message(CommandStart())
async def start_handler(message: Message):
    btns = [
        [KeyboardButton(text='Kitoblar')],
        [KeyboardButton(text='Mening buyurtmalarim')],
        [KeyboardButton(text='Biz ijtimoiy tarmoqlarda'), KeyboardButton(text="Biz bilan bog'lanish")],
    ]
    rkb = ReplyKeyboardBuilder(btns)
    await message.answer('Assalomu alaykum! Tanlang.', reply_markup=rkb.as_markup(resize_keyboard=True))


@dp.message(F.text == 'Kitoblar')
async def start_handler(message: Message):
    btns = [
        [InlineKeyboardButton(text='IKAR', callback_data='category_1'),
         InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=' ')],
    ]
    ikb = InlineKeyboardBuilder(btns)
    await message.answer('Kategoriyalardan birini tanlang.', reply_markup=ikb.as_markup())


@dp.callback_query(F.text == 'Kitoblar')
async def start_handler(callback: CallbackQuery):
    pass


# @dp.inline_query()
# async def command_start_handler(inline_query: InlineQuery) -> None:
#     iqr = InlineQueryResultArticle(
#         id='1',
#         title='1984',
#         input_message_content=InputTextMessageContent(
#             message_text="nimadir"
#         ),
#         thumbnail_url='https://cdn.dummyjson.com/product-images/1/thumbnail.jpg',
#         description="Factor Books\n💵 Narxi: 49,000 so'm",
#     )
#     await inline_query.answer([iqr], cache_time=5)
#


async def on_startup(dispatcher: Dispatcher, bot: Bot):
    command_list = [
        BotCommand(command='start', description='Botni ishga tushirish'),
        BotCommand(command='help', description='Yordam')
    ]
    await bot.set_my_commands(command_list)


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    await bot.delete_my_commands()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
