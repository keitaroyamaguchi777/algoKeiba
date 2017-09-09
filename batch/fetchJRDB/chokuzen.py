import sys,os
sys.path.append(os.pardir)

import MySQLdb
from util import encoding
from util.database import Keibadb
from datetime import datetime as dt

def fetch():
    print("file_chokuzen_TYB.txt")
    with open("../input/file_chokuzen_TYB.txt", "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()

            for line in input.readlines():
                if len(line.strip()) != 0:
                    rec = line

                    race_key = encoding.bytelen(rec, 0, 8)
                    print("race_key   : " + race_key)
                    umaban = encoding.bytelen(rec, 8, 10)
                    print("umaban        : " + umaban)
                    kishu_code = encoding.bytelen(rec, 48, 53)
                    print("kishu_code   : " + kishu_code)

                    kinryou = encoding.bytelen(rec, 65, 68)
                    if (kinryou.strip() != "0") :
                        kinryou = int(kinryou) / 10
                    print("kinryou   : " + str(kinryou))

                    bataijyu = encoding.bytelen(rec, 88, 91)
                    if (bataijyu.strip() == "") :
                        bataijyu = ""
                    print("bataijyu   : " + str(bataijyu))
                    taijyu_zougen = encoding.bytelen(rec, 91, 94).replace(" ","").strip()
                    if (taijyu_zougen == "") :
                        taijyu_zougen = ""
                    print("taijyu_zougen  : " + str(taijyu_zougen))

                    cur = cnn.cursor()
                    insert_stmt = ("""INSERT INTO sampling_chokuzen(
                        race_key, umaban, kishu_code,
                        kinryou, bataijyu, taijyu_zougen)
                        VALUES (%s,%s,%s,%s,%s,%s)""")
                    data = (race_key, umaban, kishu_code,
                            kinryou, bataijyu, taijyu_zougen)
                    cur.execute(insert_stmt, data)
                    rows = cur.fetchall()

                    for row in rows:
                        print("")
                        print("%s" % (row[0]))

            db.commitAndClose(cnn)

        except MySQLdb.Error as e:
                print('MySQLdb.Error: ', e)
