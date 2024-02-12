from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.state import default_state

from modules.text import Text
from modules.bot_commands import send_msg
from modules.get_json_data import get_data

router = Router()

async def get_message(msg: types.Message):
    data = await get_data()
    msg_text = msg.text

async def register_chat_handlers():
    router.message.register(get_message, F.chat.type == 'group', F.content_type.in_({'text', 'photo'}))