from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.state import default_state
from pprint import PrettyPrinter

from modules.bot_commands import reply_msg
from modules.extremists import list_extremists

router = Router()

async def get_message(msg: types.Message):
    # pp = PrettyPrinter(indent=4)
    # pp.pprint(dict(msg))#
    reply_text = ''
    if msg.caption is None:
        msg_text = msg.text
    else:
        msg_text = msg.caption
    for extremist in list_extremists:
        if await extremist.find(msg_text):
            reply_text += await extremist.get_text()
    if reply_text != '':
        await reply_msg(msg, reply_text)

async def register_chat_handlers():
    router.message.register(get_message, F.chat.type.in_({'group', 'supergroup'}), F.content_type.in_({'text', 'photo'}))