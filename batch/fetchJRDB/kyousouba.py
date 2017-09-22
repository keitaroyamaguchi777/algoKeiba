import sys,os
sys.path.append(os.pardir)

import util
import MySQLdb
from util import encoding, profile
from util.database import Keibadb
from datetime import datetime as dt

def fetch(filename):
    print("file_kyousouba_KYG : " + filename)
    history = profile.fetchDate(filename)
    with open(filename, "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()

            cur = cnn.cursor()
            insert_stmt = ("""INSERT INTO sampling_kyousouba(
                history, race_key, umaban, blad_int,
                kyakushitu, zensou_seiseki_key, zensou_race_key)
                VALUES (%s,%s,%s,%s,%s,%s,%s)""")

            for line in input.readlines():
                if len(line.strip()) != 0:
                    rec = line

                    race_key = encoding.bytelen(rec, 0, 8)
                    # print("race_key   : " + race_key)
                    umaban = encoding.bytelen(rec, 8, 10)
                    # print("umaban        : " + umaban)
                    blad_int = encoding.bytelen(rec, 10, 18)
                    # print("blad_int   : " + blad_int)
                    kyakushitu = encoding.bytelen(rec, 89, 90)
                    # print("kyakushitu   : " + kyakushitu)
                    zensou_seiseki_key = encoding.bytelen(rec, 203, 219)
                    # print("zensou_seiseki_key   : " + str(zensou_seiseki_key))
                    zensou_race_key = encoding.bytelen(rec, 283, 291)
                    # print("zensou_race_key   : " + str(zensou_race_key))

                    data = (history, race_key, umaban, blad_int, kyakushitu,
                            zensou_seiseki_key, zensou_race_key)
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
