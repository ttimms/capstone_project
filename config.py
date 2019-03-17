import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'backupKey.'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SMS_ACCOUNT_SID = os.environ.get('SMS_ACCOUNT_SID')
    SMS_AUTH_TOKEN = os.environ.get('SMS_AUTH_TOKEN')
    DB_HOST = os.environ.get('DB_HOST')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_CURRENT = os.environ.get('DB_CURRENT')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCH_DB')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False