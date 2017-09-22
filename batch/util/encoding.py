def bytelen(str, start, end, encoding='cp932'):
    encStr = str.encode(encoding)[start:end]
    decStr = eval("{}".format(encStr)).decode(encoding)
    return decStr
