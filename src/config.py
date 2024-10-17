class Config:
    SECRET_KEY = 'mysecret'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'fazt'
    MYSQL_PASSWORD = 'fazt'
    MYSQL_DB = 'flask_login'

config={
    'development': DevelopmentConfig,
}