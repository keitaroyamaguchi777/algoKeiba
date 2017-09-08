import util
import MySQLdb
from datetime import datetime as dt

print("file_uma_kihon_UKC.txt")
with open("input/file_kyousouba_extend_KKA.txt", "r", encoding="cp932") as input:

    from database import Keibadb
    try:
        db = Keibadb()
        cnn = db.connect()

        for line in input.readlines():
            if len(line.strip()) != 0:
                rec = line

                race_key = util.bytelen(rec, 0, 8)
                print("race_key   : " + race_key)
                umaban = util.bytelen(rec, 8, 10)
                print("umaban     : " + umaban)

                jra_seiseki_1chaku = util.bytelen(rec, 10, 13)
                if (jra_seiseki_1chaku.strip() == ""):
                    jra_seiseki_1chaku = 0
                print("jra_seiseki_1chaku   : " + str(jra_seiseki_1chaku))
                jra_seiseki_2chaku = util.bytelen(rec, 13, 16)
                if (jra_seiseki_2chaku.strip() == ""):
                    jra_seiseki_2chaku = 0
                print("jra_seiseki_2chaku   : " + str(jra_seiseki_2chaku))
                jra_seiseki_3chaku = util.bytelen(rec, 16, 19)
                if (jra_seiseki_3chaku.strip() == ""):
                    jra_seiseki_3chaku = 0
                print("jra_seiseki_3chaku   : " + str(jra_seiseki_3chaku))
                jra_seiseki_chakugai = util.bytelen(rec, 19, 22)
                if (jra_seiseki_chakugai.strip() == ""):
                    jra_seiseki_chakugai = 0
                print("jra_seiseki_chakugai  : " + str(jra_seiseki_chakugai))

                cur = cnn.cursor()
                insert_stmt = ("""INSERT INTO sampling_kyousouba_extend (
                    race_key, umaban, jra_seiseki_1chaku,
                    jra_seiseki_2chaku, jra_seiseki_3chaku, jra_seiseki_chakugai)
                    VALUES (%s,%s,%s,%s,%s,%s)""")

                data = (race_key, umaban, jra_seiseki_1chaku,
                        jra_seiseki_2chaku, jra_seiseki_3chaku, jra_seiseki_chakugai)

                cur.execute(insert_stmt, data)
                rows = cur.fetchall()

                for row in rows:
                    print("")
                    print("%s" % (row[0]))

        db.commitAndClose(cnn)

    except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)
