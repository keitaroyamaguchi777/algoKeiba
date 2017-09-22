import sys,os
sys.path.append(os.pardir)

import util
import MySQLdb
from util import encoding, profile
from util.database import Keibadb
from datetime import datetime as dt

def fetch(filename):
    print("file_zensou_ZEC : " + filename)
    make = profile.fetchDate(filename)
    with open(filename, "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()
            cur = cnn.cursor()
            insert_stmt = ("""INSERT INTO sampling_zensou(
                seiseki_key, zensou_kyori, zensou_tm_sa,
                zensou_3ftm_before, zensou_3ftm_after)
                VALUES (%s,%s,%s,%s,%s)""")
                        
            for line in input.readlines():
                if len(line.strip()) != 0:
                    rec = line

                    seiseki_key = encoding.bytelen(rec, 10, 26)
                    # print("seiseki_key   : " + str(seiseki_key))
                    zensou_kyori = encoding.bytelen(rec, 62, 66)
                    # print("zensou_kyori   : " + zensou_kyori)
                    zensou_tm_sa = encoding.bytelen(rec, 255, 258)
                    if (zensou_tm_sa.strip() == "") :
                        zensou_tm_sa = 0.0
                    else :
                        zensou_tm_sa = int(zensou_tm_sa) / 10
                    # print("zensou_tm_sa        : " + str(zensou_tm_sa))

                    zensou_3ftm_before = encoding.bytelen(rec, 258, 261)
                    if (zensou_3ftm_before.strip() == "") :
                        zensou_3ftm_before = 0.0
                    else :
                        zensou_3ftm_before = int(zensou_3ftm_before) / 10
                    # print("zensou_3ftm_before  : " + str(zensou_3ftm_before))

                    zensou_3ftm_after = encoding.bytelen(rec, 261, 264)
                    if (zensou_3ftm_after.strip() == "") :
                        zensou_3ftm_after = 0.0
                    else :
                        zensou_3ftm_after = int(zensou_3ftm_after) / 10
                    # print("zensou_3ftm_after   : " + str(zensou_3ftm_after))


                    data = (seiseki_key, zensou_kyori, zensou_tm_sa,
                            zensou_3ftm_before, zensou_3ftm_after)
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
