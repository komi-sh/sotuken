import json
import numpy as np
import numpy.linalg as LA
from collections import defaultdict

def pca(vecpath):
    
    f = open(vecpath,"r")
    vec3dict_list = json.load(f)
    f.close()

    pca_info = [] # [{org:~,S:~,eig:~,vec:~},{org:~,S:~,eig:~,vec:~},...]

    for dic in vec3dict_list:
        dict1 = defaultdict()
        dict1["orgnism"] = dic["orgnism"]
        dict1["S"] = Variance_Covariance_Matrix(dic["vec"]) 
        wv = LA.eig(dict1["S"]) # 固有値と固有ベクトルをリストに格納　wv[0] = 固有値1,固有値2,固有値3 wv[1] =固有値に対応する固有ベクトル
        # print(f"{orglist[i]:-^50}\n 固有値\n{wv[0]}\n 固有ベクトル\n{wv[1]}\n")

        wv_r = eig_replace(wv) # 固有値の大きさによって固有ベクトル入れ替え 
        dict1["eig"] = wv_r[0].tolist() # numpy配列からlistへ変換
        dict1["vec"] = wv_r[1].tolist()
        # print(f"{orglist[i]:-^50}\n 固有値\n{wv[0]}\n 固有ベクトル\n{wv[1]}\n")

        pca_info.append(dict1)

    f = open("./funcout/pcadata.json","w")
    json.dump(pca_info, f,indent = 1 ,ensure_ascii=False)
    f.close()

    vec2dict_list = [] # [{orgnism:~,vec:[[x0,x1,x2,...],[y0,y1,y2,...]]},...]
    
    #固有ベクトル上に直交射影

    for l1,l2 in zip(vec3dict_list,pca_info):
        dict1 = defaultdict()
        dict1["orgnism"] = l1["orgnism"]
        dict1["vec"] = tyokko_projection(l1["vec"],l2["vec"])
        vec2dict_list.append(dict1)

    f = open("./funcout/pca_vec.json","w")
    json.dump(vec2dict_list, f,indent = 1 ,ensure_ascii=False)
    f.close()


def tyokko_projection(vec3_vec,eig_vec):
# vec3_vec = [[x0,x1,...],[y0,y1,...],[z0,z1,...]]
# eig_vec = [[x0,x1,x2],[y0,y1,y2],[z0,z1,z2]] 

    projection_list = []

    x = [] #pca後のx
    y = [] #pca後のy

    for i in range(len(vec3_vec[0])):
        x = np.append(x,eig_vec[0][0]*vec3_vec[0][i] + eig_vec[1][0]*vec3_vec[1][i] + eig_vec[2][0]*vec3_vec[2][i])
        y = np.append(y,eig_vec[0][1]*vec3_vec[0][i] + eig_vec[1][1]*vec3_vec[1][i] + eig_vec[2][1]*vec3_vec[2][i])
    x = x.tolist()    
    projection_list.append(x)
    y = y.tolist()
    projection_list.append(y)

    return projection_list


def Variance_Covariance_Matrix(Coordinate):

    Sxy = np.cov(Coordinate[0], Coordinate[1])
    Sxz = np.cov(Coordinate[0], Coordinate[2])
    Syz = np.cov(Coordinate[1], Coordinate[2])
    S = [[Sxy[0][0], Sxy[0][1], Sxz[0][1]],
        [Sxy[0][1], Sxy[1][1],  Syz[0][1]],
        [Sxz[0][1], Syz[0][1], Syz[1][1]]]
    
    return S


def eig_replace(wv):

    if (wv[0][0] > wv[0][1]) & (wv[0][0] > wv[0][2]):
        if wv[0][2] > wv[0][1]: # 固有値入れ替え
            buf = wv[0][1]
            wv[0][1] = wv[0][2]
            wv[0][2] = buf
            for j in range(3): # 固有ベクトル入れ替え
                buf = wv[1][j][1]
                wv[1][j][1] = wv[1][j][2]
                wv[1][j][2] = buf
    if (wv[0][1] > wv[0][0]) & (wv[0][1] > wv[0][2]):
        if wv[0][2] > wv[0][0]: # 固有値入れ替え
            buf = wv[0][0]
            wv[0][0] = wv[0][2]
            wv[0][2] = buf
            for j in range(3): # 固有ベクトル入れ替え
                buf = wv[1][j][0]
                wv[1][j][0] = wv[1][j][2]
                wv[1][j][2] = buf
    else:
        if wv[0][0] < wv[0][1]:
            buf = wv[0][0]
            wv[0][0] = wv[0][1]
            wv[0][1] = buf
            for j in range(3):
                buf = wv[1][j][0]
                wv[1][j][0] = wv[1][j][1]
                wv[1][j][1] = buf
    
    return wv
