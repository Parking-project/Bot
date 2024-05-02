from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from apps.shared import ChatTypeFilter
router = Router(name=__name__)

@router.message(CommandStart(), ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_auth_hostory(message: Message, state: FSMContext):
    pass

@router.message(Command(BotCommand(command="help", description="Помощь сотрудникам")), ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_auth_hostory(message: Message, state: FSMContext):
    pass
