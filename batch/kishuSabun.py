import util

print("file_bangumi_BAC.txt")
with open("input/file_kishu_sabun_KSA.txt", "r", encoding="EUC-JP") as input:

    import MySQLdb
    try:
        cnn = MySQLdb.connect(host='localhost',
                              port=3306,
                              user='root',
                              passwd='password01',
                              db='keibadb',
                              charset="utf8")

        for line in input.readlines():
            if len(line.strip()) != 0:
                rec = line

                kishu_code = util.bytelen(rec, 0, 5)
                print("kishu_code     : " + kishu_code)
                kishu_mei = util.bytelen(rec, 14, 26)
                print("kishu_mei      : " + kishu_mei)
                heiti_1 = int(util.bytelen(rec, 199, 204))
#                print("heiti_seiseki1 : " + str(heiti_1))
                heiti_2 = int(util.bytelen(rec, 204, 209))
#                print("heiti_seiseki2 : " + str(heiti_2))
                heiti_3 = int(util.bytelen(rec, 209, 214))
#                print("heiti_seiseki3 : " + str(heiti_3))
                heiti_tyakugai = int(util.bytelen(rec, 214, 219))
#                print("heiti_tyakugai : " + str(heiti_tyakugai))
                fukushou_kaisu = heiti_1 + heiti_2 + heiti_3
#                print("fukushou_kaisu : " + str(fukushou_kaisu))
                shuso_kaisu = fukushou_kaisu + heiti_tyakugai
#                print("shuso_kaisu : " + str(shuso_kaisu))

                fukusho_ritsu = 0
                if(fukushou_kaisu != 0 and shuso_kaisu != 0):
                    fukusho_ritsu = fukushou_kaisu / shuso_kaisu
                    print("fukusho_ritsu : " + str(fukusho_ritsu*100) + "%   " + str(fukushou_kaisu) + "/" + str (shuso_kaisu))

                cur = cnn.cursor()
                insert_stmt = ("INSERT INTO sampling_kishu_sabun(kisyu_code, kisyu_mei, kisyu_fukusyou) VALUES (%s,%s,%s)")
                data = (kishu_code, kishu_mei, fukusho_ritsu)
                cur.execute(insert_stmt, data)
                rows = cur.fetchall()

                for row in rows:
                    print("")
                    print("%s" % (row[0]))

        cnn.commit()
        cur.close()
        cnn.close()

    except MySQLdb.Error as e:
            print('MySQLdb.Error: ', e)
