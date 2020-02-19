from database.db import db


class Bootcamp(db.Model):
    __tablename__ = 'bootcamps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    website = db.Column(db.String(500))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(80))
    address = db.Column(db.String(120))
    careers = db.Column(db.ARRAY(db.String(80)))
    job_assistance = db.Column(db.Boolean)
    upvotes = db.Column(db.Integer)
    img_url = db.Column(db.String(80))
    courses = db.relationship('Course', backref='bootcamp', lazy=True)

    def __init__(self, name, description, website, phone, email, address, careers, job_assistance, upvotes, img_url):
        self.name = name
        self.description = description
        self.website = website
        self.phone = phone
        self.email = email
        self.address = address
        self.careers = careers
        self.job_assistance = job_assistance
        self.upvotes = upvotes
        self.img_url = img_url

    def format_short(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "careers": self.careers,
            "upvotes": self.upvotes,
            "img_url": self.img_url
        }

    def format_long(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "website": self.website,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "careers": self.careers,
            "job_assistance": self.job_assistance,
            "upvotes": self.upvotes,
            "img_url": self.img_url
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            bootcamp = Bootcamp(name=name)
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            bootcamp.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            bootcamp = Bootcamp.query.filter(bootcamp.id=id).one_or_none()
            bootcamp.title = 'Juno'
            bootcamp.update()
    '''

    def update(self):
        db.session.commit()
