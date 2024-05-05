import io
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from bot.states import LogInState, HelpState
from bot.keyboard.reply import UserRK, auth_rk
from bot.routes.base_func import update_state_tokens, send_message

from core.requests import MessageController, DocumentController

from config import TelegramConfig

router = Router(name=__name__)

@router.message(HelpState.text, F.text == UserRK.REQUEST_HELP)
@router.message(HelpState.documents, F.text == UserRK.REQUEST_HELP)
@router.message(LogInState.auth, F.text == UserRK.REQUEST_HELP)
@router.message(LogInState.auth, 
                Command(BotCommand(command="send_help", description="register command")))
async def command_send_message(message: Message, state: FSMContext):
    data = await update_state_tokens(
        message=message,
        state=state,
        now_state=HelpState.text
    )
    if data is None:
        return
    
    await message.answer(
        "Введите текст сообщения и прикрепите файлы",
        reply_markup=auth_rk()
    )


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
async def command_send_text_photo(message: Message, state: FSMContext):
    data = await update_state_tokens(
        message=message,
        state=state,
        now_state=HelpState.documents
    )
    if data is None:
        return
    access = data["access"]

    if message.caption is None:
        await message.reply(
            text="Для отправки сообщения техподдержки необходимо ввести текст",
            reply_markup=auth_rk()
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )
        return
    
    if F.photo and message.document is None:
        await message.reply(
            text="Для отправки фото не сжимайте их",
            reply_markup=auth_rk()
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )
        return
        
    answer_tg_id = None
    if message.reply_to_message is not None:
        answer_tg_id = message.reply_to_message.message_id
    
    response_data = send_message(
        access=access,
        text=message.caption,
        message=message, 
        answer_tg_id=answer_tg_id
    )
    if response_data.IsException():
        await message.reply(
            text=f"Не удалось отправить сообщение! {response_data.data}",
            reply_markup=auth_rk()
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )
        return 

    response_data = await send_document(
        access=access,
        message=message, 
        mime=(F.photo if "photo" else "document")
    )

    if response_data.IsException():
        await message.reply(
            text=f"Не удалось отправить файл! {response_data.data}",
            reply_markup=auth_rk
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )

@router.message(HelpState.text)
async def command_send_text(message: Message, state: FSMContext):
    data = await update_state_tokens(
        message=message,
        state=state,
        now_state=HelpState.documents
    )
    if data is None:
        return
    access = data["access"]
    
    answer_tg_id = None
    if message.reply_to_message:
        answer_tg_id = message.reply_to_message.message_id

    response_data = send_message(
        access=access,
        text=message.text,
        message=message, 
        answer_tg_id=answer_tg_id
    )
    if response_data.IsException():
        await message.reply(
            text=f"Не удалось отправить сообщение! {response_data.data}",
            reply_markup=auth_rk()
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )
        return 


@router.message(HelpState.documents, F.photo)
@router.message(HelpState.documents, F.document)
async def command_send_photo(message: Message, state: FSMContext):
    data = await update_state_tokens(
        message=message,
        state=state,
        now_state=HelpState.documents
    )
    if data is None:
        return
    access = data["access"]

    if F.photo and message.document is None:
        await message.reply(
            text="Для отправки фото не сжимайте их",
            reply_markup=auth_rk()
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )
        return
    
    
    response_data = await send_document(
        access=access,
        message=message,
        mime="photo"
    )

    if response_data.IsException():
        await message.reply(
            text=f"Не удалось отправить файл! {response_data.data}",
            reply_markup=auth_rk
        )
        await update_state_tokens(
            message=message,
            state=state,
            now_state=LogInState.auth
        )
