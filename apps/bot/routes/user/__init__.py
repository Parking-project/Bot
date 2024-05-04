__all__ = ("router",)

from aiogram import Router
from .auth import router as auth_router
from .callback import router as callback_router
from .help import router as help_router
# from .reserve_handlers import router as reserve_router

router = Router(name=__name__)

router.include_routers(
    auth_router,
    callback_router,
    help_router,
)