__all__ = ("router",)

from aiogram import Router
from .exit import router as exit_router
from .log_in import router as auth_router
from .register import router as callback_router
# from .reserve_handlers import router as reserve_router

router = Router(name=__name__)

router.include_routers(
    exit_router,
    auth_router,
    callback_router,
)