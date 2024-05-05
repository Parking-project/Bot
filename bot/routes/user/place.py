from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import LogInState
from bot.keyboard.reply import UserRK

from core.requests import TokenController

router = Router(name=__name__)