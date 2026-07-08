"""
config/config.py
Loads all configuration values from the .env file so the rest of the
app never touches os.environ directly.
"""

import os
from dotenv import load_dotenv

# Load .env file from project root (one level up from this file's folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "etl_db")

    DATA_FOLDER = os.path.join(BASE_DIR, os.getenv("DATA_FOLDER", "data"))


config = Config()
