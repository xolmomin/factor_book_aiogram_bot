import asyncio
import logging
import sys

from aiogram import Dispatcher, F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, CallbackQuery
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _

TOKEN = '7176330061:AAHCAiWsfkEGiqRmnCQK_79tLJzdSTIYRss'

dp = Dispatcher()


# @dp.message(CommandStart())
# async def start_handler(message: Message):
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(
#         KeyboardButton(text='Uz🇺🇿'),
#         KeyboardButton(text='En🇬🇧')
#     )
#
#     await message.answer(_('Tilni tanlang!'), reply_markup=rkb.as_markup(resize_keyboard=True))
#

@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    rkb = InlineKeyboardBuilder()
    rkb.add(
        InlineKeyboardButton(text='Uz🇺🇿', callback_data='lang_uz'),
        InlineKeyboardButton(text='En🇬🇧', callback_data='lang_en'),
    )
    await message.answer(_('Tilni tanlang!'), reply_markup=rkb.as_markup(resize_keyboard=True))


@dp.callback_query(F.data.startswith('lang_'))
async def start_handler(callback: CallbackQuery, state: FSMContext):  # en
    lang_code = callback.data.split('lang_')[-1]
    await state.update_data(locale=lang_code)
    # lang = 'Ingliz' if lang_code == 'en' else "O'zbek"
    # lang = (_("O'zbek"), _('Ingliz'))[lang_code == 'en']
    await callback.answer(_('Til tanlandi', locale=lang_code))


#
#
# @dp.message(F.text.in_(['Uz🇺🇿', 'En🇬🇧']))
# async def start_handler(message: Message, state: FSMContext):
#     rkb = ReplyKeyboardRemove()
#     if message.text == 'Uz🇺🇿':
#         await state.update_data(locale='uz')
#         await message.answer(_('Uzbek tili tanlandi'), reply_markup=rkb)
#     else:
#         await state.update_data(locale='en')
#         await message.answer(_('Ingliz tili tanlandi'), reply_markup=rkb)


@dp.message()
async def start_handler(message: Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text=_('Ish joyi kerak')),
        KeyboardButton(text=_('Xodim kerak')),
        KeyboardButton(text=_('Sherik kerak')),
    )
    await message.answer(_('Menyu tanlang'), reply_markup=rkb.as_markup(resize_keyboard=True))


@dp.message(F.text == __('Sherik kerak'))
async def start_handler(message: Message):
    await message.answer(_('Bolimni tanladiz'))


async def main():
    bot = Bot(TOKEN)
    i18n = I18n(path='locales')
    dp.update.outer_middleware.register(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# isolation environment


# brew install gettext
# sudo apt-get install gettext

# @factor_bookbot (en, uz, kr)
# @UstozShogirdBot (uz, ru)

# sqlalchemy
# docker compose

