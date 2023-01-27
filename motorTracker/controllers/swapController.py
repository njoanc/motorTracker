from flask import request,jsonify
import json
from datetime import date
from flask import jsonify, request, make_response
from database.models import Swap,Bike,Odometer

class SwapController:
    @staticmethod
    def create_swap(driver_id, battery_id, station_id):
        swap = request.get_json()
        Swap(remainingBattery=swap["initialBattery"],
         initialBattery=swap["initialBattery"],
         driver=driver_id,
         battery=battery_id,
         station=station_id
         ).save()
        return make_response(jsonify(swap)), 201
    
    @staticmethod
    def make_swap(swap_id):
        swap = request.get_json()
        Swap.objects.get(id=swap_id).update(remainingBattery=swap["remainingBattery"], swapped=True)
        return make_response(jsonify({"message": "successfully made swap"})), 200
    
    @staticmethod
    def get_used_energy(driver_id, bike_id):
        reading_got = request.get_json()
        swaps = Swap.objects(driver=driver_id, swapped=True, timestamp=date.today()).to_json()
        reading = Bike.objects(id=bike_id, timestamp=date.today())
        data = json.loads(swaps)
        total_initial_power = 0
        total_remaining_power = 0
        for i in data:
            if i["initialBattery"]:
                total_initial_power += i["initialBattery"]
            if i["remainingBattery"]:
                total_remaining_power += i["remainingBattery"]
                total_power_used = total_initial_power - total_remaining_power
                Odometer(bike=bike_id, current_reading=reading_got["reading"]).save()
        return make_response(jsonify({"power_used": total_power_used,
                                  "kilometers": json.loads(reading.to_json())})), 200
    
    @staticmethod
    def get_swaps_made_by_driver(driver_id):
        swaps = Swap.objects(driver=driver_id).to_json()
        return make_response(swaps), 200