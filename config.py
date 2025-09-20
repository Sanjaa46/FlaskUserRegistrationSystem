import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/user_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "secretkey"