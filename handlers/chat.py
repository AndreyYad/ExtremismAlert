from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.state import default_state

from modules.bot_commands import reply_msg
from modules.extremists import list_extremists

router = Router()

async def get_message(msg: types.Message):
    print(msg.chat.type)
    reply_text = ''
    for extremist in list_extremists:
        if await extremist.find(msg.text):
            reply_text += await extremist.get_text()
    if reply_text != '':
        await reply_msg(msg, reply_text)

async def register_chat_handlers():
    router.message.register(get_message, F.chat.type.in_({'group', 'supergroup'}), F.content_type.in_({'text', 'photo'}))