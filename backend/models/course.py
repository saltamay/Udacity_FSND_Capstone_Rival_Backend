from database.db import db


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    duration = db.Column(db.Integer)
    tuition = db.Column(db.Integer)
    minimum_skill = db.Column(db.String(80))
    scholarships_available = db.Column(db.Boolean)

    def __init__(self, title, description, duration, tuition, minimum_skill, scholarships_available):
        self.title = title
        self.description = description
        self.duration = duration
        self.minimum_skill = minimum_skill
        self.scholarships_available = scholarships_available

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "duration": self.duration
            "tuition": self.tuition,
            "minimum_skill": self.minimum_skill,
            "scholarships_available": self.scholarships_available
        }

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            course = Course(title=title)
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            course.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            course = Course.query.filter_by(id=id).one_or_none()
            course.title = 'Full Stack Web Development'
            course.update()
    '''

    def update(self):
        db.session.commit()
