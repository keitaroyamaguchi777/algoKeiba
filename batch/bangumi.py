import MySQLdb
from database import Keibadb

#[半角文字 = 1byte/ 全角文字 = 3byte (UTF-8)]
#num_bytesに指定したbyte数の文字列を返却する。
def byteCheck(str, num_bytes, encoding='utf-8'):
    while len(str.encode(encoding)) > num_bytes:
        str = str[:-1]
    return str

def bytelen(str, start, end, encoding='cp932'):
	encStr = str.encode(encoding)[start:end]
	decStr = eval("{}".format(encStr)).decode(encoding)
	return decStr


print("file_bangumi_BAC.txt")
with open("input/file_bangumi_BAC.txt", "r", encoding="cp932") as input:
    try:
        db = Keibadb()
        cnn = db.connect()
        cur = cnn.cursor()

        insert_stmt = ("INSERT INTO sampling_bangumi(race_key,syussou_tousuu,syoukin) VALUES (%s,%s,%s)")

        for line in input.readlines():
            #byteCheckで指定バイト数に取得項目のバイト数を指定し、文字列を取得する。
            #上記文字列から指定項目のみを切り出す。
            rec = line[0:169]
            if len(line.strip()) != 0:
                # 場2 年2 回1 日1 R2
                key = rec[0:8]
                print("key : " + key)
                # 出走頭数
                print("rec : " + rec)
                tousuu = bytelen(rec, 94, 96)
                print("tousuu : "+tousuu)

                race = bytelen(rec, 106, 124)
                print("レース : "+race)
                # 1着賞金
                syoukin = bytelen(rec, 125, 130)
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
