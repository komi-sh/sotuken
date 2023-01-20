import json
import numpy as np
import cmath
import math
from collections import defaultdict

def dft(pcapath):

    f = open(pcapath,"r")
    pcadict_list = json.load(f)
    f.close()
            
    dftdict_list = []
    n = len(pcadict_list[0]["vec"][0])

    for dic in pcadict_list: # [{orgnism:~,vec:[[x0,x1,x2,...],[y0,y1,y2,...]]},...]

        X = []
        Y = []
        buf = []
        
        for i in range(n-1):
            X.append(i) # X=[0,1,2,...,n-2] X=0はいらないためデータ数-1

        for i in range(n): #Yだけ型変換
            buf.append(complex(dic["vec"][1][i],0))

        for t in range(1,n): # t=0は平均のためいらない
            y = 0j
            for x in range(n):
                a = 2 * cmath.pi * t * x / n
                y += buf[x] * cmath.exp(-1j * a)
            Y.append(y)

        # パワースペクトル
        powlist = []
        for j in Y:
            powlist.append(np.abs(j))

        #X = X[0:math.ceil(n/2)] #　線対象のため要素を半分（2で割って切り上げ）にする
        powlist = powlist[0:math.ceil(n/2)] #　線対象のため要素を半分（2で割って切り上げ）にする
        #dftlist.append(X)

        dict1 = defaultdict()
        dict1["orgnism"] = dic["orgnism"]
        dict1["dft"] = powlist

        dftdict_list.append(dict1)

    f = open("./funcout/dft.json","w")
    json.dump(dftdict_list, f,indent = 1 ,ensure_ascii=False)
    f.close()

