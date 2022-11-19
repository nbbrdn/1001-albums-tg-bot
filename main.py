from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import TELEGRAM_TOKEN
from keyboards import main_keyboard, album_keyboard
from controllers import get_random_album

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot has been started.')


@dp.message_handler(commands=['start'])
async def proc_cmd_start(message: types.Message):
    await message.answer(
        text='Welcome to the music album advisor! 🎧',
        reply_markup=main_keyboard,
    )
    await message.delete()


@dp.message_handler(Text(equals='Surprise Me!'))
async def proc_txt_random_album(message: types.Message):
    random_album = get_random_album()
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_album.cover,
        caption=f'<b>{random_album.title}</b> by {random_album.artist}, <em>{random_album.year}</em>',
        parse_mode='HTML',
        reply_markup=album_keyboard,
    )
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp, skip_updates=True, on_startup=on_startup
    )