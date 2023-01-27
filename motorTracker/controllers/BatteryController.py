import uuid
from flask import request,jsonify
import json
from datetime import date
from flask import Flask, jsonify, request, make_response,render_template
from database.db import initialize_db
from database.models import Battery

class BatteryController:
    @staticmethod
    def create_battery():
        battery = request.get_json()
        Battery(**battery).save()
        return make_response(jsonify(battery)), 201
    
    @staticmethod
    def get_batteries():
        batteries = Battery.objects().to_json()
        return make_response(batteries), 200
