from DS18B20 import DS18B20 #Temperature class
import BMP085 as BMP085 #Pressure class
from HTU21D import HTU21D #humidity class
from TGS2600 import TGS2600 #Air Quality class
from Wind_Direction import Wind_Direction #Wind Direction class
import Interrupt_Client #Wind speed and Wind gust speed 
from Lightning import AS3935 #Lightning sensor class
from GUVA_S12SD import GUVA_S12SD # UV class

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '~ Welcome to KAMK sensor hub ~'

@app.route('/api/v1/<string:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
  print("looking for sensor", sensor_id)

    if(len(sensor_id) == 0 or sensor_id == ' '):
        print("sensor not provided")
        return jsonify({'sensor': 'sensor_id not provided'})


     if sensor_id == "Humidity":
        Humidity = htu.read_humidity() 
        return jsonify({'sensor_id': 'htu', 'sensor_type': 'HTU21D', 'humidity', Humidity})

    elif sensor_id == "Pressure":
        Pressure = bmp.get_pressure() 
        return jsonify({'sensor_id': 'bmp', 'sensor_type': 'BMP085', 'pressure', Pressure})
    
    elif sensor_id == "AirQuality"
        AirQuality = tgs.get_airquality()
        return jsonify({'sensor_id': 'tgs', 'sensor_type': 'TGS2600', 'airquality', AirQuality})
    
    elif sensor_id == "Wind_Direction"
        WindDirection = wd.get_direction()
        return jsonify({'sensor_id': 'wd', 'sensor_type': 'Wind_Direction', 'winddirection', WindDirection})

    elif sensor_id == "UV"
        UV = guva.get_UV()
        return jsonify({'sensor_id': 'uv', 'sensor_type': 'UV', 'uv', UV})

    
    elif sensor_id == "LightningDistance"
        LightningDistance = lgt.get_lightning_distance()
        return jsonify({'sensor_id': 'lgt', 'sensor_type': 'LightningDistance', 'lightningdistance', LightningDistance })

    
    elif sensor_id == "LightningDistance"
        LightningDistance = lgt.get_lightning_distance()
        return jsonify({'sensor_id': 'lgt', 'sensor_type': 'LightningDistance', 'lightningdistance', LightningDistance })


   







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
