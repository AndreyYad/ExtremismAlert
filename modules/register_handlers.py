from handlers.generic import register_generic_handlers
from handlers.chat import register_chat_handlers

async def register_handlers():
    await register_generic_handlers()
    await register_chat_handlers()