import json
import os
import numpy as np
from collections import defaultdict

dic = {"a":(2.060, -0.669, 1.083),
           "c":(0.000, -3.718, 1.859),
           "d":(1.201, -0.390, 1.263),
           "e":(-0.689, -0.948, 1.172),
           "f":(-1.662, -2.286, 1.413),
           "g":(0.000, 2.300, 1.150),
           "h":(0.000, -1.643, 1.643),
           "i":(-1.444, 1.987, 1.228),
           "k":(0.727, 1.000, 1.236),
           "l":(-1.930, -0.627, 1.015),
           "m":(1.902, -2.616, 1.617),
           "n":(0.818, -1.125, 1.391),
           "p":(-1.259, -0.409, 1.324),
           "q":(1.336, 0.434, 1.405),
           "r":(0.000, 1.257, 1.257),
           "s":(1.385, 1.906, 1.178),
           "t":(-0.747, 1.028, 1.271),
           "v":(-2.212, 0.719, 1.163),
           "w":(3.726, 1.211, 1.959),
           "y":(-1.460, 0.474, 1.535),
           "x":(0,0,0)}

def za(aminolist):
    al = aminolist
    xbuf = 0
    ybuf = 0
    zbuf = 0    
    Xlist = []
    Ylist = []
    Zlist = []

    for ch in al:
        if ch in dic:
            xbuf = xbuf + dic[ch][0]
            ybuf = ybuf + dic[ch][1]
            zbuf = zbuf + dic[ch][2]
            Xlist.append(xbuf)
            Ylist.append(ybuf)
            Zlist.append(zbuf)
        elif ch == "\n":
            break
        else:
            print("存在しない文字です")
            print(ch)

    veclist = [Xlist,Ylist,Zlist]
             
    return veclist


def readjson(filename):
    f = open(filename,"r")
    info = json.load(f)
    f.close()

    amino_dict = {} # {orgnism:amino}

    for i in info:
        amino_dict[i["GBSeq_organism"]] = i["GBSeq_sequence"]

    return amino_dict


def makevec(filename):

    amino_dict = readjson(filename)

    maxlen = 0

    for amino in amino_dict.values():
        maxlen = max(maxlen,len(amino))

    print(maxlen)

    for org,amino in amino_dict.items():
        if maxlen > len(amino):
            amino += amino[:(maxlen-len(amino))]
            amino_dict[org] = amino
            
    vecdict_list = [] # vecdict_list = [{orgnism:~,vec:[[x0,x1,x2...],[y0,y1,y2,...],[z0,z1,z2...]]},{},...]

    for key,val in amino_dict.items():
        dict1 = defaultdict()
        dict1["orgnism"] = key
        dict1["vec"] = za(val)
        vecdict_list.append(dict1)

    os.makedirs("./funcout", exist_ok = True)

    f = open("./funcout/vec.json","w")
    json.dump(vecdict_list,f,indent = 1,ensure_ascii=False)
    f.close()

