import json
from flask import Flask, request, jsonify
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from config import Development
from database.db import setup_db, create_all
from models.bootcamp import Bootcamp
from controllers.bootcamp import add_bootcamp, get_bootcamps, get_single_bootcamp, update_bootcamp, delete_bootcamp

app = Flask(__name__)
setup_db(app)
create_all()


@app.route('/api/v1/bootcamps', methods=['GET', 'POST'])
def handle_get_and_post():
    if '/bootcamps' in request.url:
        if request.method == 'GET':
            return get_bootcamps(), status.HTTP_200_OK
        else:
            return add_bootcamp(request), status.HTTP_201_CREATED


@app.route('/api/v1/bootcamps/<int:id>', methods=['GET'])
def get_by_id(id):
    if '/bootcamps' in request.url:
        return get_single_bootcamp(id), status.HTTP_200_OK


@app.route('/api/v1/bootcamps/<int:id>', methods=['PUT'])
def update_by_id(id):
    if '/bootcamps' in request.url:
        return update_bootcamp(request, id), status.HTTP_200_OK


@app.route('/api/v1/bootcamps/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    if '/bootcamps' in request.url:
        return delete_bootcamp(id), status.HTTP_200_OK


# Default port:
if __name__ == '__main__':
    app.run()
