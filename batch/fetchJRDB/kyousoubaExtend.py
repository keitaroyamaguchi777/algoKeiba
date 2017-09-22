import sys,os
sys.path.append(os.pardir)

import MySQLdb
from util import encoding, profile
from util.database import Keibadb
from datetime import datetime as dt

def fetch(filename):
    print("file_kyousouba_extend_KKA : " + filename)
    make = profile.fetchDate(filename)
    with open(filename, "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()

            cur = cnn.cursor()
            insert_stmt = ("""INSERT INTO sampling_kyousouba_extend (
                race_key, umaban, jra_seiseki_1chaku,
                jra_seiseki_2chaku, jra_seiseki_3chaku, jra_seiseki_chakugai)
                VALUES (%s,%s,%s,%s,%s,%s)""")

            for line in input.readlines():
                if len(line.strip()) != 0:
                    rec = line

                    race_key = encoding.bytelen(rec, 0, 8)
                    # print("race_key   : " + race_key)
                    umaban = encoding.bytelen(rec, 8, 10)
                    # print("umaban     : " + umaban)

                    jra_seiseki_1chaku = encoding.bytelen(rec, 10, 13)
                    if (jra_seiseki_1chaku.strip() == ""):
                        jra_seiseki_1chaku = 0
                    # print("jra_seiseki_1chaku   : " + str(jra_seiseki_1chaku))
                    jra_seiseki_2chaku = encoding.bytelen(rec, 13, 16)
                    if (jra_seiseki_2chaku.strip() == ""):
                        jra_seiseki_2chaku = 0
                    # print("jra_seiseki_2chaku   : " + str(jra_seiseki_2chaku))
                    jra_seiseki_3chaku = encoding.bytelen(rec, 16, 19)
                    if (jra_seiseki_3chaku.strip() == ""):
                        jra_seiseki_3chaku = 0
                    # print("jra_seiseki_3chaku   : " + str(jra_seiseki_3chaku))
                    jra_seiseki_chakugai = encoding.bytelen(rec, 19, 22)
                    if (jra_seiseki_chakugai.strip() == ""):
                        jra_seiseki_chakugai = 0
                    # print("jra_seiseki_chakugai  : " + str(jra_seiseki_chakugai))

                    data = (race_key, umaban, jra_seiseki_1chaku,
                            jra_seiseki_2chaku, jra_seiseki_3chaku, jra_seiseki_chakugai)

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
