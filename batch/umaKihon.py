import util
from datetime import datetime as dt
import MySQLdb
from database import Keibadb

print("file_uma_kihon_UKC.txt")
with open("input/file_uma_kihon_UKC.txt", "r", encoding="cp932") as input:
    try:
        db = Keibadb()
        cnn = db.connect()

        for line in input.readlines():
            if len(line.strip()) != 0:
                rec = line

                blad_int = util.bytelen(rec, 0, 8)
                print("blad_int   : " + blad_int)
                name = util.bytelen(rec, 8, 44)
                print("name        : " + name)
                strbirthday = util.bytelen(rec, 157, 165)
                birthday = dt.strptime(strbirthday, '%Y%m%d')
                print("birthday        : " + str(birthday))
                sex = util.bytelen(rec, 44, 45)
                print("sex        : " + sex)

                cur = cnn.cursor()
                insert_stmt = ("""INSERT INTO sampling_uma_kihon(
                    blad_int, name, birthday, sex)
                    VALUES (%s,%s,%s,%s)""")
                data = (blad_int, name, birthday, sex)
                cur.execute(insert_stmt, data)
                rows = cur.fetchall()

                for row in rows:
                    print("")
                    print("%s" % (row[0]))

        db.commitAndClose(cnn)

    except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)
