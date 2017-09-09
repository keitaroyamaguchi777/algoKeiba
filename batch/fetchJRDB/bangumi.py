import sys,os
sys.path.append(os.pardir)

import MySQLdb
from util import encoding
from util.database import Keibadb

def fetch():
    print("file_bangumi_BAC.txt")
    with open("../input/file_bangumi_BAC.txt", "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()
            cur = cnn.cursor()

            insert_stmt = ("INSERT INTO sampling_bangumi(race_key,syussou_tousuu,syoukin) VALUES (%s,%s,%s)")

            for line in input.readlines():
                rec = line[0:169]
                if len(line.strip()) != 0:
                    # 場2 年2 回1 日1 R2
                    key = rec[0:8]
                    print("key : " + key)
                    # 出走頭数
                    print("rec : " + rec)
                    tousuu = encoding.bytelen(rec, 94, 96)
                    print("tousuu : "+tousuu)

                    race = encoding.bytelen(rec, 106, 124)
                    print("レース : "+race)
                    # 1着賞金
                    syoukin = encoding.bytelen(rec, 125, 130)
                    print("syoukin : " + syoukin)

                    data = (key,tousuu,syoukin)
                    cur.execute(insert_stmt, data)
                    rows = cur.fetchall()

                    for row in rows:
                        print("登録")
                        print("%s" % (row[0]))

            db.commitAndClose(cnn)
        except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)
