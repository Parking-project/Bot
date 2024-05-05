__all__ = ("router",)

from aiogram import Router
from .callback import router as callback_router
from .help import router as help_router
from .place import router as place_router
from .reserve import router as reserve_router

router = Router(name=__name__)

router.include_routers(
    callback_router,
    help_router,
    place_router,
    reserve_router
)