import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand, KeyboardButton, InlineKeyboardButton, CallbackQuery
from aiogram.utils.i18n import gettext as _, I18n, FSMI18nMiddleware
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
# from dotenv import load_dotenv
from aiogram.utils.i18n import lazy_gettext as __
from redis_dict import RedisDict

from buttons import BOOK_TEXT

database = RedisDict()
# load_dotenv()
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
        [KeyboardButton(text=_(BOOK_TEXT))],
        [KeyboardButton(text=_('Mening buyurtmalarim'))],
        [KeyboardButton(text=_('Biz ijtimoiy tarmoqlarda')), KeyboardButton(text=_("Biz bilan bog'lanish"))],
        [KeyboardButton(text=_('Til almashtirish'))],
    ]
    rkb = ReplyKeyboardBuilder(btns)
    await message.answer(_('Assalomu alaykum! Tanlang. Hurmatli {name}'.format(name=message.from_user.full_name)),
                         reply_markup=rkb.as_markup(resize_keyboard=True))


@dp.message(F.text == __(BOOK_TEXT))
async def start_handler(message: Message):
    btns = [
        [InlineKeyboardButton(text='IKAR', callback_data='category_1'),
         InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=' ')],
    ]
    ikb = InlineKeyboardBuilder(btns)
    await message.answer('Kategoriyalardan birini tanlang.', reply_markup=ikb.as_markup())


@dp.message(F.text == __(BOOK_TEXT))
async def start_handler(message: Message):
    btns = [
        [InlineKeyboardButton(text='IKAR', callback_data='category_1'),
         InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=' ')],
    ]
    ikb = InlineKeyboardBuilder(btns)
    await message.answer('Kategoriyalardan birini tanlang.', reply_markup=ikb.as_markup())

@dp.message(F.text == __(BOOK_TEXT))
async def start_handler(message: Message):
    btns = [
        [InlineKeyboardButton(text='IKAR', callback_data='category_1'),
         InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=' ')],
    ]
    ikb = InlineKeyboardBuilder(btns)
    await message.answer('Kategoriyalardan birini tanlang.', reply_markup=ikb.as_markup())


@dp.message(F.text == __('Til almashtirish'))
async def start_handler(message: Message):
    btns = [
        [InlineKeyboardButton(text='uzbek', callback_data='lang_uz'),
         InlineKeyboardButton(text="english", callback_data='lang_en')],
    ]
    ikb = InlineKeyboardBuilder(btns)
    await message.answer(_('Tilni tanlang'), reply_markup=ikb.as_markup())


@dp.callback_query(F.data.startswith('lang_'))
async def start_handler(callback: CallbackQuery, state: FSMContext):
    lang_code = callback.data.split('lang_')[-1]
    await state.set_data({'locale': lang_code})
    await callback.answer(_('Til tanlandi', locale=lang_code))


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

    i18n = I18n(path="locales", default_locale="en", domain="messages")
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
