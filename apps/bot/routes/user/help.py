from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from apps.shared import ChatTypeFilter
from apps.bot.states import LogIn_State
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import TokenController

router = Router(name=__name__)

@router.message(ChatTypeFilter(chat_type=["private"]),
                LogIn_State.auth,
                F.photo)
async def command_send_photo(message: Message, state: FSMContext):
    pass

@router.message(ChatTypeFilter(chat_type=["private"]),
                LogIn_State.auth,
                F.document)
async def command_send_photo(message: Message, state: FSMContext):
    pass

@router.message(Command(BotCommand(command="register", description="register command")),
                ChatTypeFilter(chat_type=["private"]),
                LogIn_State.auth)
async def command_send_photo(message: Message, state: FSMContext):
    pass