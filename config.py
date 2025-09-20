import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toor@localhost/user_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "secretkey"