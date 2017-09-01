import MySQLdb

def connect():
    try:
        cnn = MySQLdb.connect(host='localhost',
                        port=3306,
                        user='root',
                        passwd='password01',
                        db='keibadb',
                        charset="utf8")
    
    except MySQLdb.Error as e:
        print('MySQLdb.connect: ', e)

    return cnn

def showTables():
    try:
        cnn = connect()
        cur = cnn.cursor()
        cur.execute(""" show tables """)

        rows = cur.fetchall()
        for row in rows:
            print("%s" % (row[0]))

        cnn.commit()
        cur.close()
        cnn.close()
    except MySQLdb.Error as e:
        print('MySQLdb.showTables: ', e)


#    pref_cd = "tables"
#    cur.execute(""" show %s """, (pref_cd, ))

showTables()

