import json
from flask import Flask, request, jsonify, abort
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from config import Development
from database.db import setup_db, create_all
from controllers.bootcamp import add_bootcamp, get_bootcamps, get_single_bootcamp, update_bootcamp, delete_bootcamp
from controllers.course import add_course, get_courses, get_single_course, update_course, delete_course

app = Flask(__name__)
setup_db(app, Development.SQLALCHEMY_DATABASE_URI)

'''
    GET /api/v1/bootcamps
        Returns status code 200 and json object { "success": True, "data": bootcamps}
            where bootcamps is the list of all bootcamps
        Access public

    POST /api/v1/bootcamps
        Returns status code 201 and json object { "success": True, "data": bootcamp}
            where bootcamp is the newly create bootcamp
        Access Private
'''


@app.route('/api/v1/bootcamps', methods=['GET', 'POST'])
def bootcamp():
    if request.method == 'GET':
        bootcamps = get_bootcamps()

        if len(bootcamps) == 0:
            abort(404)

        bootcamps = [bootcamp.format() for bootcamp in bootcamps]

        data = jsonify({
            "success": True,
            "data": bootcamps
        })

        return data, status.HTTP_200_OK
    else:
        try:
            new_bootcamp = add_bootcamp(request)

            data = jsonify({
                "success": True,
                "message": new_bootcamp.format()
            })
            return data, status.HTTP_201_CREATED
        except:
            abort(422)


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
def update_bootcamp_by_id(id):
    try:
        updated_bootcamp = update_bootcamp(request, id)

        if updated_bootcamp is None:
            abort(404)

        data = jsonify({
            "success": True,
            "message": updated_bootcamp.format()
        })

        return data, status.HTTP_200_OK
    except:
        abort(422)


'''
    DELETE /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True }
            
        Access private
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['DELETE'])
def delete_bootcamp_by_id(id):
    try:
        data = delete_bootcamp(id)

        if data is None:
            abort(404)

        return data, status.HTTP_200_OK
    except:
        abort(422)


'''
    GET /api/v1/courses
        Returns status code 200 and json object { "success": True, "data": courses}
            where courses is the list of all courses
        Access public
    
    POST /api/v1/courses
        Returns status code 201 and json object { "success": True, "data": course}
            where course is the newly create course
        Access Private
'''


@app.route('/api/v1/courses', methods=['GET', 'POST'])
def course():
    if request.method == 'GET':
        courses = get_courses()

        if len(courses) == 0:
            abort(404)

        courses = [course.format() for course in courses]

        data = jsonify({
            "success": True,
            "data": courses
        })
        return data, status.HTTP_200_OK
    else:
        try:
            new_course = add_course(request)

            data = jsonify({
                "success": True,
                "message": new_course.format()
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
def update_course_by_id(id):
    try:
        updated_course = update_course(request, id)

        if updated_course is None:
            abort(404)

        data = jsonify({
            "success": True,
            "message": updated_course.format()
        })

        return data, status.HTTP_200_OK
    except:
        abort(422)


'''
    DELETE /api/v1/courses/<int:id>
        Returns status code 200 and json object { "success": True }
            
        Access private
'''


@app.route('/api/v1/courses/<int:id>', methods=['DELETE'])
def delete_course_by_id(id):
    try:
        data = delete_course(id)

        if data is None:
            abort(404)

        return data, status.HTTP_200_OK
    except:
        abort(422)


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
        "message": "unprocessable"
    }), 422
