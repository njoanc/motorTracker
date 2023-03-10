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


app.add_url_rule('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


app.add_url_rule("/driver/<bike_id>", methods=["POST"], view_func=DriverController.create_battery)
app.add_url_rule("/drivers", methods=["GET"], view_func=DriverController.get_drivers)
app.add_url_rule("/driver/driver_id", methods=["GET"], view_func=DriverController.get_one_drivers)



app.add_url_rule("/battery", methods=["POST"], view_func=BatteryController.create_battery)
app.add_url_rule("/batteries", methods=["GET"],view_func=BatteryController.get_batteries)


app.add_url_rule("/station", methods=["POST"], view_func=StationController.create_station)
app.add_url_rule("/stations", methods=["GET"],view_func=StationController.get_stations)



app.add_url_rule("/bike", methods=["POST"], view_func=BikeController.create_bike)
app.add_url_rule("/bike/<bike_id>/day", methods=["GET"], view_func=BikeController.get_kilometers_done)



app.add_url_rule("/swap/driver/<driver_id>/battery/<battery_id>/station/<station_id>", methods=["POST"], view_func=SwapController.create_swap)
app.add_url_rule("/swap/<swap_id>", methods=["PUT"], view_func=SwapController.make_swap)
app.add_url_rule("/swap/driver/<driver_id>/bike/<bike_id>/day", methods=["POST"], view_func=SwapController.get_used_energy)
app.add_url_rule("/swap/driver/<driver_id>", methods=["GET"], view_func=SwapController.get_swaps_made_by_driver)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
