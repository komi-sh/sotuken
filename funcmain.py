from func import makevec
from func import pca
from func import dft
from func import cossim
from func import plot
import time

if __name__ == '__main__':

    time_sta = time.perf_counter()

    makevec.makevec("./NCBIDLout/dlxml.json")
    pca.pca("./funcout/vec.json")
    dft.dft("./funcout/pca_vec.json")
    cos,org = cossim.cossim("./funcout/dft.json")
    cossim.print_cos_sim(cos,org)
    cossim.write_cos_sim(cos,org)

    time_end = time.perf_counter()
    tim = time_end - time_sta

    print(tim)

    # plot.plot_pca("./funcout/pca_vec.json")
    # plot.plot_dft("./funcout/dft.json")
    # plot.plot_3dim("./funcout/vec.json")
