# config.py

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.flaskenv'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 b'\x16\xf2hz\x07\xf4<\xbb"\x8d,\xf9*a\x0bg\n`\xe4\x0fG\xb4@\xf0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentSqliteConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data/dev_db')


class DevelopmentConfig(Config):
    DEBUG = True
    PG_USER = "pvv"
    PG_PASSWORD = "krpp"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "departments_db"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'tests/test_db/test_db')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass


config = {
    'development_sqlite': DevelopmentSqliteConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

}
