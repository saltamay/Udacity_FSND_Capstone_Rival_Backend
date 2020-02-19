from flask import jsonify
from models.course import Course
from utils import rand_upvote


def get_courses():
    return Course.query.all()


def get_single_course(id):
    try:
        return Course.query.filter_by(id=id).one_or_none()
    except:
        return None


def add_course(request):
    course = request.get_json()

    title = course['title']
    description = course['description']
    duration = course['duration']
    tuition = course['tuition']
    minimum_skill = course['minimumSkill']
    scholarships_available = course['scholarshipsAvailable']
    bootcamp_id = course['bootcampId']
    upvotes = rand_upvote()

    new_course = Course(title, description, duration, tuition,
                        minimum_skill, scholarships_available, upvotes, bootcamp_id)
    print(course)
    new_course.insert()

    return new_course


def update_course(request, id):
    course = Course.query.filter_by(id=id).one_or_none()

    if course is None:
        return None

    updated_course = request.get_json()

    course.name = updated_course['title']
    course.description = updated_course['description']
    course.duration = updated_course['duration']
    course.tuition = updated_course['tuition']
    course.minimum_skill = updated_course['minimumSkill']
    course.scholarships_available = updated_course['scholarshipsAvailable']
    course.upvotes = updated_course['upvotes']

    course.update()

    return course


def delete_course(id):
    course = Course.query.filter_by(id=id).one_or_none()

    if course is None:
        return None

    course.delete()
    data = jsonify({
        "success": True
    })
    return data
