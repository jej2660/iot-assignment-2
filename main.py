from dbmanage import Db
from controller import Sensor
import time
class Worker:
    def __init__(self):
        self.db = Db(id="yourID",pw="yourPW",db="yourDB")
        self.sensor = Sensor(pin=4)#pin Number

    def run(self):
        self.db.initTable()
        while True:
            tmp = self.sensor.getSensorInfo()
            self.db.insertData(tmp[0], tmp[1])
            self.db.getAvg()
            time.sleep(5)
if __name__ == "__main__":
    worker = Worker()
    worker.run()
            
            
    