"""Bot config class."""
import os
from dotenv import load_dotenv

load_dotenv()

class ApiConfig:
    API_URL: str = os.getenv('API_URL')