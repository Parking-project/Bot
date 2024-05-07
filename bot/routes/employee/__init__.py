__all__ = ("router",)

from aiogram import Router
from .help import router as help_router
from .callback import router as callback_router
from .reserve import router as reserve_router

router = Router(name=__name__)

router.include_routers(
    callback_router,
    reserve_router,
    help_router,
)