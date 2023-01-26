## Product overview
 MotorTracker is a tool that facilitates management of electric bikes businesses in Rwanda. It enables  calculating  the amount of energy a driver has used in a day and the kilometers the same driver has done.

## Development set up

#### Getting a copy on your local machine
- Clone the repo
	```
    git clone https://github.com/njoanc/motorTracker.git
    ```
- Installing the virtual env 

    ```
    python3 -m pip install virtualenv |OR| python3 -m pip install --user virtualenv
    ```
- Creating your virtual env

    ```
    virtualenv <name of your virtualenv>  ie: virtualenv my_venv
    ```
- Activating the virtual env

    ``` 
    source my_venv/bin/activate 
    ```
- Deactivating the virtualenv   

    ``` deactivate```
 
- Installing dependencies 

    ``` 
    pip3 install -r requirements.txt
    ```

- Run application.
    ```
    flask run |OR| python3 app.py
    ```
- Databases and Migrations 

   This service is built using MongoDB, you need to have MongoDB installed and you don't need to run any migrations 



##### ENDPOINTS TO BE TESTED
  - Create bike 
	``` 
	POST /bike 
	```
	
	`` {
	"name": "audi",
	"odometer_reading": 900 }
	``
  - Getting all bikes
  	```
    GET /bikes
  	```
 - Create a driver 
    ``` 
    POST /driver/<bike_id>
    ```
    ``{
	"name": "Jeanne d'Arc" }``
	
- Get drivers

    ``` 
    GET /drivers
    ```
- Get one Driver 
  ```
  GET /driver/driver_id 
  ```
- Create a battery 
    ```
    POST /battery 
    ```
    ``{
	"voltage": 150,
	"capacity": 90 }``
- Get all batteries 
    ``` 
    GET /batteries
    ```
- Create Swapping station
    ``` 
    POST /station
    ```
    ``{
	"location": "Kacyiru"
}``

- Getting all stations 
    ``` 
    GET /stations
    ```
- Creating the first swap [ Here a driver gets his first battery]
    ```  
    POST /swap/driver/<driver_id>/battery/<battery_id>/station/<station_id>
    ```
    ``{
	"initialBattery": 93
}``

- Completing a swap [ A driver returns the battery to get another one]
    ```
     PUT /swap/<swap_id>
    ```
    ``{
	"remainingBattery": 30
}``

- Getting total energy used in a day [Because we retrieve this at the end of the day we also take the odometer reading]
    ``` 
    POST /swap/driver/<driver_id>/bike/<bike_id>/day
    ```
    ``{
	"reading": 300
}``
- Getting Kilometers done in a day 

    ```  
    GET /bike/<bike_id>/day
    ```
- Getting swaps done by one driver a day
    ``` 
    GET /swap/driver/<driver_id>
    ```

## Built with
- Python version  3
- Flask
- MongoDb


