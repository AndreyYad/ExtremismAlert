from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import generic
from handlers import chat

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

dp.include_routers(
    generic.router,
    chat.router
)