import json
from datetime import date

from flask import Flask, jsonify, request, make_response,render_template
from database.db import initialize_db
from database.models import Driver, Battery, Station, Bike, Swap, Odometer
from controllers import BatteryController, DriverController, StationController, BikeController, SwapController,Odometercontroller

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/motors'
}
initialize_db(app)


@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


@app.route("/driver/<bike_id>", methods=["POST"], view_func=DriverController.create_battery)
@app.route("/drivers", methods=["GET"], view_func=DriverController.get_drivers)
@app.route("/driver/driver_id", methods=["GET"], view_func=DriverController.get_one_drivers)



@app.route("/battery", methods=["POST"], view_func=BatteryController.create_battery)
@app.route("/batteries", methods=["GET"],view_func=BatteryController.get_batteries)


@app.route("/station", methods=["POST"], view_func=StationController.create_station)
@app.route("/stations", methods=["GET"],view_func=StationController.get_stations)



@app.route("/bike", methods=["POST"], view_func=BikeController.create_bike)
@app.route("/bike/<bike_id>/day", methods=["GET"], view_func=BikeController.get_kilometers_done)



@app.route("/swap/driver/<driver_id>/battery/<battery_id>/station/<station_id>", methods=["POST"])
def create_swap(driver_id, battery_id, station_id):
    swap = request.get_json()
    Swap(remainingBattery=swap["initialBattery"],
         initialBattery=swap["initialBattery"],
         driver=driver_id,
         battery=battery_id,
         station=station_id
         ).save()
    return make_response(jsonify(swap)), 201


@app.route("/swap/<swap_id>", methods=["PUT"])
def make_swap(swap_id):
    swap = request.get_json()
    Swap.objects.get(id=swap_id).update(remainingBattery=swap["remainingBattery"], swapped=True)
    return make_response(jsonify({"message": "successfully made swap"})), 200


@app.route("/swap/driver/<driver_id>/bike/<bike_id>/day", methods=["POST"])
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





@app.route("/swap/driver/<driver_id>", methods=["GET"])
def get_swaps_made_by_driver(driver_id):
    swaps = Swap.objects(driver=driver_id).to_json()
    return make_response(swaps), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
