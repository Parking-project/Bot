__all__ = ("router",)

from aiogram import Router
from .history import form_router as hisory_router

router = Router(name=__name__)

router.include_routers(
    hisory_router
)