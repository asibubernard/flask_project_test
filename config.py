import os  

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You-will-never-guess'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')  # new
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)  # new
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None  # new 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # new
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # new
    ADMINS = ['your-email@example.com']  # new