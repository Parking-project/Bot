from bot.routes import router as main_router
from aiogram import Dispatcher

def register_route(disp: Dispatcher):
    disp.include_router(main_router)

