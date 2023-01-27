from flask import request,jsonify
import json
from datetime import date
from flask import jsonify, request, make_response
from database.models import Bike,Odometer

class BikeController:

    @staticmethod
    def create_bike():
        bike_obj = request.get_json()
        bike = Bike(odometer_reading=bike_obj["odometer_reading"]).save()
        return make_response(jsonify({"message": "successfully created bike",
                                  "bike": json.loads(bike.to_json())})), 201
    

    @staticmethod
    def get_kilometers_done(bike_id):
        reading = Odometer.objects(bike=bike_id, timestamp=date.today()).to_json()
        reading_data = json.loads(reading)
        km_done = 0
        for i in reading_data:
            km_done += i["current_reading"]-i["previous_reading"]
        return make_response(jsonify({"kilometers": km_done})), 200