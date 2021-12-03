import Adafruit_DHT

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT11
        
    def getSensorInfo(self):
        humi, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return {"humi":humi, "temp":temp}
    
if __name__ == "__main__":
    sensor = Sensor(4)
    print(sensor.getSensorInfo())