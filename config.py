import os


# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
    ALGORITHMS = os.environ.get('ALGORITHMS')
    API_AUDIENCE = os.environ.get('API_AUDIENCE')


class Development:
    # FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
    ALGORITHMS = os.getenv('ALGORITHMS')
    API_AUDIENCE = os.getenv('API_AUDIENCE')


class Test:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_TEST_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
