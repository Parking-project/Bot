from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from apps.bot.states import LogIn_State
from apps.shared import ChatTypeFilter

router = Router(name=__name__)

@router.message(CommandStart(),
                ChatTypeFilter(chat_type=["private"]))
async def command_auth_hostory(message: Message, state: FSMContext):
    pass

@router.message(Command(BotCommand(command="help", description="auth command")),
                ChatTypeFilter(chat_type=["private"]))
async def command_auth_hostory(message: Message, state: FSMContext):
    pass

@router.message(Command(BotCommand(command="help", description="auth help")),
                ChatTypeFilter(chat_type=["private"]),
                LogIn_State.auth)
async def command_auth_hostory(message: Message, state: FSMContext):
    pass