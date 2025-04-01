from dotenv import load_dotenv
import os

load_dotenv() # take environment variable from .env

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    DATABASE = os.getenv('DATABASE')
    DATABASE_PWD = os.getenv('DATABASE_PSSWD')
    MYSQL_PORT=os.getenv('MYSQL_PORT')
    DATABASE_USER= os.getenv('MYSQL_USER')


