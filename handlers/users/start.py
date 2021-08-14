import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuBottom import menuAsosiy, topmenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # logging.info(message)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu)
