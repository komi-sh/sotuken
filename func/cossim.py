import json
import numpy as np
import math
import numpy.linalg as LA#線形代数

def cossim(dftpath):

    f = open(dftpath,"r")
    dftdict_list = json.load(f)
    f.close()

    n = len(dftdict_list[0]["dft"])
    N = len(dftdict_list)
    normlist = []
    stalist = [[0 for i in range(n)] for j in range(N)]
    cos_simlist = np.zeros((N,N))

    for dic in dftdict_list:
        sum = 0
        for i in dic["dft"]:
            sum += i**2
        normlist.append(math.sqrt(sum))

    for i in range(N):
        for j in range(n):
            stalist[i][j] = dftdict_list[i]["dft"][j] / normlist[i]

    # for i in range(N):
    #     buf = 0
    #     for j in range(n):
    #        buf += stalist[i][j]**2
    #     print(buf) 
            
    for i in range(N):
        for j in range(N):
            if j < i:
                theta = np.dot(stalist[i],stalist[j])/(LA.norm(stalist[i])*LA.norm(stalist[j]))
                if theta > 1 : theta = 1
                cos_simlist[i][j] = np.arccos(theta)
                cos_simlist[j][i] = cos_simlist[i][j]

    orglist = []

    for dic in dftdict_list:
        orglist.append(dic["orgnism"])

    print(orglist)

    return cos_simlist,orglist


def print_cos_sim(coslist,orglist):
    print("\t",end = "")
    for i in orglist:
        print("{:.7s}".format(i),end = "\t")
    print("")
    for i in range(len(orglist)):
        print("{:.7s}".format(orglist[i]),end = "\t")
        for j in range(len(orglist)):
            if j < i:
                print("{:.5g}".format(coslist[i][j]),end = "\t")
        print("")


def write_cos_sim(coslist,orglist):

    N = len(orglist)
    trans_orglist = []

    for org in orglist:
        buf = []
        for s in org:
            if s == " ":
                buf = buf[0] + buf[1] + "."
            else:
                buf += s
        trans_orglist.append(buf)

    f = open("./funcout/cossim.txt", 'w')
    f.write('    ' + str(N) + '  ')
    for org in orglist:
        f.write(org)
        f.write('  ')
    f.write('\n')
    
    for i in range(N):
        a = trans_orglist[i].ljust(8)
        f.write(a[:8] + "  ")
        for j in range(N):
            f.write(str('{:.08f}'.format(coslist[i][j])))
            f.write('  ')
        f.write('\n')

    f.close()
