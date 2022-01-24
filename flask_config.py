import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Setup:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BIND_PROT = os.environ.get('BIND_PROT')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentSetup(Setup):
    DEBUG = True
    ENGINE_STR = os.environ.get('DEV_DATABASE_URL') or \
        os.environ.get('ENGINE_STR')

class TestingSetup(Setup):
    TESTING = True
    ENGINE_STR = os.environ.get('TEST_DATABASE_URL') or \
        os.environ.get('ENGINE_STR')


class ProductionSetup(Setup):
    ENGINE_STR = os.environ.get('DATABASE_URL') or \
        os.environ.get('ENGINE_STR')


mysetup = {
    'development': DevelopmentSetup,
    'testing': TestingSetup,
    'production': ProductionSetup,

    'default': DevelopmentSetup
}
