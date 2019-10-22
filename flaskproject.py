import RPi.GPIO as GPIO
import MCP342X #ADC
from DS18B20 import DS18B20 #Temperature class
from BMP085 import BMP085 #Pressure class
import Adafruit_BMP.BMP085
from HTU21D import HTU21D #humidity class
from TGS2600 import TGS2600 #Air Quality class
from Wind_Direction import Wind_Direction #Wind Direction class
import Interrupt_Client #Wind speed and Wind gust speed 
from Lightning import AS3935 #Lightning sensor class
from GUVA_S12SD import GUVA_S12SD # UV class

from flask import Flask, jsonify

app = Flask(__name__) 

@app.route('/') # app.route function tells which URL should call the associated function


def index():    # index function returns the following text
    return '~ Welcome to KAMK sensor hub ~'

@app.route('/api/v1/<string:sensor_id>', methods=['GET']) # Using GET method 

def get_sensor(sensor_id):  # define function get_sensor with parameter sensor_id
    print("looking for sensor", sensor_id)

    if(len(sensor_id) == 0 or sensor_id == ' '): # checking if sensor is valid
        print("sensor not provided")
        return jsonify({'sensor': 'sensor_id not provided'}) # returns as JSONIFY respond to the browser.


    if sensor_id == "Humidity": # if sensor_id matches with the following keyword...
        print("humidity if lause!!!")
        htu = HTU21D()  # Makes an object from class
        Humidity = htu.read_humidity()  # Read values from object class function
        return jsonify({'sensor_id': 'htu', 'sensor_type': 'HTU21D', 'humidity': Humidity}) # returns these values to the server

    elif sensor_id == "Pressure":
        bmp = BMP085.BMP085()
        Pressure = bmp.get_pressure()
        return jsonify({'sensor_id': 'bmp', 'sensor_type': 'BMP085', 'pressure': Pressure})
    
    elif sensor_id == "AirQuality":
        tgs = TGS2600()
        AirQuality = tgs.get_airquality()
        return jsonify({'sensor_id': 'tgs', 'sensor_type': 'TGS2600', 'airquality': AirQuality})
    
    elif sensor_id == "Wind_Direction":
        wd = Wind_Direction()
        WindDirection = wd.get_direction()
        return jsonify({'sensor_id': 'wd', 'sensor_type': 'wd', 'wind_direction': WindDirection})

    elif sensor_id == "UV":
        guva = GUVA_S12SD()
        UV = guva.get_UV()
        return jsonify({'sensor_id': 'guva', 'sensor_type': 'GUVA_S12SD', 'uv': UV})

    elif sensor_id == "LightningDistance":
        lgt = AS3935()
        LightningDistance = lgt.get_lightning_distance()
        return jsonify({'sensor_id': 'lgt', 'sensor_type': 'AS3935', 'lightningdistance': LightningDistance})

    
    elif sensor_id == "Temperature":
        ds18b = DS18B20()
        Temperature = ds18b.read_temp()
        return jsonify({'sensor_id': 'ds18b', 'sensor_type': 'DS18B20', 'temperature': Temperature})

if __name__ == "__main__":
    app.debug = True # enables debug support
    app.run(host='0.0.0.0', port=8080, debug=True) # app.run function runs the application on a local development server.
