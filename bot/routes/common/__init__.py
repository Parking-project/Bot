__all__ = ("router",)

from aiogram import Router
from .chat import router as chat_router
from .group import router as group_router

router = Router(name=__name__)

router.include_routers(
    chat_router,
    group_router
)