import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import numpy as np


def plot_pca(pcapath):

    f = open(pcapath,"r")
    vec2dict_list = json.load(f)
    f.close()

    os.makedirs("./funcout/pca", exist_ok = True)

    colors = ["red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green"]
    count = 0

    for dic in vec2dict_list:
        fig = plt.figure()
        ax = fig.add_subplot(111,xlabel = "x",ylabel = "y")
        ax.plot(dic["vec"][0],dic["vec"][1], color=colors[count], label = dic["orgnism"])
        plt.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0, fontsize=12)
        ax.set_title("Principal Component Analysis")
        plt.savefig("./funcout/pca/" + dic["orgnism"] + ".jpg", bbox_inches="tight", pad_inches=0.05)
        plt.close()
        count += 1

def plot_dft(dftpath):

    f = open(dftpath,"r")
    vec2dict_list = json.load(f)
    f.close()

    os.makedirs("./funcout/dft", exist_ok = True)

    colors = ["red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green"]
    count = 0

    X_list = np.arange(1,len(vec2dict_list[0]["dft"])+1)

    for dic in vec2dict_list:
        fig = plt.figure()
        ax = fig.add_subplot(111,xlabel = "x",ylabel = "y")
        plt.yscale('log')
        ax.plot(X_list,dic["dft"], color=colors[count], label = dic["orgnism"])
        plt.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0, fontsize=12)
        ax.set_title("Discrete Fourier Transform")
        plt.savefig("./funcout/dft/" + dic["orgnism"] + ".jpg", bbox_inches="tight", pad_inches=0.05)
        plt.close()
        count += 1

def plot_3dim(vecpath):

    f = open(vecpath,"r")
    vec3dict_list = json.load(f)
    f.close()

    os.makedirs("./funcout/dim_3", exist_ok = True)

    colors = ["red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green","red","coral","gold","olive","cyan","blue","purple","magenta","green"]
    count = 0

    for dic in vec3dict_list:
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.plot(dic["vec"][0],dic["vec"][1],dic["vec"][2],color=colors[count], label = dic["orgnism"])
        plt.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0, fontsize=12)
        ax.set_title("3dim graph")
        plt.savefig("./funcout/dim_3/" + dic["orgnism"] + ".jpg", bbox_inches="tight", pad_inches=0.05)
        plt.close()
        count += 1
