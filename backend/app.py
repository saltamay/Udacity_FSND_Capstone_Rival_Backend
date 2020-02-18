import json
from flask import Flask, request, jsonify, abort
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config.config import Development
from config.config import Test
from database.db import setup_db, create_all
from auth import AuthError, requires_auth
from controllers.bootcamp import add_bootcamp, get_bootcamps, get_single_bootcamp, update_bootcamp, delete_bootcamp
from controllers.course import add_course, get_courses, get_single_course, update_course, delete_course

app = Flask(__name__)
setup_db(app, Development.SQLALCHEMY_DATABASE_URI)
# setup_db(app, Test.SQLALCHEMY_DATABASE_URI)
CORS(app)


'''
    GET /api/v1/bootcamps
        Returns status code 200 and json object { "success": True, "data": bootcamps}
            where bootcamps is the list of all bootcamps
        Access public
'''


@app.route('/api/v1/bootcamps', methods=['GET'])
def bootcamps():
    bootcamps = get_bootcamps()

    if len(bootcamps) == 0:
        abort(404)

    bootcamps = [bootcamp.format() for bootcamp in bootcamps]

    data = jsonify({
        "success": True,
        "data": bootcamps
    })

    return data, status.HTTP_200_OK


'''
    POST /api/v1/bootcamps
        Returns status code 201 and json object { "success": True, "data": bootcamp}
            where bootcamp is the newly create bootcamp
        Access Private
'''


@app.route('/api/v1/bootcamps', methods=['POST'])
@requires_auth('add:bootcamps')
def bootcamp(payload):
    # try:
    new_bootcamp = add_bootcamp(request)

    data = jsonify({
        "success": True,
        "data": new_bootcamp.format()
    })
    return data, status.HTTP_201_CREATED
    # except BaseException:
    # abort(422)


'''
    GET /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True, "data": bootcamp}
            where bootcamp is the bootcamp with the id of id
            that is defined within the query string
        Access public
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['GET'])
def get_bootcamp_by_id(id):
    bootcamp = get_single_bootcamp(id)

    if bootcamp is None:
        abort(404)

    data = jsonify({
        "success": True,
        "data": bootcamp.format()
    })
    return data, status.HTTP_200_OK


'''
    PUT /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True, "data": bootcamp}
            where bootcamp is the updated bootcamp with the id of id
            that is defined within the query string
        Access private
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['PUT'])
@requires_auth('update:bootcamps')
def update_bootcamp_by_id(payload, id):
    try:
        updated_bootcamp = update_bootcamp(request, id)

        data = jsonify({
            "success": True,
            "data": updated_bootcamp.format()
        })

        return data, status.HTTP_200_OK
    except Exception as ex:
        print(ex.__class__.__name__)
        if ex.__class__.__name__ == 'AttributeError':
            abort(404)
        else:
            abort(422)


'''
    DELETE /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True }

        Access private
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['DELETE'])
@requires_auth('delete:bootcamps')
def delete_bootcamp_by_id(payload, id):
    data = delete_bootcamp(id)

    if data is None:
        abort(404)

    return data, status.HTTP_200_OK


'''
    GET /api/v1/courses
        Returns status code 200 and json object { "success": True, "data": courses}
            where courses is the list of all courses
        Access public
'''


@app.route('/api/v1/courses', methods=['GET'])
def courses():
    courses = get_courses()

    if len(courses) == 0:
        abort(404)

    courses = [course.format() for course in courses]

    data = jsonify({
        "success": True,
        "data": courses
    })
    return data, status.HTTP_200_OK


'''
    POST /api/v1/courses
        Returns status code 201 and json object { "success": True, "data": course}
            where course is the newly create course
        Access Private
'''


@app.route('/api/v1/courses', methods=['POST'])
@requires_auth('add:courses')
def course(payload):
    try:
        new_course = add_course(request)

        data = jsonify({
            "success": True,
            "data": new_course.format()
        })
        return data, status.HTTP_201_CREATED
    except:
        abort(422)


'''
    GET /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True, "data": course}
            where course is the course with the id of id
            that is defined within the query string
        Access public
'''


@app.route('/api/v1/courses/<int:id>', methods=['GET'])
def get_course_by_id(id):
    course = get_single_course(id)

    if course is None:
        abort(404)

    data = jsonify({
        "success": True,
        "data": course.format()
    })
    return data, status.HTTP_200_OK


'''
    PUT /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True, "data": course}
            where course is the updated course with the id of id
            that is defined within the query string
        Access private
'''


@app.route('/api/v1/courses/<int:id>', methods=['PUT'])
@requires_auth('update:courses')
def update_course_by_id(payload, id):
    try:
        updated_course = update_course(request, id)

        data = jsonify({
            "success": True,
            "data": updated_course.format()
        })

        return data, status.HTTP_200_OK
    except Exception as ex:
        print(ex.__class__.__name__)
        if ex.__class__.__name__ == 'AttributeError':
            abort(404)
        else:
            abort(422)


'''
    DELETE /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True }
            
        Access private
'''


@app.route('/api/v1/courses/<int:id>', methods=['DELETE'])
@requires_auth('delete:courses')
def delete_course_by_id(payload, id):
    data = delete_course(id)

    if data is None:
        abort(404)

    return data, status.HTTP_200_OK


# Default port:
if __name__ == '__main__':
    app.run()

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"
    }), 422


@app.errorhandler(AuthError)
def handle_auth_error(auth_error):
    print(auth_error.error)
    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": auth_error.error['message']
    }), auth_error.status_code
