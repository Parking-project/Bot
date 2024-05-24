from aiogram.types import Message, BotCommand
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F, Router

from aiogram.filters import Command, CommandStart
from bot.keyboard.reply import AuthRK

from bot.states import AuthState, HelpState

router = Router(name=__name__)

@router.message(CommandStart())
@router.message(AuthState.user, CommandStart())
@router.message(AuthState.admin, CommandStart())
@router.message(HelpState.text, CommandStart())
@router.message(HelpState.documents, CommandStart())
async def command_start(message: Message, state: FSMContext):
    await message.answer(
        text="Здраствуйте, Вас приветствует бот парковки!\nПрошу авторизируйтесь",
        reply_markup=AuthRK.rk()
    )


@router.message(AuthState.user or HelpState.text or HelpState.documents, Command(BotCommand(command="help", description="user help")))
async def command_user_help(message: Message, state: FSMContext):
    pass

@router.message(AuthState.admin, Command(BotCommand(command="help", description="admin help")))
async def command_admin_help(message: Message, state: FSMContext):
    pass

@router.message(Command(BotCommand(command="help", description="user help")))
async def command_base_help(message: Message, state: FSMContext):
    pass
