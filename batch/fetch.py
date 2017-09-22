# coding: utf-8
import os,imghdr,shutil
import re  # regex
from fetchJRDB import bangumi, chokuzen, kishuSabun, kyousouba, kyousoubaExtend, umaKihon, zensou

def get_file_list(path):
    file_list = []
    for (root, dirs, files) in os.walk(path):
        for file in files:
            target = os.path.join(root,file).replace("\\", "/")
            body, ext = os.path.splitext(target)
            if os.path.isfile(target):
                # if imghdr.what(target) != None :
                if ext == ".txt" :
                    file_list.append(target)
    return file_list


if __name__ == "__main__":
    path = "./input/data/"
    file_list = get_file_list(path) 

    for fname in file_list :
        if "UKC" in fname : # OK
            umaKihon.fetch(fname);
            continue
        """
        if "BAC" in fname :             
            bangumi.fetch(fname);
            continue
        if "TYB" in fname :  # OK 
            chokuzen.fetch(fname);
            continue
        if "KSA" in fname : 
            kishuSabun.fetch(fname);
            continue
        if "KYG"  in fname : # OK 
            kyousouba.fetch(fname);
            continue
        if "KKA"  in fname : # OK 
            kyousoubaExtend.fetch(fname);
            continue
        if "ZEC" in fname : # OK 
            zensou.fetch(fname);
            continue
        """
        
    print("end...")
    