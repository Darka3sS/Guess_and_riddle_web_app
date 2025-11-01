from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

DB_USER = os.getenv("USERNAME_DB")
DB_PASSWORD = os.getenv("PASSWORD_DB")
DB_NAME = os.getenv("NAME_DB")
