__all__ = (
    "register_bot",
    "register_log",
    "register_route"
)

from .bot_extension import register_bot
from .log_extension import register_log
from .route_extension import register_route