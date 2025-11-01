import os
from dotenv import load_dotenv


# load enviroment variables from Database.env file

load_dotenv(".env")  # carica .env in sviluppo
DB_USER = os.getenv("USERNAME_DB")
DB_PASSWORD = os.getenv("PASSWORD_DB")
DB_NAME = os.getenv("NAME_DB")


class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
