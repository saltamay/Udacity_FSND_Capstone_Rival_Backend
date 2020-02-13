class Development:
    # Enable debug mode.
    DEBUG = True


class Postgrest:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/bootcamp_report'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
