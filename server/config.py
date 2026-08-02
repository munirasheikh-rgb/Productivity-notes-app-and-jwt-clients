import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR /"instance"/"productivity_notes.db"

class Config:
 SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI",f"sqlite:///{DATABASE_PATH}")
 SQLALCHEMY_TRACK_MODIFICATIONS =False
 JWT_SECRET_KEY = "cd029162c63773a70e66bc41e9aa2923b586448b1f463d2768a5267d5c9c7d79"

 JSON_SORT_KEYS =False