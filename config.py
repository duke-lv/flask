import datetime
class Config(object):
    pass
class TestConfig(Config):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    # flask vars
    FLASK_VARS = {
        'DEBUG': True,
        'PORT': 8088,
        'SECRET_KEY': 'aReallySecretKey',
    }

    # flask-jwt vars
    FLASK_JWT_VARS = {
        'JWT_AUTH_URL_RULE': '/api/auth',
        'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1)
    }
    FLASK_ENV = 'development'
    host = 'localhost'
    debug = True
    port = 8080
    SQLALCHEMY_DATABASE_URI = "mongodb://aios:aios2018@127.0.0.1/aios" #"postgresql+psycopg2://postgres:postgres@192.168.12.187:5432/aios"
