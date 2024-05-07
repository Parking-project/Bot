__all__ = ("router",)

from aiogram import Router

from .add import router as add_router
from .delete import router as delete_router
from .get import router as get_router
from .set_place import router as set_place_router
from .callback import router as callback_router

router = Router(name=__name__)

router.include_routers(
    callback_router,
    add_router,
    delete_router,
    get_router,
    set_place_router
)