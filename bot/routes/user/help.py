from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import HelpState, AuthState, ReserveState
from bot.keyboard.reply import UserRK
from bot.routes.base_func import update_state, send_message

from core.requests import DocumentController

from config import TelegramConfig
from .base_handlers import check_user_response_exception

router = Router(name=__name__)

async def send_document(access: str, message: Message, mime: str):
    document = message.document
    file = await message.bot.get_file(document.file_id)
    return DocumentController.post(
            file_id=document.file_id,
            file_unique_id=document.file_unique_id,
            file_size=document.file_size,
            file_url=f"https://api.telegram.org/file/"
                        f"bot{TelegramConfig.TOKEN_API}/"
                        f"{file.file_path}",
            file_mime=mime,
            token=access,
    )


@router.message(HelpState.text, F.photo)
@router.message(HelpState.text, F.document)
async def command_send_document(message: Message, state: FSMContext):
    await state.set_state(HelpState.documents)
    data = await update_state(
        message=message,
        state=state
    )
    if data is None:
        return
    access = data["access"]

    if message.caption is None:
        await message.reply(
            text="Для отправки сообщения техподдержки необходимо ввести текст",
            reply_markup=UserRK.rk()
        )
        await state.set_state(HelpState.text)
        return
    
    mime = "document"
    if F.photo:
        mime = "photo"
        if message.document is None:
            await message.reply(
                text="Для отправки фото не сжимайте их",
                reply_markup=UserRK.rk()
            )
            await state.set_state(AuthState.user)
            return
        
    answer_tg_id = None
    if message.reply_to_message is not None:
        answer_tg_id = message.reply_to_message.message_id
    
    response = send_message(
        access=access,
        text=message.caption,
        message=message, 
        answer_tg_id=answer_tg_id
    )
    if await check_user_response_exception(response, message, state):
        return 

    response = await send_document(
        access=access,
        message=message, 
        mime=mime
    )

    await check_user_response_exception(response, message, state)

@router.message(HelpState.text)
async def command_send_text(message: Message, state: FSMContext):
    await state.set_state(HelpState.documents)
    data = await update_state(
        message=message,
        state=state
    )
    if data is None:
        return
    access = data["access"]
    
    answer_tg_id = None
    if message.reply_to_message is not None:
        answer_tg_id = message.reply_to_message.message_id

    response = send_message(
        access=access,
        text=message.text,
        message=message, 
        answer_tg_id=answer_tg_id
    )
    await check_user_response_exception(response, message, state)


@router.message(HelpState.documents, F.photo)
@router.message(HelpState.documents, F.document)
async def command_send_photo(message: Message, state: FSMContext):
    data = await update_state(
        message=message,
        state=state,
        now_state=HelpState.documents
    )
    if data is None:
        return
    access = data["access"]

    mime = "document"
    if F.photo:
        mime = "photo"
        if message.document is None:
            await message.reply(
                text="Для отправки фото не сжимайте их",
                reply_markup=UserRK.rk()
            )
            return
    
    
    response = await send_document(
        access=access,
        message=message,
        mime=mime
    )

    await check_user_response_exception(response, message, state)
