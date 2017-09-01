print("file_bangumi_BAC.txt")
with open("file_bangumi_BAC.txt", "r", encoding="EUC-JP") as input:
    for line in input.readlines():
        rec = line[0:176]
        if len(line.strip()) != 0:
            """
            ba = rec[0:2]
            year = rec[2:4]
            cnt = rec[4:5]
            r = rec[5:6]
            dt = rec[7:14]
            """
            key = rec[0:14]
            print("key : " + key)

"""
print("file_chokuzen_TYB.txt")
with open("file_chokuzen_TYB.txt", "r", encoding="EUC-JP") as input:
    for line in input.readlines():
        rec = line[0:128]
        if len(line.strip()) != 0:
            # 場2 年2 回1 日1 R2
            key = rec[0:8]
            print("key : " + key)
            # 斤量
            kinryou = rec[59:62] # rec[65:68]
            # 馬体重
            weight = rec[82:85]
            # 馬体重増減
            zougen = rec[85:88]
            print("kinryou : " + kinryou)
            print("weight : " + weight)
            print("zougen : " + zougen)
"""






