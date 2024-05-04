from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, BotCommand

from apps.bot.states import LogInState, HelpState
from apps.bot.keyboard.reply import ButtonRK, base_rk, auth_rk

from core.requests import MessageController
from ..base_func import update_tokens

router = Router(name=__name__)

@router.message(HelpState.documents,
                F.photo)
async def command_send_photo(message: Message, state: FSMContext):
    pass

@router.message(HelpState.documents,
                F.document)
async def command_send_document(message: Message, state: FSMContext):
    pass

@router.message(F.text == ButtonRK.SEND_HELP,
                LogInState.auth)
@router.message(Command(BotCommand(command="send_help", description="register command")),
                LogInState.auth)
async def command_send_photo(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        return
    await state.set_state(HelpState.text)
    await state.set_data(
        data=data
    )
    await message.answer(
        "Введите текст сообщения",
        reply_markup=base_rk()
    )

@router.message(HelpState.text)
async def command_send_photo(message: Message, state: FSMContext):
    await update_tokens(state=state)
    data = await state.get_data()
    access = data.get("access")
    if access is None:
        return
    await state.set_state(LogInState.auth)
    await state.set_data(
        data=data
    )
    
    answer_tg_id = None
    if message.reply_to_message:
        answer_tg_id = message.reply_to_message.message_id

    MessageController.post(
        token = access,
        text=message.text,
        group_id=message.from_user.id,
        message_id=message.message_id,
        answer_tg_id=answer_tg_id
    )
    # message.answer(
    #     text="Сообщение техподдержке отправлено\n"\
    #         "Чтобы отправить файлы техподдержке отправьте их после этого сообщения"
    # )
