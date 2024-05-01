from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from ...states import LogIn_State, Help_State
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import TokenController
from apps.shared import ChatTypeFilter

router = Router(name=__name__)

@router.message(LogIn_State.auth, Command(BotCommand(command="send_help", description="auth command")))
async def command_send_help(message: Message, state: FSMContext):
    data = await state.get_data()