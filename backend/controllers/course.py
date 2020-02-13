from flask import jsonify
from models.course import Course


'''
    GET /api/v1/courses
        Returns status code 200 and json object { "success": True, "data": courses}
            where courses is the list of all courses
        Access public
'''


def get_courses():
    courses = Course.query.all()
    courses = [course.format() for course in courses]
    data = jsonify({
        "success": True,
        "data": courses
    })
    return data


'''
    GET /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True, "data": course}
            where course is the course with the id of id
            that is defined within the query string
        Access public
'''


def get_single_course(id):
    course = Course.query.filter_by(id=id).one_or_none()
    data = jsonify({
        "success": True,
        "data": course.format()
    })

    return data


'''
    POST /api/v1/courses
        Returns status code 201 and json object { "success": True, "data": course}
            where course is the newly create course
        Access Private
'''


def add_course(request):
    course = request.get_json()

    title = course['title']
    description = course['description']
    duration = course['duration']
    tuition = course['tuition']
    minimum_skill = course['minimum_skill']
    scholarships_available = course['scholarships_available']

    new_course = Course(title, description, duration, tuition,
                        minimum_skill, scholarships_available)

    new_course.insert()

    data = jsonify({
        "success": True,
        "message": new_course.format()
    })

    return data


'''
    PUT /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True, "data": course}
            where course is the updated course with the id of id
            that is defined within the query string
        Access private
'''


def update_course(request, id):
    course = Course.query.filter_by(id=id).one_or_none()

    updated_course = request.get_json()

    course.name = updated_course['title']
    course.description = updated_course['description']
    course.duration = updated_course['duration']
    course.tuition = updated_course['tuition']
    course.minimum_skill = updated_course['minimum_skill']
    course.scholarships_available = updated_course['scholarships_available']

    course.update()

    data = jsonify({
        "success": True,
        "message": course.format()
    })
    return data


'''
    DELETE /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True }
            
        Access private
'''


def delete_course(id):
    course = Course.query.filter_by(id=id).one_or_none()
    course.delete()
    data = jsonify({
        "success": True
    })
    return data
