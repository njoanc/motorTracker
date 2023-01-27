from flask import request,jsonify
from flask import  jsonify, request, make_response
from database.models import Station

class StationController:

    @staticmethod
    def create_station():
        station = request.get_json()
        Station(location=station["location"]).save()
        return make_response(jsonify(station)), 201


    @staticmethod
    def get_stations():
        stations = Station.objects().to_json()
        return make_response(stations), 200