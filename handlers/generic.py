from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.state import default_state

from modules.text import Text
from modules.bot_commands import send_msg

router = Router()

async def start_func(msg: types.Message):
    await send_msg(
        msg.chat.id, 
        Text.start
    )

async def register_generic_handlers():
    router.message.register(start_func, CommandStart(), StateFilter(default_state))