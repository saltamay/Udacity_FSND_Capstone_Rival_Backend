from flask import Flask, request, jsonify
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from config import Development
from models import setup_db, create_all, Bootcamp

app = Flask(__name__)
setup_db(app)
create_all()


def create_bootcamp(bootcamp):
    data = jsonify({
        "success": True,
        "message": "Create new bootcamp"
    })

    return data, status.HTTP_201_CREATED


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
        data = jsonify({
            "success": True,
            "message": "Show all bootcamps"
        })
        return data, status.HTTP_200_OK
    else:
        bootcamp = request.get_json()
        return create_bootcamp(bootcamp)


'''
    GET /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True, "data": bootcamp}
            where bootcamp is the bootcamp with the id of id 
            that is defined within the query string
        Access public
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['GET'])
def get_bootcamp(id):
    data = jsonify({
        "success": True,
        "message": f"Get bootcamp {id}"
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
def update_bootcamp(id):
    data = jsonify({
        "success": True,
        "message": f"Update bootcamp {id}"
    })
    return data, status.HTTP_200_OK


'''
    DELETE /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True, "data": bootcamp}
            where bootcamp is the deleted bootcamp with the id of id 
            that is defined within the query string
        Access public
'''


@app.route('/api/v1/bootcamps/<int:id>', methods=['DELETE'])
def delete_bootcamp(id):
    data = jsonify({
        "success": True,
        "message": f"Delete bootcamp {id}"
    })
    return data, status.HTTP_200_OK


# # Default port:
# if __name__ == '__main__':
#     app.run()
