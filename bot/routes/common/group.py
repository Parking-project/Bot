from aiogram import F, Router
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.shared import ChatTypeFilter

from config import TelegramConfig

router = Router(name=__name__)

@router.message(CommandStart(),
                F.chat.id == int(TelegramConfig.GROUP_ID),
                ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_auth_hostory(message: Message, state: FSMContext):
    await message.answer(
        text=f"Help group start" 
    )

# @router.message(CommandStart(),
#                 F.chat.id == int(TelegramConfig.RESERVETION_GROUP_ID),
#                 ChatTypeFilter(chat_type=["group", "supergroup"]))
# async def command_auth_hostory(message: Message, state: FSMContext):
#     await message.answer(
#         text=f"Reserve group start" 
#     )

@router.message(Command(BotCommand(command="help", description="Помощь сотрудникам")),
                # F.chat.id == int(TelegramConfig.GROUP_ID),
                ChatTypeFilter(chat_type=["group", "supergroup"]))
async def command_auth_hostory(message: Message):
    await message.answer(
        text=f"Help group start" 
    )

# @router.message(Command(BotCommand(command="help", description="Помощь сотрудникам")),
#                 F.chat.id == int(TelegramConfig.RESERVETION_GROUP_ID),
#                 ChatTypeFilter(chat_type=["group", "supergroup"]))
# async def command_auth_hostory(message: Message):
#     await message.answer(
#         text=f"group reserve {message.chat.id}"
#     )
