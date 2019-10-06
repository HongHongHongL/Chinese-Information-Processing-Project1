import csv
import codecs
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
    import sys
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-e', type='string', dest='encoding',
                      help='encoding')
    parser.add_option('-f', type='string', dest='file_in',
                      help='input file (- for stdin)')
    parser.add_option('-t', type='string', dest='file_out',
                      help='output file')
    (options, args) = parser.parse_args()
    if not options.encoding:
        parser.error('encoding must be set')
    if options.file_in:
        if options.file_in == '-':
            file_in = sys.stdin
        else:
            file_in = codecs.open(options.file_in, 'r+', encoding='utf-8')
    else:
        file_in = sys.stdin
    if options.file_out:
        if options.file_out == '-':
            file_out = sys.stdout
        else:
            file_out = codecs.open(options.file_out, 'wb', encoding='utf-8')
    else:
        file_out = sys.stdout

    if options.encoding == "STT":
        for line in file_in:
            file_out.write(Simplified_To_Traditional(line))
    else:
        for line in file_in:
            file_out.write(Traditional_To_Simplified(line))
