from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from extensions import register_route, register_bot, register_log
# from config import settings
import logging

def create_app():
    dp = Dispatcher(storage=MemoryStorage())
    register_route(dp)
    bot = register_bot()
    register_log()
    return dp, bot