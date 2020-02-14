import json
from flask import Flask, request, jsonify, abort
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from config import Development
from database.db import setup_db, create_all
from models.bootcamp import Bootcamp
from controllers.bootcamp import add_bootcamp, get_bootcamps, get_single_bootcamp, update_bootcamp, delete_bootcamp
from controllers.course import add_course, get_courses, get_single_course, update_course, delete_course

app = Flask(__name__)
setup_db(app)
create_all()

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
    updated_bootcamp = update_bootcamp(request, id)

    if updated_bootcamp is None:
        abort(404)

    data = jsonify({
        "success": True,
        "message": updated_bootcamp.format()
    })

    return data, status.HTTP_200_OK


'''
    DELETE /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True }
            
        Access private
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['DELETE'])
def delete_bootcamp_by_id(id):
    data = delete_bootcamp(id)

    if data is None:
        abort(404)

    return data, status.HTTP_200_OK


@app.route('/api/v1/courses', methods=['GET', 'POST'])
def course():
    if request.method == 'GET':
        return get_courses(), status.HTTP_200_OK
    else:
        return add_course(request), status.HTTP_201_CREATED


@app.route('/api/v1/courses/<int:id>', methods=['GET'])
def get_course_by_id(id):
    return get_single_course(id), status.HTTP_200_OK


@app.route('/api/v1/courses/<int:id>', methods=['PUT'])
def update_course_by_id(id):
    return update_course(request, id), status.HTTP_200_OK


@app.route('/api/v1/courses/<int:id>', methods=['DELETE'])
def delete_course_by_id(id):
    return delete_course(id), status.HTTP_200_OK


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
