__all__ = ("router",)

from aiogram import Router
from .help import router as help_router
from .reserve import router as reserve_router

router = Router(name=__name__)

router.include_routers(
    help_router,
    reserve_router
)