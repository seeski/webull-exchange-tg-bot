from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from lexicon import LEXICON as lex
from services import get_info, get_caption


async def start(message: Message):
    await message.answer(text=lex['hello'])


async def ticker(message: Message):
    chat_id = message.from_user.id
    path = get_info(message.text)
    photo = open(path, 'rb')
    caption = get_caption(message.text)
    await message.answer_photo(photo, caption=caption)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(ticker)
