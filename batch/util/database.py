import MySQLdb

class Keibadb:

    def connect(self):
        return MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='admin',
            db='keibadb',
            charset="utf8")

    def commitAndClose(self, cnn):
        cnn.commit()
        cur = cnn.cursor()
        cur.close()
        cnn.close()
