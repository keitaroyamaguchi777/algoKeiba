import sys,os
sys.path.append(os.pardir)

import math, decimal
import util
import MySQLdb
from util import encoding, profile
from util.database import Keibadb

def fetch(filename):
    print("file_kishu_sabun_KSA : " + filename)
    history = profile.fetchDate(filename)
    with open(filename, "r", encoding="cp932") as input:
        try:
            db = Keibadb()
            cnn = db.connect()
            cur = cnn.cursor()
            insert_stmt = ("""INSERT INTO sampling_kishu_sabun(
                    history, kishu_code, kishu_mei, kishu_fukusyou)
                    VALUES (%s,%s,%s,%s)""")

            for line in input.readlines():
                if len(line.strip()) != 0:
                    rec = line

                    kishu_code = encoding.bytelen(rec, 0, 5)
                    # print("kishu_code     : " + kishu_code)
                    kishu_mei = encoding.bytelen(rec, 14, 26)
                    # print("kishu_mei      : " + kishu_mei)
                    heiti_1 = int(encoding.bytelen(rec, 199, 204))
                    heiti_2 = int(encoding.bytelen(rec, 204, 209))
                    heiti_3 = int(encoding.bytelen(rec, 209, 214))
                    heiti_tyakugai = int(encoding.bytelen(rec, 214, 219))
                    fukushou_kaisu = heiti_1 + heiti_2 + heiti_3
                    shuso_kaisu = fukushou_kaisu + heiti_tyakugai

                    fukusho_ritsu = 0.00
                    if(fukushou_kaisu != 0 and shuso_kaisu != 0):
                        with decimal.localcontext() as ctx:
                            ctx.rounding = decimal.ROUND_FLOOR
                            fukusho_ritsu = round(decimal.Decimal(fukushou_kaisu / shuso_kaisu), 9)

                    # print("fukusho_ritsu : " + str(fukusho_ritsu*100) + "%   " + str(fukushou_kaisu) + "/" + str (shuso_kaisu))

                    data = (history, kishu_code, kishu_mei, fukusho_ritsu)
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
