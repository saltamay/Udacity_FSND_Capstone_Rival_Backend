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


class Bootcamp(db.Model):
    __tablename__ = 'bootcamps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))
    website = db.Column(db.String(500))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))
    address = db.Column(db.String(120))
    careers = db.Column(db.ARRAY(db.String(80)))
    job_assistance = db.Column(db.Boolean)
