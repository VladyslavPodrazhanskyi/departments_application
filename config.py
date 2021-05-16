import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.flaskenv'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 b'\x16\xf2hz\x07\xf4<\xbb"\x8d,\xf9*a\x0bg\n`\xe4\x0fG\xb4@\xf0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data/dev_db')


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'tests/test_db/test_db')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


# class DevelopmentWinPostgres(Config):
#     DEBUG = True
#     PG_USER = "postgres"
#     PG_PASSWORD = "krpp1"
#     PG_HOST = "localhost"
#     PG_PORT = 5432
#     DB_NAME = "company_db"
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#                               f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


# class DevelopmentPostgres(Config):
#     DEBUG = True
#     PG_USER = "postgres"
#     PG_PASSWORD = "krpp1"
#     PG_HOST = "localhost"
#     PG_PORT = 5432
#     DB_NAME = "company_db"
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#                               f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# def run_config():
#     env = os.environ.get("ENV")
#     if env == "DEV":
#         return DevConfig
#     elif env == "TEST":
#         return TestConfig
#     else:
#         return Config
