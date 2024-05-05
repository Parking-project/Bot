"""Bot config class."""
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramConfig:
    TOKEN_API: str = os.getenv('TOKEN_API')
