import pandas as pd
import re

def now(birthday):
    today = int(pd.to_datetime('today').strftime('%Y%m%d'))
    birth = int(pd.to_datetime('birthday').strftime('%Y%m%d'))
    return int((today - birth) / 10000)

def fetchDate(yymmdd):
    print("yymmdd : " + yymmdd)
    dateStr = "";
    ret = re.search("[0-9]{6}",yymmdd)

    if ret == None:
        return dateStr

    ymd = re.search("[0-9]{6}",yymmdd).group()
    year = ymd[0:2]
    if int(year) <= 99 :
        dateStr = "19" + ymd
    else :
        dateStr = "20" + ymd

    # return dt.strptime(dateStr, '%Y%m%d')
    return dateStr
