def bytelen(str, start, end, encoding='EUC-JP'):
        encStr = str.encode(encoding)[start:end]
        decStr = eval("{}".format(encStr)).decode(encoding)
        return decStr

