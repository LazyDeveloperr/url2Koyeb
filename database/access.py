
from config import DATABASE_URL, SESSION_NAME
from database.database import Database

clinton = Database(DATABASE_URL, SESSION_NAME)