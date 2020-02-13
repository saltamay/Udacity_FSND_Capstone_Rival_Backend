import json
from flask_sqlalchemy import SQLAlchemy
from config import Postgrest


db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = Postgrest.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Postgrest.SQLALCHEMY_TRACK_MODIFICATIONS
    db.app = app
    db.init_app(app)


def create_all():
    db.create_all()
