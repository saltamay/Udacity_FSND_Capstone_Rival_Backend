from flask import jsonify
from models.bootcamp import Bootcamp


def get_bootcamps():
    return Bootcamp.query.all()


def get_single_bootcamp(id):
    try:
        return Bootcamp.query.filter_by(id=id).one_or_none()
    except:
        return None


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

    return new_bootcamp


def update_bootcamp(request, id):
    bootcamp = Bootcamp.query.filter_by(id=id).one_or_none()

    if bootcamp is None:
        return None

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

    return bootcamp


def delete_bootcamp(id):
    bootcamp = Bootcamp.query.filter_by(id=id).one_or_none()

    if bootcamp is None:
        return None

    bootcamp.delete()

    data = jsonify({
        "success": True
    })
    return data
