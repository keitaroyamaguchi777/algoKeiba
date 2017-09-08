import util
import MySQLdb
from database import Keibadb
from datetime import datetime as dt

print("file_uma_kihon_UKC.txt")
with open("input/file_kyousouba_KYG.txt", "r", encoding="cp932") as input:

        db = Keibadb()
        cnn = db.connect()

        for line in input.readlines():
            if len(line.strip()) != 0:
                rec = line

                race_key = util.bytelen(rec, 0, 8)
                print("race_key   : " + race_key)
                umaban = util.bytelen(rec, 8, 10)
                print("umaban        : " + umaban)
                blad_int = util.bytelen(rec, 10, 18)
                print("blad_int   : " + blad_int)
                kyakushitu = util.bytelen(rec, 89, 90)
                print("kyakushitu   : " + kyakushitu)
                zensou_seiseki_key = util.bytelen(rec, 203, 219)
                print("zensou_seiseki_key   : " + str(zensou_seiseki_key))
                zensou_race_key = util.bytelen(rec, 283, 291)
                print("zensou_race_key   : " + str(zensou_race_key))

                cur = cnn.cursor()
                insert_stmt = ("""INSERT INTO sampling_kyousouba(
                    race_key, umaban, blad_int,
                    kyakushitu, zensou_seiseki_key, zensou_race_key)
                    VALUES (%s,%s,%s,%s,%s,%s)""")
                data = (race_key, umaban, blad_int, kyakushitu,
                        zensou_seiseki_key, zensou_race_key)
                cur.execute(insert_stmt, data)
                rows = cur.fetchall()

                for row in rows:
                    print("")
                    print("%s" % (row[0]))

        db.commitAndClose(cnn)

    except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)
