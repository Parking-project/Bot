from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from apps.bot.states import LogInState
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import TokenController

router = Router(name=__name__)