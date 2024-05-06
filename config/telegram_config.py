"""Bot config class."""
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramConfig:
    TOKEN_API: str = os.getenv('TOKEN_API')
    GROUP_ID: int = os.getenv('GROUP_ID')
    RESERVETION_GROUP_ID: int = os.getenv('RESERVETION_GROUP_ID')
