import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import GroupFilter
from filters import AdminFilter
from loader import dp, bot


@dp.message_handler(GroupFilter(), Command("set_photo", prefixes="!/@"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    try:
        # print(source_message.photo)
        photo = source_message.photo[-1]
        photo = await photo.download(destination=io.BytesIO())
        input_file = types.InputFile(photo)
        # 1-usul
        await message.chat.set_photo(photo=input_file)
    except AttributeError:
        await message.reply("Rasm o'zgartirilmadi!")


@dp.message_handler(GroupFilter(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    # 2-usul
    await bot.set_chat_title(message.chat.id, title=title)


@dp.message_handler(GroupFilter(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)
