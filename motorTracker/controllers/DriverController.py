from flask import request,jsonify
import json
from flask import jsonify, request, make_response
from database.models import Driver


class DriverController:

    @staticmethod
    def create_driver(bike_id):
        driver = request.get_json()
        new_driver = Driver(name=driver["name"], bike=bike_id).save()
        return make_response(jsonify({"driver": json.loads(new_driver.to_json())})), 201


    @staticmethod
    def get_drivers():
        drivers = Driver.objects().to_json()
        return make_response(drivers), 200


    @staticmethod
    def get_one_drivers():
        one_driver = Driver.objects().to_json()
        return make_response(one_driver), 200