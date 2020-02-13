from flask import jsonify
from models.bootcamp import Bootcamp


'''
    GET /api/v1/bootcamps
        Returns status code 200 and json object { "success": True, "data": bootcamps}
            where bootcamps is the list of all bootcamps
        Access public
'''


def get_bootcamps():
    bootcamps = Bootcamp.query.all()
    bootcamps = [bootcamp.format() for bootcamp in bootcamps]
    data = jsonify({
        "success": True,
        "data": bootcamps
    })
    return data


'''
    GET /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True, "data": bootcamp}
            where bootcamp is the bootcamp with the id of id
            that is defined within the query string
        Access public
'''


def get_single_bootcamp(id):
    bootcamp = Bootcamp.query.filter_by(id=id).one_or_none()
    data = jsonify({
        "success": True,
        "data": bootcamp.format()
    })

    return data


'''
    POST /api/v1/bootcamps
        Returns status code 201 and json object { "success": True, "data": bootcamp}
            where bootcamp is the newly create bootcamp
        Access Private
'''


def add_bootcamp(request):
    bootcamp = request.get_json()

    name = bootcamp['name']
    description = bootcamp['description']
    website = bootcamp['website']
    phone = bootcamp['phone']
    email = bootcamp['email']
    address = bootcamp['address']
    careers = bootcamp['careers']
    job_assistance = bootcamp['job_assistance']

    new_bootcamp = Bootcamp(name, description, website,
                            phone, email, address, careers, job_assistance)

    new_bootcamp.insert()

    data = jsonify({
        "success": True,
        "message": new_bootcamp.format()
    })

    return data


'''
    PUT /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True, "data": bootcamp}
            where bootcamp is the updated bootcamp with the id of id
            that is defined within the query string
        Access private
'''


def update_bootcamp(request, id):
    bootcamp = Bootcamp.query.filter_by(id=id).one_or_none()

    updated_bootcamp = request.get_json()

    bootcamp.name = updated_bootcamp['name']
    bootcamp.description = updated_bootcamp['description']
    bootcamp.website = updated_bootcamp['website']
    bootcamp.phone = updated_bootcamp['phone']
    bootcamp.email = updated_bootcamp['email']
    bootcamp.address = updated_bootcamp['address']
    bootcamp.careers = updated_bootcamp['careers']
    bootcamp.job_assistance = updated_bootcamp['job_assistance']

    bootcamp.update()

    data = jsonify({
        "success": True,
        "message": bootcamp.format()
    })
    return data


'''
    DELETE /api/v1/bootcamps/<int:id>
        Returns status code 200 and json object { "success": True }
            
        Access private
'''


def delete_bootcamp(id):
    bootcamp = Bootcamp.query.filter_by(id=id).one_or_none()
    bootcamp.delete()
    data = jsonify({
        "success": True
    })
    return data
