__all__ = ("router",)

from aiogram import Router

from .admin import router as admin_router
from .auth import router as auth_router
from .common import router as common_router
from .user import router as user_router
from .employee import router as employee_router

router = Router(name=__name__)

router.include_routers(
    common_router,
    auth_router,
    employee_router,
    admin_router,
    user_router
)