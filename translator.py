import csv
from read import *

TTSMap = dict()
STTMap = dict()

def Get_Config():
    global TTSMap
    global STTMap
    TTSMap = tradition_to_simplify()
    STTMap = simplify_to_tradition()

def Traditional_To_Simplified(txt):
    ret = ""
    i = 0
    while i < len(txt):
        for j in range(min(len(txt) - i, 4), 0, -1):
            if txt[i:i + j] in TTSMap:
                ret += TTSMap[txt[i:i + j]]
                i += j
                break
            if j == 1:
                ret += txt[i]
                i += 1
    return ret

def Simplified_To_Traditional(txt):
    ret = ""
    i = 0
    while i < len(txt):
        for j in range(min(len(txt) - i, 4), 0, -1):
            if txt[i:i + j] in STTMap:
                ret += STTMap[txt[i:i + j]]
                i += j
                break
            if j == 1:
                ret += txt[i]
                i += 1
    return ret

if __name__ == '__main__':
    Get_Config()
    print(Traditional_To_Simplified("天好藍要和你一起看，起風時由你来温暖。"))
    print(Simplified_To_Traditional("天好蓝要和你一起看，起风时由你来温暖。"))