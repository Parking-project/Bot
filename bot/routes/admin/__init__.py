__all__ = ("router",)

from aiogram import Router
from .history import router as history_router
from .callback import router as callback_router

router = Router(name=__name__)

router.include_routers(
    history_router,
    callback_router
)