import os

# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '/\xfd\xc9&\xf4\xa4\x9eu\xf75\x8c\x10\x16\xb2\xfb\xb8z\x06wc$N\xd7n'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False