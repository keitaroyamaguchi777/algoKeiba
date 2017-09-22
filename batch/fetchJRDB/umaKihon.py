import sys,os
sys.path.append(os.pardir)

from datetime import datetime as dt
import MySQLdb
from util import encoding, profile
from util.database import Keibadb

def fetch(filename):
    print("file_uma_kihon_UKC : " + filename)
    history = profile.fetchDate(filename)
    with open(filename, "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()
            cur = cnn.cursor()
            insert_stmt = ("""INSERT INTO sampling_uma_kihon(
                history, blad_int, name, birthday, sex)
                VALUES (%s,%s,%s,%s,%s)""")

            for line in input.readlines():
                if len(line.strip()) != 0:
                    rec = line

                    blad_int = encoding.bytelen(rec, 0, 8)
                    # print("blad_int   : " + blad_int)
                    name = encoding.bytelen(rec, 8, 44)
                    # print("name        : " + name)
                    strbirthday = encoding.bytelen(rec, 157, 165)
                    birthday = dt.strptime(strbirthday, '%Y%m%d')
                    # print("birthday        : " + str(birthday))
                    sex = encoding.bytelen(rec, 44, 45)
                    # print("sex        : " + sex)

                    data = (history, blad_int, name, birthday, sex)
                    cur.execute(insert_stmt, data)
                    rows = cur.fetchall()

                    """
                    for row in rows:
                        print("")
                        print("%s" % (row[0]))
                    """

            db.commitAndClose(cnn)

        except MySQLdb.Error as e:
                print('MySQLdb.Error: ', e)
