__all__ = ("router",)

from aiogram import Router
from .admin import router as admin_callback_router
from .user import router as user_callback_router

router = Router(name=__name__)

router.include_routers(
    admin_callback_router,
    user_callback_router
)