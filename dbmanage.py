import pymysql

class Db:
    def __init__(self,id,pw,db):
        try:
            self.conn = pymysql.connect(host="localhost", user=id, password=pw, db=db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("DB connection error")
    def __del__(self):
        self.conn.close()
    
    def initTable(self):
        sql = """create table if not exists envinfo(
                no INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                humidity double,
                temperature double
                );"""
        self.cursor.execute(sql)
    
    def insertData(self, humi, temp):
        sql = "INSERT INTO envinfo VALUES(NULL, {}, {})".format(humi, temp)
        self.cursor.execute(sql)
        self.conn.commit()
        
    def getAvg(self):
        sql = "select AVG(humidity), AVG(temperature) from envinfo"
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        print("Humidity %2.1f, Temperature %2.1f"%(data[0], data[1]))
    
if __name__ == "__main__":
    db = Db()
    db.initTable()
    db.insertData(44,11)
    db.insertData(44,11)
    db.insertData(44,11)
    db.insertData(999,111)
    db.getAvg()