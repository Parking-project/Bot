from apps.bot.routes import router as main_router
from aiogram import Dispatcher
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import Message, BotCommand, BufferedInputFile
from aiogram.fsm.context import FSMContext
from config.telegram_config import TelegramConfig
import io
import os
from urllib.parse import urlparse
import urllib.request
import base64
from aiogram.types import URLInputFile

# router = Router(name=__name__)
# url: str = ""
# filename: str = ""

# @router.message(F.document)
# async def command_send_document_handler(message: types.Message):
#         document = message.document
#         file = await message.bot.get_file(document.file_id)
#         file_in_io = io.BytesIO()
#         await message.bot.download_file(file.file_path, destination=file_in_io)
#         global url
#         global filename
#         url = f"https://api.telegram.org/file/bot{TelegramConfig.TOKEN_API}/{file.file_path}"       
#         filename = document.file_name
#         file_bytes = file_in_io.read(document.file_size)

#         await message.bot.send_document(
#             chat_id=TelegramConfig.ADMIN_ID,
#             caption=f"Test",
#             parse_mode=ParseMode.MARKDOWN_V2,
#             document=BufferedInputFile(file_bytes, filename=document.file_name),
#         )

#         print(f"\n\n\nfile_size = {file.file_size}\nfilename = {document.file_name}\nfile_path = {file.file_path}")
        

# @router.message(Command(BotCommand(command="test", description="Обратиться к тех поддержке")))
# async def command_send_document_handler(message: types.Message):
#         file_in_io = io.BytesIO()
#         file_bytes = file_in_io.read(21611)

#         global url
#         global filename
#         a = urlparse(url)
#         document = URLInputFile(
#             url=url,
#             filename=os.path.basename(a.path)
#         )
#         await message.bot.send_document(
#             chat_id=TelegramConfig.ADMIN_ID,
#             caption=f"Test",
#             parse_mode=ParseMode.MARKDOWN_V2,
#             document=document,
#         )

def register_route(disp: Dispatcher):
    disp.include_router(main_router)

