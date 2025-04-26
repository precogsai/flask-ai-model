import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    DEBUG = os.getenv("DEBUG", False)
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
