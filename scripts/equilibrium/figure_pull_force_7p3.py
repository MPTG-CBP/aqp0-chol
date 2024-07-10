import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  scipy.ndimage import gaussian_filter1d as filtro_gaussiano
from scipy.stats import sem as error_estandar
from scipy.optimize import curve_fit
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 3.5 #set the value globally

"""
slower_chol_1_x=pd.read_csv("slower/chol/1/pullx_format.xvg",header=None,sep="\t")
slower_chol_2_x=pd.read_csv("slower/chol/2/pullx_format.xvg",header=None,sep="\t")
slower_chol_3_x=pd.read_csv("slower/chol/3/pullx_format.xvg",header=None,sep="\t")
slower_chol_4_x=pd.read_csv("slower/chol/4/pullx_format.xvg",header=None,sep="\t")
slower_chol_5_x=pd.read_csv("slower/chol/5/pullx_format.xvg",header=None,sep="\t")
slower_chol_6_x=pd.read_csv("slower/chol/6/pullx_format.xvg",header=None,sep="\t")
slower_chol_7_x=pd.read_csv("slower/chol/7/pullx_format.xvg",header=None,sep="\t")
slower_chol_8_x=pd.read_csv("slower/chol/8/pullx_format.xvg",header=None,sep="\t")
slower_chol_9_x=pd.read_csv("slower/chol/9/pullx_format.xvg",header=None,sep="\t")
slower_chol_10_x=pd.read_csv("slower/chol/10/pullx_format.xvg",header=None,sep="\t")

print("paso")

slower_nochol_1_x=pd.read_csv("slower/no_chol/1/pullx_format.xvg",header=None,sep="\t")
slower_nochol_2_x=pd.read_csv("slower/no_chol/2/pullx_format.xvg",header=None,sep="\t")
slower_nochol_3_x=pd.read_csv("slower/no_chol/3/pullx_format.xvg",header=None,sep="\t")
slower_nochol_4_x=pd.read_csv("slower/no_chol/4/pullx_format.xvg",header=None,sep="\t")
slower_nochol_5_x=pd.read_csv("slower/no_chol/5/pullx_format.xvg",header=None,sep="\t")
slower_nochol_6_x=pd.read_csv("slower/no_chol/6/pullx_format.xvg",header=None,sep="\t")
slower_nochol_7_x=pd.read_csv("slower/no_chol/7/pullx_format.xvg",header=None,sep="\t")
slower_nochol_8_x=pd.read_csv("slower/no_chol/8/pullx_format.xvg",header=None,sep="\t")
slower_nochol_9_x=pd.read_csv("slower/no_chol/9/pullx_format.xvg",header=None,sep="\t")
slower_nochol_10_x=pd.read_csv("slower/no_chol/10/pullx_format.xvg",header=None,sep="\t")

print("paso")

slower_chol_1_f=pd.read_csv("slower/chol/1/pullf_format.xvg",header=None,sep="\t")
slower_chol_2_f=pd.read_csv("slower/chol/2/pullf_format.xvg",header=None,sep="\t")
slower_chol_3_f=pd.read_csv("slower/chol/3/pullf_format.xvg",header=None,sep="\t")
slower_chol_4_f=pd.read_csv("slower/chol/4/pullf_format.xvg",header=None,sep="\t")
slower_chol_5_f=pd.read_csv("slower/chol/5/pullf_format.xvg",header=None,sep="\t")
slower_chol_6_f=pd.read_csv("slower/chol/6/pullf_format.xvg",header=None,sep="\t")
slower_chol_7_f=pd.read_csv("slower/chol/7/pullf_format.xvg",header=None,sep="\t")
slower_chol_8_f=pd.read_csv("slower/chol/8/pullf_format.xvg",header=None,sep="\t")
slower_chol_9_f=pd.read_csv("slower/chol/9/pullf_format.xvg",header=None,sep="\t")
slower_chol_10_f=pd.read_csv("slower/chol/10/pullf_format.xvg",header=None,sep="\t")

print("paso")

slower_nochol_1_f=pd.read_csv("slower/no_chol/1/pullf_format.xvg",header=None,sep="\t")
slower_nochol_2_f=pd.read_csv("slower/no_chol/2/pullf_format.xvg",header=None,sep="\t")
slower_nochol_3_f=pd.read_csv("slower/no_chol/3/pullf_format.xvg",header=None,sep="\t")
slower_nochol_4_f=pd.read_csv("slower/no_chol/4/pullf_format.xvg",header=None,sep="\t")
slower_nochol_5_f=pd.read_csv("slower/no_chol/5/pullf_format.xvg",header=None,sep="\t")
slower_nochol_6_f=pd.read_csv("slower/no_chol/6/pullf_format.xvg",header=None,sep="\t")
slower_nochol_7_f=pd.read_csv("slower/no_chol/7/pullf_format.xvg",header=None,sep="\t")
slower_nochol_8_f=pd.read_csv("slower/no_chol/8/pullf_format.xvg",header=None,sep="\t")
slower_nochol_9_f=pd.read_csv("slower/no_chol/9/pullf_format.xvg",header=None,sep="\t")
slower_nochol_10_f=pd.read_csv("slower/no_chol/10/pullf_format.xvg",header=None,sep="\t")

print("paso")


slower_chol_11_x=pd.read_csv("slower/chol/11/pullx_format.xvg",header=None,sep="\t")
slower_chol_12_x=pd.read_csv("slower/chol/12/pullx_format.xvg",header=None,sep="\t")
slower_chol_13_x=pd.read_csv("slower/chol/13/pullx_format.xvg",header=None,sep="\t")
slower_chol_14_x=pd.read_csv("slower/chol/14/pullx_format.xvg",header=None,sep="\t")
slower_chol_15_x=pd.read_csv("slower/chol/15/pullx_format.xvg",header=None,sep="\t")
slower_chol_16_x=pd.read_csv("slower/chol/16/pullx_format.xvg",header=None,sep="\t")
slower_chol_17_x=pd.read_csv("slower/chol/17/pullx_format.xvg",header=None,sep="\t")
slower_chol_18_x=pd.read_csv("slower/chol/18/pullx_format.xvg",header=None,sep="\t")
slower_chol_19_x=pd.read_csv("slower/chol/19/pullx_format.xvg",header=None,sep="\t")
slower_chol_20_x=pd.read_csv("slower/chol/20/pullx_format.xvg",header=None,sep="\t")


slower_nochol_11_x=pd.read_csv("slower/no_chol/11/pullx_format.xvg",header=None,sep="\t")
slower_nochol_12_x=pd.read_csv("slower/no_chol/12/pullx_format.xvg",header=None,sep="\t")
slower_nochol_13_x=pd.read_csv("slower/no_chol/13/pullx_format.xvg",header=None,sep="\t")
slower_nochol_14_x=pd.read_csv("slower/no_chol/14/pullx_format.xvg",header=None,sep="\t")
slower_nochol_15_x=pd.read_csv("slower/no_chol/15/pullx_format.xvg",header=None,sep="\t")
slower_nochol_16_x=pd.read_csv("slower/no_chol/16/pullx_format.xvg",header=None,sep="\t")
slower_nochol_17_x=pd.read_csv("slower/no_chol/17/pullx_format.xvg",header=None,sep="\t")
slower_nochol_18_x=pd.read_csv("slower/no_chol/18/pullx_format.xvg",header=None,sep="\t")
slower_nochol_19_x=pd.read_csv("slower/no_chol/19/pullx_format.xvg",header=None,sep="\t")
slower_nochol_20_x=pd.read_csv("slower/no_chol/20/pullx_format.xvg",header=None,sep="\t")

slower_chol_11_f=pd.read_csv("slower/chol/11/pullf_format.xvg",header=None,sep="\t")
slower_chol_12_f=pd.read_csv("slower/chol/12/pullf_format.xvg",header=None,sep="\t")
slower_chol_13_f=pd.read_csv("slower/chol/13/pullf_format.xvg",header=None,sep="\t")
slower_chol_14_f=pd.read_csv("slower/chol/14/pullf_format.xvg",header=None,sep="\t")
slower_chol_15_f=pd.read_csv("slower/chol/15/pullf_format.xvg",header=None,sep="\t")
slower_chol_16_f=pd.read_csv("slower/chol/16/pullf_format.xvg",header=None,sep="\t")
slower_chol_17_f=pd.read_csv("slower/chol/17/pullf_format.xvg",header=None,sep="\t")
slower_chol_18_f=pd.read_csv("slower/chol/18/pullf_format.xvg",header=None,sep="\t")
slower_chol_19_f=pd.read_csv("slower/chol/19/pullf_format.xvg",header=None,sep="\t")
slower_chol_20_f=pd.read_csv("slower/chol/20/pullf_format.xvg",header=None,sep="\t")


slower_nochol_11_f=pd.read_csv("slower/no_chol/11/pullf_format.xvg",header=None,sep="\t")
slower_nochol_12_f=pd.read_csv("slower/no_chol/12/pullf_format.xvg",header=None,sep="\t")
slower_nochol_13_f=pd.read_csv("slower/no_chol/13/pullf_format.xvg",header=None,sep="\t")
slower_nochol_14_f=pd.read_csv("slower/no_chol/14/pullf_format.xvg",header=None,sep="\t")
slower_nochol_15_f=pd.read_csv("slower/no_chol/15/pullf_format.xvg",header=None,sep="\t")
slower_nochol_16_f=pd.read_csv("slower/no_chol/16/pullf_format.xvg",header=None,sep="\t")
slower_nochol_17_f=pd.read_csv("slower/no_chol/17/pullf_format.xvg",header=None,sep="\t")
slower_nochol_18_f=pd.read_csv("slower/no_chol/18/pullf_format.xvg",header=None,sep="\t")
slower_nochol_19_f=pd.read_csv("slower/no_chol/19/pullf_format.xvg",header=None,sep="\t")
slower_nochol_20_f=pd.read_csv("slower/no_chol/20/pullf_format.xvg",header=None,sep="\t")




slowest_chol_1_x=pd.read_csv("slowest/chol/1/pullx_format.xvg",header=None,sep="\t")
slowest_chol_2_x=pd.read_csv("slowest/chol/2/pullx_format.xvg",header=None,sep="\t")
slowest_chol_3_x=pd.read_csv("slowest/chol/3/pullx_format.xvg",header=None,sep="\t")
slowest_chol_4_x=pd.read_csv("slowest/chol/4/pullx_format.xvg",header=None,sep="\t")
slowest_chol_5_x=pd.read_csv("slowest/chol/5/pullx_format.xvg",header=None,sep="\t")
slowest_chol_6_x=pd.read_csv("slowest/chol/6/pullx_format.xvg",header=None,sep="\t")
slowest_chol_7_x=pd.read_csv("slowest/chol/7/pullx_format.xvg",header=None,sep="\t")
slowest_chol_8_x=pd.read_csv("slowest/chol/8/pullx_format.xvg",header=None,sep="\t")
slowest_chol_9_x=pd.read_csv("slowest/chol/9/pullx_format.xvg",header=None,sep="\t")
slowest_chol_10_x=pd.read_csv("slowest/chol/10/pullx_format.xvg",header=None,sep="\t")

print("paso")

slowest_nochol_1_x=pd.read_csv("slowest/no_chol/1/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_2_x=pd.read_csv("slowest/no_chol/2/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_3_x=pd.read_csv("slowest/no_chol/3/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_4_x=pd.read_csv("slowest/no_chol/4/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_5_x=pd.read_csv("slowest/no_chol/5/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_6_x=pd.read_csv("slowest/no_chol/6/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_7_x=pd.read_csv("slowest/no_chol/7/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_8_x=pd.read_csv("slowest/no_chol/8/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_9_x=pd.read_csv("slowest/no_chol/9/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_10_x=pd.read_csv("slowest/no_chol/10/pullx_format.xvg",header=None,sep="\t")

print("paso")

slowest_chol_1_f=pd.read_csv("slowest/chol/1/pullf_format.xvg",header=None,sep="\t")
slowest_chol_2_f=pd.read_csv("slowest/chol/2/pullf_format.xvg",header=None,sep="\t")
slowest_chol_3_f=pd.read_csv("slowest/chol/3/pullf_format.xvg",header=None,sep="\t")
slowest_chol_4_f=pd.read_csv("slowest/chol/4/pullf_format.xvg",header=None,sep="\t")
slowest_chol_5_f=pd.read_csv("slowest/chol/5/pullf_format.xvg",header=None,sep="\t")
slowest_chol_6_f=pd.read_csv("slowest/chol/6/pullf_format.xvg",header=None,sep="\t")
slowest_chol_7_f=pd.read_csv("slowest/chol/7/pullf_format.xvg",header=None,sep="\t")
slowest_chol_8_f=pd.read_csv("slowest/chol/8/pullf_format.xvg",header=None,sep="\t")
slowest_chol_9_f=pd.read_csv("slowest/chol/9/pullf_format.xvg",header=None,sep="\t")
slowest_chol_10_f=pd.read_csv("slowest/chol/10/pullf_format.xvg",header=None,sep="\t")

print("paso")

slowest_nochol_1_f=pd.read_csv("slowest/no_chol/1/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_2_f=pd.read_csv("slowest/no_chol/2/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_3_f=pd.read_csv("slowest/no_chol/3/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_4_f=pd.read_csv("slowest/no_chol/4/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_5_f=pd.read_csv("slowest/no_chol/5/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_6_f=pd.read_csv("slowest/no_chol/6/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_7_f=pd.read_csv("slowest/no_chol/7/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_8_f=pd.read_csv("slowest/no_chol/8/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_9_f=pd.read_csv("slowest/no_chol/9/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_10_f=pd.read_csv("slowest/no_chol/10/pullf_format.xvg",header=None,sep="\t")

print("paso")

slowest_chol_11_x=pd.read_csv("slowest/chol/11/pullx_format.xvg",header=None,sep="\t")
slowest_chol_12_x=pd.read_csv("slowest/chol/12/pullx_format.xvg",header=None,sep="\t")
slowest_chol_13_x=pd.read_csv("slowest/chol/13/pullx_format.xvg",header=None,sep="\t")
slowest_chol_14_x=pd.read_csv("slowest/chol/14/pullx_format.xvg",header=None,sep="\t")
slowest_chol_15_x=pd.read_csv("slowest/chol/15/pullx_format.xvg",header=None,sep="\t")
slowest_chol_16_x=pd.read_csv("slowest/chol/16/pullx_format.xvg",header=None,sep="\t")
slowest_chol_17_x=pd.read_csv("slowest/chol/17/pullx_format.xvg",header=None,sep="\t")
slowest_chol_18_x=pd.read_csv("slowest/chol/18/pullx_format.xvg",header=None,sep="\t")
slowest_chol_19_x=pd.read_csv("slowest/chol/19/pullx_format.xvg",header=None,sep="\t")
slowest_chol_20_x=pd.read_csv("slowest/chol/20/pullx_format.xvg",header=None,sep="\t")

slowest_nochol_11_x=pd.read_csv("slowest/no_chol/11/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_12_x=pd.read_csv("slowest/no_chol/12/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_13_x=pd.read_csv("slowest/no_chol/13/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_14_x=pd.read_csv("slowest/no_chol/14/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_15_x=pd.read_csv("slowest/no_chol/15/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_16_x=pd.read_csv("slowest/no_chol/16/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_17_x=pd.read_csv("slowest/no_chol/17/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_18_x=pd.read_csv("slowest/no_chol/18/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_19_x=pd.read_csv("slowest/no_chol/19/pullx_format.xvg",header=None,sep="\t")
slowest_nochol_20_x=pd.read_csv("slowest/no_chol/20/pullx_format.xvg",header=None,sep="\t")

slowest_chol_11_f=pd.read_csv("slowest/chol/11/pullf_format.xvg",header=None,sep="\t")
slowest_chol_12_f=pd.read_csv("slowest/chol/12/pullf_format.xvg",header=None,sep="\t")
slowest_chol_13_f=pd.read_csv("slowest/chol/13/pullf_format.xvg",header=None,sep="\t")
slowest_chol_14_f=pd.read_csv("slowest/chol/14/pullf_format.xvg",header=None,sep="\t")
slowest_chol_15_f=pd.read_csv("slowest/chol/15/pullf_format.xvg",header=None,sep="\t")
slowest_chol_16_f=pd.read_csv("slowest/chol/16/pullf_format.xvg",header=None,sep="\t")
slowest_chol_17_f=pd.read_csv("slowest/chol/17/pullf_format.xvg",header=None,sep="\t")
slowest_chol_18_f=pd.read_csv("slowest/chol/18/pullf_format.xvg",header=None,sep="\t")
slowest_chol_19_f=pd.read_csv("slowest/chol/19/pullf_format.xvg",header=None,sep="\t")
slowest_chol_20_f=pd.read_csv("slowest/chol/20/pullf_format.xvg",header=None,sep="\t")


slowest_nochol_11_f=pd.read_csv("slowest/no_chol/11/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_12_f=pd.read_csv("slowest/no_chol/12/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_13_f=pd.read_csv("slowest/no_chol/13/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_14_f=pd.read_csv("slowest/no_chol/14/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_15_f=pd.read_csv("slowest/no_chol/15/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_16_f=pd.read_csv("slowest/no_chol/16/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_17_f=pd.read_csv("slowest/no_chol/17/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_18_f=pd.read_csv("slowest/no_chol/18/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_19_f=pd.read_csv("slowest/no_chol/19/pullf_format.xvg",header=None,sep="\t")
slowest_nochol_20_f=pd.read_csv("slowest/no_chol/20/pullf_format.xvg",header=None,sep="\t")


glacial_chol_1_x=pd.read_csv("glacial/chol/1/pullx_format.xvg",header=None,sep="\t")
glacial_chol_2_x=pd.read_csv("glacial/chol/2/pullx_format.xvg",header=None,sep="\t")
glacial_chol_3_x=pd.read_csv("glacial/chol/3/pullx_format.xvg",header=None,sep="\t")
glacial_chol_4_x=pd.read_csv("glacial/chol/4/pullx_format.xvg",header=None,sep="\t")
glacial_chol_5_x=pd.read_csv("glacial/chol/5/pullx_format.xvg",header=None,sep="\t")
glacial_chol_6_x=pd.read_csv("glacial/chol/6/pullx_format.xvg",header=None,sep="\t")
glacial_chol_7_x=pd.read_csv("glacial/chol/7/pullx_format.xvg",header=None,sep="\t")
glacial_chol_8_x=pd.read_csv("glacial/chol/8/pullx_format.xvg",header=None,sep="\t")
glacial_chol_9_x=pd.read_csv("glacial/chol/9/pullx_format.xvg",header=None,sep="\t")
glacial_chol_10_x=pd.read_csv("glacial/chol/10/pullx_format.xvg",header=None,sep="\t")

print("paso")

glacial_nochol_1_x=pd.read_csv("glacial/no_chol/1/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_2_x=pd.read_csv("glacial/no_chol/2/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_3_x=pd.read_csv("glacial/no_chol/3/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_4_x=pd.read_csv("glacial/no_chol/4/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_5_x=pd.read_csv("glacial/no_chol/5/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_6_x=pd.read_csv("glacial/no_chol/6/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_7_x=pd.read_csv("glacial/no_chol/7/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_8_x=pd.read_csv("glacial/no_chol/8/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_9_x=pd.read_csv("glacial/no_chol/9/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_10_x=pd.read_csv("glacial/no_chol/10/pullx_format.xvg",header=None,sep="\t")

print("paso")


glacial_chol_1_f=pd.read_csv("glacial/chol/1/pullf_format.xvg",header=None,sep="\t")
glacial_chol_2_f=pd.read_csv("glacial/chol/2/pullf_format.xvg",header=None,sep="\t")
glacial_chol_3_f=pd.read_csv("glacial/chol/3/pullf_format.xvg",header=None,sep="\t")
glacial_chol_4_f=pd.read_csv("glacial/chol/4/pullf_format.xvg",header=None,sep="\t")
glacial_chol_5_f=pd.read_csv("glacial/chol/5/pullf_format.xvg",header=None,sep="\t")
glacial_chol_6_f=pd.read_csv("glacial/chol/6/pullf_format.xvg",header=None,sep="\t")
glacial_chol_7_f=pd.read_csv("glacial/chol/7/pullf_format.xvg",header=None,sep="\t")
glacial_chol_8_f=pd.read_csv("glacial/chol/8/pullf_format.xvg",header=None,sep="\t")
glacial_chol_9_f=pd.read_csv("glacial/chol/9/pullf_format.xvg",header=None,sep="\t")
glacial_chol_10_f=pd.read_csv("glacial/chol/10/pullf_format.xvg",header=None,sep="\t")


glacial_nochol_1_f=pd.read_csv("glacial/no_chol/1/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_2_f=pd.read_csv("glacial/no_chol/2/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_3_f=pd.read_csv("glacial/no_chol/3/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_4_f=pd.read_csv("glacial/no_chol/4/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_5_f=pd.read_csv("glacial/no_chol/5/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_6_f=pd.read_csv("glacial/no_chol/6/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_7_f=pd.read_csv("glacial/no_chol/7/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_8_f=pd.read_csv("glacial/no_chol/8/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_9_f=pd.read_csv("glacial/no_chol/9/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_10_f=pd.read_csv("glacial/no_chol/10/pullf_format.xvg",header=None,sep="\t")

glacial_chol_11_x=pd.read_csv("glacial/chol/11/pullx_format.xvg",header=None,sep="\t")
glacial_chol_12_x=pd.read_csv("glacial/chol/12/pullx_format.xvg",header=None,sep="\t")
glacial_chol_13_x=pd.read_csv("glacial/chol/13/pullx_format.xvg",header=None,sep="\t")
glacial_chol_14_x=pd.read_csv("glacial/chol/14/pullx_format.xvg",header=None,sep="\t")
glacial_chol_15_x=pd.read_csv("glacial/chol/15/pullx_format.xvg",header=None,sep="\t")
glacial_chol_16_x=pd.read_csv("glacial/chol/16/pullx_format.xvg",header=None,sep="\t")
glacial_chol_17_x=pd.read_csv("glacial/chol/17/pullx_format.xvg",header=None,sep="\t")
glacial_chol_18_x=pd.read_csv("glacial/chol/18/pullx_format.xvg",header=None,sep="\t")
glacial_chol_19_x=pd.read_csv("glacial/chol/19/pullx_format.xvg",header=None,sep="\t")
glacial_chol_20_x=pd.read_csv("glacial/chol/20/pullx_format.xvg",header=None,sep="\t")


glacial_nochol_11_x=pd.read_csv("glacial/no_chol/11/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_12_x=pd.read_csv("glacial/no_chol/12/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_13_x=pd.read_csv("glacial/no_chol/13/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_14_x=pd.read_csv("glacial/no_chol/14/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_15_x=pd.read_csv("glacial/no_chol/15/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_16_x=pd.read_csv("glacial/no_chol/16/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_17_x=pd.read_csv("glacial/no_chol/17/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_18_x=pd.read_csv("glacial/no_chol/18/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_19_x=pd.read_csv("glacial/no_chol/19/pullx_format.xvg",header=None,sep="\t")
glacial_nochol_20_x=pd.read_csv("glacial/no_chol/20/pullx_format.xvg",header=None,sep="\t")

glacial_chol_11_f=pd.read_csv("glacial/chol/11/pullf_format.xvg",header=None,sep="\t")
glacial_chol_12_f=pd.read_csv("glacial/chol/12/pullf_format.xvg",header=None,sep="\t")
glacial_chol_13_f=pd.read_csv("glacial/chol/13/pullf_format.xvg",header=None,sep="\t")
glacial_chol_14_f=pd.read_csv("glacial/chol/14/pullf_format.xvg",header=None,sep="\t")
glacial_chol_15_f=pd.read_csv("glacial/chol/15/pullf_format.xvg",header=None,sep="\t")
glacial_chol_16_f=pd.read_csv("glacial/chol/16/pullf_format.xvg",header=None,sep="\t")
glacial_chol_17_f=pd.read_csv("glacial/chol/17/pullf_format.xvg",header=None,sep="\t")
glacial_chol_18_f=pd.read_csv("glacial/chol/18/pullf_format.xvg",header=None,sep="\t")
glacial_chol_19_f=pd.read_csv("glacial/chol/19/pullf_format.xvg",header=None,sep="\t")
glacial_chol_20_f=pd.read_csv("glacial/chol/20/pullf_format.xvg",header=None,sep="\t")


glacial_nochol_11_f=pd.read_csv("glacial/no_chol/11/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_12_f=pd.read_csv("glacial/no_chol/12/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_13_f=pd.read_csv("glacial/no_chol/13/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_14_f=pd.read_csv("glacial/no_chol/14/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_15_f=pd.read_csv("glacial/no_chol/15/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_16_f=pd.read_csv("glacial/no_chol/16/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_17_f=pd.read_csv("glacial/no_chol/17/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_18_f=pd.read_csv("glacial/no_chol/18/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_19_f=pd.read_csv("glacial/no_chol/19/pullf_format.xvg",header=None,sep="\t")
glacial_nochol_20_f=pd.read_csv("glacial/no_chol/20/pullf_format.xvg",header=None,sep="\t")

"""
ancho=1000

"""
filtered_slower_chol_1_x=filtro_gaussiano(slower_chol_1_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_2_x=filtro_gaussiano(slower_chol_2_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_3_x=filtro_gaussiano(slower_chol_3_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_4_x=filtro_gaussiano(slower_chol_4_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_5_x=filtro_gaussiano(slower_chol_5_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_6_x=filtro_gaussiano(slower_chol_6_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_7_x=filtro_gaussiano(slower_chol_7_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_8_x=filtro_gaussiano(slower_chol_8_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_9_x=filtro_gaussiano(slower_chol_9_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_10_x=filtro_gaussiano(slower_chol_10_x.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_slower_nochol_1_x=filtro_gaussiano(slower_nochol_1_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_2_x=filtro_gaussiano(slower_nochol_2_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_3_x=filtro_gaussiano(slower_nochol_3_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_4_x=filtro_gaussiano(slower_nochol_4_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_5_x=filtro_gaussiano(slower_nochol_5_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_6_x=filtro_gaussiano(slower_nochol_6_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_7_x=filtro_gaussiano(slower_nochol_7_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_8_x=filtro_gaussiano(slower_nochol_8_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_9_x=filtro_gaussiano(slower_nochol_9_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_10_x=filtro_gaussiano(slower_nochol_10_x.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_slower_chol_1_f=filtro_gaussiano(slower_chol_1_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_2_f=filtro_gaussiano(slower_chol_2_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_3_f=filtro_gaussiano(slower_chol_3_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_4_f=filtro_gaussiano(slower_chol_4_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_5_f=filtro_gaussiano(slower_chol_5_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_6_f=filtro_gaussiano(slower_chol_6_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_7_f=filtro_gaussiano(slower_chol_7_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_8_f=filtro_gaussiano(slower_chol_8_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_9_f=filtro_gaussiano(slower_chol_9_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_10_f=filtro_gaussiano(slower_chol_10_f.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_slower_nochol_1_f=filtro_gaussiano(slower_nochol_1_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_2_f=filtro_gaussiano(slower_nochol_2_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_3_f=filtro_gaussiano(slower_nochol_3_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_4_f=filtro_gaussiano(slower_nochol_4_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_5_f=filtro_gaussiano(slower_nochol_5_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_6_f=filtro_gaussiano(slower_nochol_6_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_7_f=filtro_gaussiano(slower_nochol_7_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_8_f=filtro_gaussiano(slower_nochol_8_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_9_f=filtro_gaussiano(slower_nochol_9_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_10_f=filtro_gaussiano(slower_nochol_10_f.iloc[:,1],sigma=ancho,order=0)

print("paso")


filtered_slower_chol_11_x=filtro_gaussiano(slower_chol_11_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_12_x=filtro_gaussiano(slower_chol_12_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_13_x=filtro_gaussiano(slower_chol_13_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_14_x=filtro_gaussiano(slower_chol_14_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_15_x=filtro_gaussiano(slower_chol_15_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_16_x=filtro_gaussiano(slower_chol_16_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_17_x=filtro_gaussiano(slower_chol_17_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_18_x=filtro_gaussiano(slower_chol_18_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_19_x=filtro_gaussiano(slower_chol_19_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_20_x=filtro_gaussiano(slower_chol_20_x.iloc[:,1],sigma=ancho,order=0)

filtered_slower_nochol_11_x=filtro_gaussiano(slower_nochol_11_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_12_x=filtro_gaussiano(slower_nochol_12_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_13_x=filtro_gaussiano(slower_nochol_13_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_14_x=filtro_gaussiano(slower_nochol_14_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_15_x=filtro_gaussiano(slower_nochol_15_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_16_x=filtro_gaussiano(slower_nochol_16_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_17_x=filtro_gaussiano(slower_nochol_17_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_18_x=filtro_gaussiano(slower_nochol_18_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_19_x=filtro_gaussiano(slower_nochol_19_x.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_20_x=filtro_gaussiano(slower_nochol_20_x.iloc[:,1],sigma=ancho,order=0)

filtered_slower_chol_11_f=filtro_gaussiano(slower_chol_11_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_12_f=filtro_gaussiano(slower_chol_12_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_13_f=filtro_gaussiano(slower_chol_13_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_14_f=filtro_gaussiano(slower_chol_14_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_15_f=filtro_gaussiano(slower_chol_15_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_16_f=filtro_gaussiano(slower_chol_16_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_17_f=filtro_gaussiano(slower_chol_17_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_18_f=filtro_gaussiano(slower_chol_18_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_19_f=filtro_gaussiano(slower_chol_19_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_chol_20_f=filtro_gaussiano(slower_chol_20_f.iloc[:,1],sigma=ancho,order=0)

filtered_slower_nochol_11_f=filtro_gaussiano(slower_nochol_11_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_12_f=filtro_gaussiano(slower_nochol_12_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_13_f=filtro_gaussiano(slower_nochol_13_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_14_f=filtro_gaussiano(slower_nochol_14_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_15_f=filtro_gaussiano(slower_nochol_15_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_16_f=filtro_gaussiano(slower_nochol_16_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_17_f=filtro_gaussiano(slower_nochol_17_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_18_f=filtro_gaussiano(slower_nochol_18_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_19_f=filtro_gaussiano(slower_nochol_19_f.iloc[:,1],sigma=ancho,order=0)
filtered_slower_nochol_20_f=filtro_gaussiano(slower_nochol_20_f.iloc[:,1],sigma=ancho,order=0)


filtered_slowest_chol_1_x=filtro_gaussiano(slowest_chol_1_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_2_x=filtro_gaussiano(slowest_chol_2_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_3_x=filtro_gaussiano(slowest_chol_3_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_4_x=filtro_gaussiano(slowest_chol_4_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_5_x=filtro_gaussiano(slowest_chol_5_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_6_x=filtro_gaussiano(slowest_chol_6_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_7_x=filtro_gaussiano(slowest_chol_7_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_8_x=filtro_gaussiano(slowest_chol_8_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_9_x=filtro_gaussiano(slowest_chol_9_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_10_x=filtro_gaussiano(slowest_chol_10_x.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_slowest_nochol_1_x=filtro_gaussiano(slowest_nochol_1_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_2_x=filtro_gaussiano(slowest_nochol_2_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_3_x=filtro_gaussiano(slowest_nochol_3_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_4_x=filtro_gaussiano(slowest_nochol_4_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_5_x=filtro_gaussiano(slowest_nochol_5_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_6_x=filtro_gaussiano(slowest_nochol_6_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_7_x=filtro_gaussiano(slowest_nochol_7_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_8_x=filtro_gaussiano(slowest_nochol_8_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_9_x=filtro_gaussiano(slowest_nochol_9_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_10_x=filtro_gaussiano(slowest_nochol_10_x.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_slowest_chol_1_f=filtro_gaussiano(slowest_chol_1_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_2_f=filtro_gaussiano(slowest_chol_2_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_3_f=filtro_gaussiano(slowest_chol_3_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_4_f=filtro_gaussiano(slowest_chol_4_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_5_f=filtro_gaussiano(slowest_chol_5_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_6_f=filtro_gaussiano(slowest_chol_6_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_7_f=filtro_gaussiano(slowest_chol_7_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_8_f=filtro_gaussiano(slowest_chol_8_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_9_f=filtro_gaussiano(slowest_chol_9_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_10_f=filtro_gaussiano(slowest_chol_10_f.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_slowest_nochol_1_f=filtro_gaussiano(slowest_nochol_1_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_2_f=filtro_gaussiano(slowest_nochol_2_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_3_f=filtro_gaussiano(slowest_nochol_3_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_4_f=filtro_gaussiano(slowest_nochol_4_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_5_f=filtro_gaussiano(slowest_nochol_5_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_6_f=filtro_gaussiano(slowest_nochol_6_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_7_f=filtro_gaussiano(slowest_nochol_7_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_8_f=filtro_gaussiano(slowest_nochol_8_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_9_f=filtro_gaussiano(slowest_nochol_9_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_10_f=filtro_gaussiano(slowest_nochol_10_f.iloc[:,1],sigma=ancho,order=0)

print("paso")


filtered_slowest_chol_11_x=filtro_gaussiano(slowest_chol_11_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_12_x=filtro_gaussiano(slowest_chol_12_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_13_x=filtro_gaussiano(slowest_chol_13_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_14_x=filtro_gaussiano(slowest_chol_14_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_15_x=filtro_gaussiano(slowest_chol_15_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_16_x=filtro_gaussiano(slowest_chol_16_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_17_x=filtro_gaussiano(slowest_chol_17_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_18_x=filtro_gaussiano(slowest_chol_18_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_19_x=filtro_gaussiano(slowest_chol_19_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_20_x=filtro_gaussiano(slowest_chol_20_x.iloc[:,1],sigma=ancho,order=0)

filtered_slowest_nochol_11_x=filtro_gaussiano(slowest_nochol_11_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_12_x=filtro_gaussiano(slowest_nochol_12_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_13_x=filtro_gaussiano(slowest_nochol_13_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_14_x=filtro_gaussiano(slowest_nochol_14_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_15_x=filtro_gaussiano(slowest_nochol_15_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_16_x=filtro_gaussiano(slowest_nochol_16_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_17_x=filtro_gaussiano(slowest_nochol_17_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_18_x=filtro_gaussiano(slowest_nochol_18_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_19_x=filtro_gaussiano(slowest_nochol_19_x.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_20_x=filtro_gaussiano(slowest_nochol_20_x.iloc[:,1],sigma=ancho,order=0)

filtered_slowest_chol_11_f=filtro_gaussiano(slowest_chol_11_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_12_f=filtro_gaussiano(slowest_chol_12_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_13_f=filtro_gaussiano(slowest_chol_13_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_14_f=filtro_gaussiano(slowest_chol_14_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_15_f=filtro_gaussiano(slowest_chol_15_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_16_f=filtro_gaussiano(slowest_chol_16_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_17_f=filtro_gaussiano(slowest_chol_17_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_18_f=filtro_gaussiano(slowest_chol_18_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_19_f=filtro_gaussiano(slowest_chol_19_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_chol_20_f=filtro_gaussiano(slowest_chol_20_f.iloc[:,1],sigma=ancho,order=0)

filtered_slowest_nochol_11_f=filtro_gaussiano(slowest_nochol_11_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_12_f=filtro_gaussiano(slowest_nochol_12_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_13_f=filtro_gaussiano(slowest_nochol_13_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_14_f=filtro_gaussiano(slowest_nochol_14_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_15_f=filtro_gaussiano(slowest_nochol_15_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_16_f=filtro_gaussiano(slowest_nochol_16_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_17_f=filtro_gaussiano(slowest_nochol_17_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_18_f=filtro_gaussiano(slowest_nochol_18_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_19_f=filtro_gaussiano(slowest_nochol_19_f.iloc[:,1],sigma=ancho,order=0)
filtered_slowest_nochol_20_f=filtro_gaussiano(slowest_nochol_20_f.iloc[:,1],sigma=ancho,order=0)


filtered_glacial_chol_1_x=filtro_gaussiano(glacial_chol_1_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_2_x=filtro_gaussiano(glacial_chol_2_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_3_x=filtro_gaussiano(glacial_chol_3_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_4_x=filtro_gaussiano(glacial_chol_4_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_5_x=filtro_gaussiano(glacial_chol_5_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_6_x=filtro_gaussiano(glacial_chol_6_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_7_x=filtro_gaussiano(glacial_chol_7_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_8_x=filtro_gaussiano(glacial_chol_8_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_9_x=filtro_gaussiano(glacial_chol_9_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_10_x=filtro_gaussiano(glacial_chol_10_x.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_glacial_nochol_1_x=filtro_gaussiano(glacial_nochol_1_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_2_x=filtro_gaussiano(glacial_nochol_2_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_3_x=filtro_gaussiano(glacial_nochol_3_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_4_x=filtro_gaussiano(glacial_nochol_4_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_5_x=filtro_gaussiano(glacial_nochol_5_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_6_x=filtro_gaussiano(glacial_nochol_6_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_7_x=filtro_gaussiano(glacial_nochol_7_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_8_x=filtro_gaussiano(glacial_nochol_8_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_9_x=filtro_gaussiano(glacial_nochol_9_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_10_x=filtro_gaussiano(glacial_nochol_10_x.iloc[:,1],sigma=ancho,order=0)

print("paso")

filtered_glacial_chol_1_f=filtro_gaussiano(glacial_chol_1_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_2_f=filtro_gaussiano(glacial_chol_2_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_3_f=filtro_gaussiano(glacial_chol_3_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_4_f=filtro_gaussiano(glacial_chol_4_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_5_f=filtro_gaussiano(glacial_chol_5_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_6_f=filtro_gaussiano(glacial_chol_6_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_7_f=filtro_gaussiano(glacial_chol_7_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_8_f=filtro_gaussiano(glacial_chol_8_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_9_f=filtro_gaussiano(glacial_chol_9_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_10_f=filtro_gaussiano(glacial_chol_10_f.iloc[:,1],sigma=ancho,order=0)

filtered_glacial_nochol_1_f=filtro_gaussiano(glacial_nochol_1_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_2_f=filtro_gaussiano(glacial_nochol_2_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_3_f=filtro_gaussiano(glacial_nochol_3_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_4_f=filtro_gaussiano(glacial_nochol_4_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_5_f=filtro_gaussiano(glacial_nochol_5_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_6_f=filtro_gaussiano(glacial_nochol_6_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_7_f=filtro_gaussiano(glacial_nochol_7_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_8_f=filtro_gaussiano(glacial_nochol_8_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_9_f=filtro_gaussiano(glacial_nochol_9_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_10_f=filtro_gaussiano(glacial_nochol_10_f.iloc[:,1],sigma=ancho,order=0)

filtered_glacial_chol_11_x=filtro_gaussiano(glacial_chol_11_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_12_x=filtro_gaussiano(glacial_chol_12_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_13_x=filtro_gaussiano(glacial_chol_13_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_14_x=filtro_gaussiano(glacial_chol_14_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_15_x=filtro_gaussiano(glacial_chol_15_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_16_x=filtro_gaussiano(glacial_chol_16_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_17_x=filtro_gaussiano(glacial_chol_17_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_18_x=filtro_gaussiano(glacial_chol_18_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_19_x=filtro_gaussiano(glacial_chol_19_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_20_x=filtro_gaussiano(glacial_chol_20_x.iloc[:,1],sigma=ancho,order=0)

filtered_glacial_nochol_11_x=filtro_gaussiano(glacial_nochol_11_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_12_x=filtro_gaussiano(glacial_nochol_12_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_13_x=filtro_gaussiano(glacial_nochol_13_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_14_x=filtro_gaussiano(glacial_nochol_14_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_15_x=filtro_gaussiano(glacial_nochol_15_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_16_x=filtro_gaussiano(glacial_nochol_16_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_17_x=filtro_gaussiano(glacial_nochol_17_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_18_x=filtro_gaussiano(glacial_nochol_18_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_19_x=filtro_gaussiano(glacial_nochol_19_x.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_20_x=filtro_gaussiano(glacial_nochol_20_x.iloc[:,1],sigma=ancho,order=0)

filtered_glacial_chol_11_f=filtro_gaussiano(glacial_chol_11_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_12_f=filtro_gaussiano(glacial_chol_12_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_13_f=filtro_gaussiano(glacial_chol_13_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_14_f=filtro_gaussiano(glacial_chol_14_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_15_f=filtro_gaussiano(glacial_chol_15_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_16_f=filtro_gaussiano(glacial_chol_16_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_17_f=filtro_gaussiano(glacial_chol_17_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_18_f=filtro_gaussiano(glacial_chol_18_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_19_f=filtro_gaussiano(glacial_chol_19_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_chol_20_f=filtro_gaussiano(glacial_chol_20_f.iloc[:,1],sigma=ancho,order=0)

filtered_glacial_nochol_11_f=filtro_gaussiano(glacial_nochol_11_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_12_f=filtro_gaussiano(glacial_nochol_12_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_13_f=filtro_gaussiano(glacial_nochol_13_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_14_f=filtro_gaussiano(glacial_nochol_14_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_15_f=filtro_gaussiano(glacial_nochol_15_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_16_f=filtro_gaussiano(glacial_nochol_16_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_17_f=filtro_gaussiano(glacial_nochol_17_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_18_f=filtro_gaussiano(glacial_nochol_18_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_19_f=filtro_gaussiano(glacial_nochol_19_f.iloc[:,1],sigma=ancho,order=0)
filtered_glacial_nochol_20_f=filtro_gaussiano(glacial_nochol_20_f.iloc[:,1],sigma=ancho,order=0)


np.savetxt('filtered/short_filter_slower_chol_1_x.txt',filtered_slower_chol_1_x)
np.savetxt('filtered/short_filter_slower_chol_2_x.txt',filtered_slower_chol_2_x)
np.savetxt('filtered/short_filter_slower_chol_3_x.txt',filtered_slower_chol_3_x)
np.savetxt('filtered/short_filter_slower_chol_4_x.txt',filtered_slower_chol_4_x)
np.savetxt('filtered/short_filter_slower_chol_5_x.txt',filtered_slower_chol_5_x)
np.savetxt('filtered/short_filter_slower_chol_6_x.txt',filtered_slower_chol_6_x)
np.savetxt('filtered/short_filter_slower_chol_7_x.txt',filtered_slower_chol_7_x)
np.savetxt('filtered/short_filter_slower_chol_8_x.txt',filtered_slower_chol_8_x)
np.savetxt('filtered/short_filter_slower_chol_9_x.txt',filtered_slower_chol_9_x)
np.savetxt('filtered/short_filter_slower_chol_10_x.txt',filtered_slower_chol_10_x)

np.savetxt('filtered/short_filter_slower_nochol_1_x.txt',filtered_slower_nochol_1_x)
np.savetxt('filtered/short_filter_slower_nochol_2_x.txt',filtered_slower_nochol_2_x)
np.savetxt('filtered/short_filter_slower_nochol_3_x.txt',filtered_slower_nochol_3_x)
np.savetxt('filtered/short_filter_slower_nochol_4_x.txt',filtered_slower_nochol_4_x)
np.savetxt('filtered/short_filter_slower_nochol_5_x.txt',filtered_slower_nochol_5_x)
np.savetxt('filtered/short_filter_slower_nochol_6_x.txt',filtered_slower_nochol_6_x)
np.savetxt('filtered/short_filter_slower_nochol_7_x.txt',filtered_slower_nochol_7_x)
np.savetxt('filtered/short_filter_slower_nochol_8_x.txt',filtered_slower_nochol_8_x)
np.savetxt('filtered/short_filter_slower_nochol_9_x.txt',filtered_slower_nochol_9_x)
np.savetxt('filtered/short_filter_slower_nochol_10_x.txt',filtered_slower_nochol_10_x)

np.savetxt('filtered/short_filter_slower_chol_1_f.txt',filtered_slower_chol_1_f)
np.savetxt('filtered/short_filter_slower_chol_2_f.txt',filtered_slower_chol_2_f)
np.savetxt('filtered/short_filter_slower_chol_3_f.txt',filtered_slower_chol_3_f)
np.savetxt('filtered/short_filter_slower_chol_4_f.txt',filtered_slower_chol_4_f)
np.savetxt('filtered/short_filter_slower_chol_5_f.txt',filtered_slower_chol_5_f)
np.savetxt('filtered/short_filter_slower_chol_6_f.txt',filtered_slower_chol_6_f)
np.savetxt('filtered/short_filter_slower_chol_7_f.txt',filtered_slower_chol_7_f)
np.savetxt('filtered/short_filter_slower_chol_8_f.txt',filtered_slower_chol_8_f)
np.savetxt('filtered/short_filter_slower_chol_9_f.txt',filtered_slower_chol_9_f)
np.savetxt('filtered/short_filter_slower_chol_10_f.txt',filtered_slower_chol_10_f)

np.savetxt('filtered/short_filter_slower_nochol_1_f.txt',filtered_slower_nochol_1_f)
np.savetxt('filtered/short_filter_slower_nochol_2_f.txt',filtered_slower_nochol_2_f)
np.savetxt('filtered/short_filter_slower_nochol_3_f.txt',filtered_slower_nochol_3_f)
np.savetxt('filtered/short_filter_slower_nochol_4_f.txt',filtered_slower_nochol_4_f)
np.savetxt('filtered/short_filter_slower_nochol_5_f.txt',filtered_slower_nochol_5_f)
np.savetxt('filtered/short_filter_slower_nochol_6_f.txt',filtered_slower_nochol_6_f)
np.savetxt('filtered/short_filter_slower_nochol_7_f.txt',filtered_slower_nochol_7_f)
np.savetxt('filtered/short_filter_slower_nochol_8_f.txt',filtered_slower_nochol_8_f)
np.savetxt('filtered/short_filter_slower_nochol_9_f.txt',filtered_slower_nochol_9_f)
np.savetxt('filtered/short_filter_slower_nochol_10_f.txt',filtered_slower_nochol_10_f)



np.savetxt('filtered/short_filter_slowest_chol_1_x.txt',filtered_slowest_chol_1_x)
np.savetxt('filtered/short_filter_slowest_chol_2_x.txt',filtered_slowest_chol_2_x)
np.savetxt('filtered/short_filter_slowest_chol_3_x.txt',filtered_slowest_chol_3_x)
np.savetxt('filtered/short_filter_slowest_chol_4_x.txt',filtered_slowest_chol_4_x)
np.savetxt('filtered/short_filter_slowest_chol_5_x.txt',filtered_slowest_chol_5_x)
np.savetxt('filtered/short_filter_slowest_chol_6_x.txt',filtered_slowest_chol_6_x)
np.savetxt('filtered/short_filter_slowest_chol_7_x.txt',filtered_slowest_chol_7_x)
np.savetxt('filtered/short_filter_slowest_chol_8_x.txt',filtered_slowest_chol_8_x)
np.savetxt('filtered/short_filter_slowest_chol_9_x.txt',filtered_slowest_chol_9_x)
np.savetxt('filtered/short_filter_slowest_chol_10_x.txt',filtered_slowest_chol_10_x)

np.savetxt('filtered/short_filter_slowest_nochol_1_x.txt',filtered_slowest_nochol_1_x)
np.savetxt('filtered/short_filter_slowest_nochol_2_x.txt',filtered_slowest_nochol_2_x)
np.savetxt('filtered/short_filter_slowest_nochol_3_x.txt',filtered_slowest_nochol_3_x)
np.savetxt('filtered/short_filter_slowest_nochol_4_x.txt',filtered_slowest_nochol_4_x)
np.savetxt('filtered/short_filter_slowest_nochol_5_x.txt',filtered_slowest_nochol_5_x)
np.savetxt('filtered/short_filter_slowest_nochol_6_x.txt',filtered_slowest_nochol_6_x)
np.savetxt('filtered/short_filter_slowest_nochol_7_x.txt',filtered_slowest_nochol_7_x)
np.savetxt('filtered/short_filter_slowest_nochol_8_x.txt',filtered_slowest_nochol_8_x)
np.savetxt('filtered/short_filter_slowest_nochol_9_x.txt',filtered_slowest_nochol_9_x)
np.savetxt('filtered/short_filter_slowest_nochol_10_x.txt',filtered_slowest_nochol_10_x)

np.savetxt('filtered/short_filter_slowest_chol_1_f.txt',filtered_slowest_chol_1_f)
np.savetxt('filtered/short_filter_slowest_chol_2_f.txt',filtered_slowest_chol_2_f)
np.savetxt('filtered/short_filter_slowest_chol_3_f.txt',filtered_slowest_chol_3_f)
np.savetxt('filtered/short_filter_slowest_chol_4_f.txt',filtered_slowest_chol_4_f)
np.savetxt('filtered/short_filter_slowest_chol_5_f.txt',filtered_slowest_chol_5_f)
np.savetxt('filtered/short_filter_slowest_chol_6_f.txt',filtered_slowest_chol_6_f)
np.savetxt('filtered/short_filter_slowest_chol_7_f.txt',filtered_slowest_chol_7_f)
np.savetxt('filtered/short_filter_slowest_chol_8_f.txt',filtered_slowest_chol_8_f)
np.savetxt('filtered/short_filter_slowest_chol_9_f.txt',filtered_slowest_chol_9_f)
np.savetxt('filtered/short_filter_slowest_chol_10_f.txt',filtered_slowest_chol_10_f)

np.savetxt('filtered/short_filter_slowest_nochol_1_f.txt',filtered_slowest_nochol_1_f)
np.savetxt('filtered/short_filter_slowest_nochol_2_f.txt',filtered_slowest_nochol_2_f)
np.savetxt('filtered/short_filter_slowest_nochol_3_f.txt',filtered_slowest_nochol_3_f)
np.savetxt('filtered/short_filter_slowest_nochol_4_f.txt',filtered_slowest_nochol_4_f)
np.savetxt('filtered/short_filter_slowest_nochol_5_f.txt',filtered_slowest_nochol_5_f)
np.savetxt('filtered/short_filter_slowest_nochol_6_f.txt',filtered_slowest_nochol_6_f)
np.savetxt('filtered/short_filter_slowest_nochol_7_f.txt',filtered_slowest_nochol_7_f)
np.savetxt('filtered/short_filter_slowest_nochol_8_f.txt',filtered_slowest_nochol_8_f)
np.savetxt('filtered/short_filter_slowest_nochol_9_f.txt',filtered_slowest_nochol_9_f)
np.savetxt('filtered/short_filter_slowest_nochol_10_f.txt',filtered_slowest_nochol_10_f)


np.savetxt('filtered/short_filter_glacial_chol_1_x.txt',filtered_glacial_chol_1_x)
np.savetxt('filtered/short_filter_glacial_chol_2_x.txt',filtered_glacial_chol_2_x)
np.savetxt('filtered/short_filter_glacial_chol_3_x.txt',filtered_glacial_chol_3_x)
np.savetxt('filtered/short_filter_glacial_chol_4_x.txt',filtered_glacial_chol_4_x)
np.savetxt('filtered/short_filter_glacial_chol_5_x.txt',filtered_glacial_chol_5_x)
np.savetxt('filtered/short_filter_glacial_chol_6_x.txt',filtered_glacial_chol_6_x)
np.savetxt('filtered/short_filter_glacial_chol_7_x.txt',filtered_glacial_chol_7_x)
np.savetxt('filtered/short_filter_glacial_chol_8_x.txt',filtered_glacial_chol_8_x)
np.savetxt('filtered/short_filter_glacial_chol_9_x.txt',filtered_glacial_chol_9_x)
np.savetxt('filtered/short_filter_glacial_chol_10_x.txt',filtered_glacial_chol_10_x)

np.savetxt('filtered/short_filter_glacial_nochol_1_x.txt',filtered_glacial_nochol_1_x)
np.savetxt('filtered/short_filter_glacial_nochol_2_x.txt',filtered_glacial_nochol_2_x)
np.savetxt('filtered/short_filter_glacial_nochol_3_x.txt',filtered_glacial_nochol_3_x)
np.savetxt('filtered/short_filter_glacial_nochol_4_x.txt',filtered_glacial_nochol_4_x)
np.savetxt('filtered/short_filter_glacial_nochol_5_x.txt',filtered_glacial_nochol_5_x)
np.savetxt('filtered/short_filter_glacial_nochol_6_x.txt',filtered_glacial_nochol_6_x)
np.savetxt('filtered/short_filter_glacial_nochol_7_x.txt',filtered_glacial_nochol_7_x)
np.savetxt('filtered/short_filter_glacial_nochol_8_x.txt',filtered_glacial_nochol_8_x)
np.savetxt('filtered/short_filter_glacial_nochol_9_x.txt',filtered_glacial_nochol_9_x)
np.savetxt('filtered/short_filter_glacial_nochol_10_x.txt',filtered_glacial_nochol_10_x)

np.savetxt('filtered/short_filter_glacial_chol_1_f.txt',filtered_glacial_chol_1_f)
np.savetxt('filtered/short_filter_glacial_chol_2_f.txt',filtered_glacial_chol_2_f)
np.savetxt('filtered/short_filter_glacial_chol_3_f.txt',filtered_glacial_chol_3_f)
np.savetxt('filtered/short_filter_glacial_chol_4_f.txt',filtered_glacial_chol_4_f)
np.savetxt('filtered/short_filter_glacial_chol_5_f.txt',filtered_glacial_chol_5_f)
np.savetxt('filtered/short_filter_glacial_chol_6_f.txt',filtered_glacial_chol_6_f)
np.savetxt('filtered/short_filter_glacial_chol_7_f.txt',filtered_glacial_chol_7_f)
np.savetxt('filtered/short_filter_glacial_chol_8_f.txt',filtered_glacial_chol_8_f)
np.savetxt('filtered/short_filter_glacial_chol_9_f.txt',filtered_glacial_chol_9_f)
np.savetxt('filtered/short_filter_glacial_chol_10_f.txt',filtered_glacial_chol_10_f)

np.savetxt('filtered/short_filter_glacial_nochol_1_f.txt',filtered_glacial_nochol_1_f)
np.savetxt('filtered/short_filter_glacial_nochol_2_f.txt',filtered_glacial_nochol_2_f)
np.savetxt('filtered/short_filter_glacial_nochol_3_f.txt',filtered_glacial_nochol_3_f)
np.savetxt('filtered/short_filter_glacial_nochol_4_f.txt',filtered_glacial_nochol_4_f)
np.savetxt('filtered/short_filter_glacial_nochol_5_f.txt',filtered_glacial_nochol_5_f)
np.savetxt('filtered/short_filter_glacial_nochol_6_f.txt',filtered_glacial_nochol_6_f)
np.savetxt('filtered/short_filter_glacial_nochol_7_f.txt',filtered_glacial_nochol_7_f)
np.savetxt('filtered/short_filter_glacial_nochol_8_f.txt',filtered_glacial_nochol_8_f)
np.savetxt('filtered/short_filter_glacial_nochol_9_f.txt',filtered_glacial_nochol_9_f)
np.savetxt('filtered/short_filter_glacial_nochol_10_f.txt',filtered_glacial_nochol_10_f)


np.savetxt('filtered/short_filter_slower_chol_11_x.txt',filtered_slower_chol_11_x)
np.savetxt('filtered/short_filter_slower_chol_12_x.txt',filtered_slower_chol_12_x)
np.savetxt('filtered/short_filter_slower_chol_13_x.txt',filtered_slower_chol_13_x)
np.savetxt('filtered/short_filter_slower_chol_14_x.txt',filtered_slower_chol_14_x)
np.savetxt('filtered/short_filter_slower_chol_15_x.txt',filtered_slower_chol_15_x)
np.savetxt('filtered/short_filter_slower_chol_16_x.txt',filtered_slower_chol_16_x)
np.savetxt('filtered/short_filter_slower_chol_17_x.txt',filtered_slower_chol_17_x)
np.savetxt('filtered/short_filter_slower_chol_18_x.txt',filtered_slower_chol_18_x)
np.savetxt('filtered/short_filter_slower_chol_19_x.txt',filtered_slower_chol_19_x)
np.savetxt('filtered/short_filter_slower_chol_20_x.txt',filtered_slower_chol_20_x)

np.savetxt('filtered/short_filter_slower_nochol_11_x.txt',filtered_slower_nochol_11_x)
np.savetxt('filtered/short_filter_slower_nochol_12_x.txt',filtered_slower_nochol_12_x)
np.savetxt('filtered/short_filter_slower_nochol_13_x.txt',filtered_slower_nochol_13_x)
np.savetxt('filtered/short_filter_slower_nochol_14_x.txt',filtered_slower_nochol_14_x)
np.savetxt('filtered/short_filter_slower_nochol_15_x.txt',filtered_slower_nochol_15_x)
np.savetxt('filtered/short_filter_slower_nochol_16_x.txt',filtered_slower_nochol_16_x)
np.savetxt('filtered/short_filter_slower_nochol_17_x.txt',filtered_slower_nochol_17_x)
np.savetxt('filtered/short_filter_slower_nochol_18_x.txt',filtered_slower_nochol_18_x)
np.savetxt('filtered/short_filter_slower_nochol_19_x.txt',filtered_slower_nochol_19_x)
np.savetxt('filtered/short_filter_slower_nochol_20_x.txt',filtered_slower_nochol_20_x)


np.savetxt('filtered/short_filter_slower_chol_11_f.txt',filtered_slower_chol_11_f)
np.savetxt('filtered/short_filter_slower_chol_12_f.txt',filtered_slower_chol_12_f)
np.savetxt('filtered/short_filter_slower_chol_13_f.txt',filtered_slower_chol_13_f)
np.savetxt('filtered/short_filter_slower_chol_14_f.txt',filtered_slower_chol_14_f)
np.savetxt('filtered/short_filter_slower_chol_15_f.txt',filtered_slower_chol_15_f)
np.savetxt('filtered/short_filter_slower_chol_16_f.txt',filtered_slower_chol_16_f)
np.savetxt('filtered/short_filter_slower_chol_17_f.txt',filtered_slower_chol_17_f)
np.savetxt('filtered/short_filter_slower_chol_18_f.txt',filtered_slower_chol_18_f)
np.savetxt('filtered/short_filter_slower_chol_19_f.txt',filtered_slower_chol_19_f)
np.savetxt('filtered/short_filter_slower_chol_20_f.txt',filtered_slower_chol_20_f)

np.savetxt('filtered/short_filter_slower_nochol_11_f.txt',filtered_slower_nochol_11_f)
np.savetxt('filtered/short_filter_slower_nochol_12_f.txt',filtered_slower_nochol_12_f)
np.savetxt('filtered/short_filter_slower_nochol_13_f.txt',filtered_slower_nochol_13_f)
np.savetxt('filtered/short_filter_slower_nochol_14_f.txt',filtered_slower_nochol_14_f)
np.savetxt('filtered/short_filter_slower_nochol_15_f.txt',filtered_slower_nochol_15_f)
np.savetxt('filtered/short_filter_slower_nochol_16_f.txt',filtered_slower_nochol_16_f)
np.savetxt('filtered/short_filter_slower_nochol_17_f.txt',filtered_slower_nochol_17_f)
np.savetxt('filtered/short_filter_slower_nochol_18_f.txt',filtered_slower_nochol_18_f)
np.savetxt('filtered/short_filter_slower_nochol_19_f.txt',filtered_slower_nochol_19_f)
np.savetxt('filtered/short_filter_slower_nochol_20_f.txt',filtered_slower_nochol_20_f)


np.savetxt('filtered/short_filter_slowest_chol_11_x.txt',filtered_slowest_chol_11_x)
np.savetxt('filtered/short_filter_slowest_chol_12_x.txt',filtered_slowest_chol_12_x)
np.savetxt('filtered/short_filter_slowest_chol_13_x.txt',filtered_slowest_chol_13_x)
np.savetxt('filtered/short_filter_slowest_chol_14_x.txt',filtered_slowest_chol_14_x)
np.savetxt('filtered/short_filter_slowest_chol_15_x.txt',filtered_slowest_chol_15_x)
np.savetxt('filtered/short_filter_slowest_chol_16_x.txt',filtered_slowest_chol_16_x)
np.savetxt('filtered/short_filter_slowest_chol_17_x.txt',filtered_slowest_chol_17_x)
np.savetxt('filtered/short_filter_slowest_chol_18_x.txt',filtered_slowest_chol_18_x)
np.savetxt('filtered/short_filter_slowest_chol_19_x.txt',filtered_slowest_chol_19_x)
np.savetxt('filtered/short_filter_slowest_chol_20_x.txt',filtered_slowest_chol_20_x)

np.savetxt('filtered/short_filter_slowest_nochol_11_x.txt',filtered_slowest_nochol_11_x)
np.savetxt('filtered/short_filter_slowest_nochol_12_x.txt',filtered_slowest_nochol_12_x)
np.savetxt('filtered/short_filter_slowest_nochol_13_x.txt',filtered_slowest_nochol_13_x)
np.savetxt('filtered/short_filter_slowest_nochol_14_x.txt',filtered_slowest_nochol_14_x)
np.savetxt('filtered/short_filter_slowest_nochol_15_x.txt',filtered_slowest_nochol_15_x)
np.savetxt('filtered/short_filter_slowest_nochol_16_x.txt',filtered_slowest_nochol_16_x)
np.savetxt('filtered/short_filter_slowest_nochol_17_x.txt',filtered_slowest_nochol_17_x)
np.savetxt('filtered/short_filter_slowest_nochol_18_x.txt',filtered_slowest_nochol_18_x)
np.savetxt('filtered/short_filter_slowest_nochol_19_x.txt',filtered_slowest_nochol_19_x)
np.savetxt('filtered/short_filter_slowest_nochol_20_x.txt',filtered_slowest_nochol_20_x)

np.savetxt('filtered/short_filter_slowest_chol_11_f.txt',filtered_slowest_chol_11_f)
np.savetxt('filtered/short_filter_slowest_chol_12_f.txt',filtered_slowest_chol_12_f)
np.savetxt('filtered/short_filter_slowest_chol_13_f.txt',filtered_slowest_chol_13_f)
np.savetxt('filtered/short_filter_slowest_chol_14_f.txt',filtered_slowest_chol_14_f)
np.savetxt('filtered/short_filter_slowest_chol_15_f.txt',filtered_slowest_chol_15_f)
np.savetxt('filtered/short_filter_slowest_chol_16_f.txt',filtered_slowest_chol_16_f)
np.savetxt('filtered/short_filter_slowest_chol_17_f.txt',filtered_slowest_chol_17_f)
np.savetxt('filtered/short_filter_slowest_chol_18_f.txt',filtered_slowest_chol_18_f)
np.savetxt('filtered/short_filter_slowest_chol_19_f.txt',filtered_slowest_chol_19_f)
np.savetxt('filtered/short_filter_slowest_chol_20_f.txt',filtered_slowest_chol_20_f)

np.savetxt('filtered/short_filter_slowest_nochol_11_f.txt',filtered_slowest_nochol_11_f)
np.savetxt('filtered/short_filter_slowest_nochol_12_f.txt',filtered_slowest_nochol_12_f)
np.savetxt('filtered/short_filter_slowest_nochol_13_f.txt',filtered_slowest_nochol_13_f)
np.savetxt('filtered/short_filter_slowest_nochol_14_f.txt',filtered_slowest_nochol_14_f)
np.savetxt('filtered/short_filter_slowest_nochol_15_f.txt',filtered_slowest_nochol_15_f)
np.savetxt('filtered/short_filter_slowest_nochol_16_f.txt',filtered_slowest_nochol_16_f)
np.savetxt('filtered/short_filter_slowest_nochol_17_f.txt',filtered_slowest_nochol_17_f)
np.savetxt('filtered/short_filter_slowest_nochol_18_f.txt',filtered_slowest_nochol_18_f)
np.savetxt('filtered/short_filter_slowest_nochol_19_f.txt',filtered_slowest_nochol_19_f)
np.savetxt('filtered/short_filter_slowest_nochol_20_f.txt',filtered_slowest_nochol_20_f)

np.savetxt('filtered/short_filter_glacial_chol_11_x.txt',filtered_glacial_chol_11_x)
np.savetxt('filtered/short_filter_glacial_chol_12_x.txt',filtered_glacial_chol_12_x)
np.savetxt('filtered/short_filter_glacial_chol_13_x.txt',filtered_glacial_chol_13_x)
np.savetxt('filtered/short_filter_glacial_chol_14_x.txt',filtered_glacial_chol_14_x)
np.savetxt('filtered/short_filter_glacial_chol_15_x.txt',filtered_glacial_chol_15_x)
np.savetxt('filtered/short_filter_glacial_chol_16_x.txt',filtered_glacial_chol_16_x)
np.savetxt('filtered/short_filter_glacial_chol_17_x.txt',filtered_glacial_chol_17_x)
np.savetxt('filtered/short_filter_glacial_chol_18_x.txt',filtered_glacial_chol_18_x)
np.savetxt('filtered/short_filter_glacial_chol_19_x.txt',filtered_glacial_chol_19_x)
np.savetxt('filtered/short_filter_glacial_chol_20_x.txt',filtered_glacial_chol_20_x)

np.savetxt('filtered/short_filter_glacial_nochol_11_x.txt',filtered_glacial_nochol_11_x)
np.savetxt('filtered/short_filter_glacial_nochol_12_x.txt',filtered_glacial_nochol_12_x)
np.savetxt('filtered/short_filter_glacial_nochol_13_x.txt',filtered_glacial_nochol_13_x)
np.savetxt('filtered/short_filter_glacial_nochol_14_x.txt',filtered_glacial_nochol_14_x)
np.savetxt('filtered/short_filter_glacial_nochol_15_x.txt',filtered_glacial_nochol_15_x)
np.savetxt('filtered/short_filter_glacial_nochol_16_x.txt',filtered_glacial_nochol_16_x)
np.savetxt('filtered/short_filter_glacial_nochol_17_x.txt',filtered_glacial_nochol_17_x)
np.savetxt('filtered/short_filter_glacial_nochol_18_x.txt',filtered_glacial_nochol_18_x)
np.savetxt('filtered/short_filter_glacial_nochol_19_x.txt',filtered_glacial_nochol_19_x)
np.savetxt('filtered/short_filter_glacial_nochol_20_x.txt',filtered_glacial_nochol_20_x)

np.savetxt('filtered/short_filter_glacial_chol_11_f.txt',filtered_glacial_chol_11_f)
np.savetxt('filtered/short_filter_glacial_chol_12_f.txt',filtered_glacial_chol_12_f)
np.savetxt('filtered/short_filter_glacial_chol_13_f.txt',filtered_glacial_chol_13_f)
np.savetxt('filtered/short_filter_glacial_chol_14_f.txt',filtered_glacial_chol_14_f)
np.savetxt('filtered/short_filter_glacial_chol_15_f.txt',filtered_glacial_chol_15_f)
np.savetxt('filtered/short_filter_glacial_chol_16_f.txt',filtered_glacial_chol_16_f)
np.savetxt('filtered/short_filter_glacial_chol_17_f.txt',filtered_glacial_chol_17_f)
np.savetxt('filtered/short_filter_glacial_chol_18_f.txt',filtered_glacial_chol_18_f)
np.savetxt('filtered/short_filter_glacial_chol_19_f.txt',filtered_glacial_chol_19_f)
np.savetxt('filtered/short_filter_glacial_chol_20_f.txt',filtered_glacial_chol_20_f)

np.savetxt('filtered/short_filter_glacial_nochol_11_f.txt',filtered_glacial_nochol_11_f)
np.savetxt('filtered/short_filter_glacial_nochol_12_f.txt',filtered_glacial_nochol_12_f)
np.savetxt('filtered/short_filter_glacial_nochol_13_f.txt',filtered_glacial_nochol_13_f)
np.savetxt('filtered/short_filter_glacial_nochol_14_f.txt',filtered_glacial_nochol_14_f)
np.savetxt('filtered/short_filter_glacial_nochol_15_f.txt',filtered_glacial_nochol_15_f)
np.savetxt('filtered/short_filter_glacial_nochol_16_f.txt',filtered_glacial_nochol_16_f)
np.savetxt('filtered/short_filter_glacial_nochol_17_f.txt',filtered_glacial_nochol_17_f)
np.savetxt('filtered/short_filter_glacial_nochol_18_f.txt',filtered_glacial_nochol_18_f)
np.savetxt('filtered/short_filter_glacial_nochol_19_f.txt',filtered_glacial_nochol_19_f)
np.savetxt('filtered/short_filter_glacial_nochol_20_f.txt',filtered_glacial_nochol_20_f)

"""


filtered_slower_chol_1_x=np.loadtxt("filtered/short_filter_slower_chol_1_x.txt")
filtered_slower_chol_2_x=np.loadtxt("filtered/short_filter_slower_chol_2_x.txt")
filtered_slower_chol_3_x=np.loadtxt("filtered/short_filter_slower_chol_3_x.txt")
filtered_slower_chol_4_x=np.loadtxt("filtered/short_filter_slower_chol_4_x.txt")
filtered_slower_chol_5_x=np.loadtxt("filtered/short_filter_slower_chol_5_x.txt")
filtered_slower_chol_6_x=np.loadtxt("filtered/short_filter_slower_chol_6_x.txt")
filtered_slower_chol_7_x=np.loadtxt("filtered/short_filter_slower_chol_7_x.txt")
filtered_slower_chol_8_x=np.loadtxt("filtered/short_filter_slower_chol_8_x.txt")
filtered_slower_chol_9_x=np.loadtxt("filtered/short_filter_slower_chol_9_x.txt")
filtered_slower_chol_10_x=np.loadtxt("filtered/short_filter_slower_chol_10_x.txt")

filtered_slower_nochol_1_x=np.loadtxt("filtered/short_filter_slower_nochol_1_x.txt")
filtered_slower_nochol_2_x=np.loadtxt("filtered/short_filter_slower_nochol_2_x.txt")
filtered_slower_nochol_3_x=np.loadtxt("filtered/short_filter_slower_nochol_3_x.txt")
filtered_slower_nochol_4_x=np.loadtxt("filtered/short_filter_slower_nochol_4_x.txt")
filtered_slower_nochol_5_x=np.loadtxt("filtered/short_filter_slower_nochol_5_x.txt")
filtered_slower_nochol_6_x=np.loadtxt("filtered/short_filter_slower_nochol_6_x.txt")
filtered_slower_nochol_7_x=np.loadtxt("filtered/short_filter_slower_nochol_7_x.txt")
filtered_slower_nochol_8_x=np.loadtxt("filtered/short_filter_slower_nochol_8_x.txt")
filtered_slower_nochol_9_x=np.loadtxt("filtered/short_filter_slower_nochol_9_x.txt")
filtered_slower_nochol_10_x=np.loadtxt("filtered/short_filter_slower_nochol_10_x.txt")

filtered_slower_chol_1_f=np.loadtxt("filtered/short_filter_slower_chol_1_f.txt")
filtered_slower_chol_2_f=np.loadtxt("filtered/short_filter_slower_chol_2_f.txt")
filtered_slower_chol_3_f=np.loadtxt("filtered/short_filter_slower_chol_3_f.txt")
filtered_slower_chol_4_f=np.loadtxt("filtered/short_filter_slower_chol_4_f.txt")
filtered_slower_chol_5_f=np.loadtxt("filtered/short_filter_slower_chol_5_f.txt")
filtered_slower_chol_6_f=np.loadtxt("filtered/short_filter_slower_chol_6_f.txt")
filtered_slower_chol_7_f=np.loadtxt("filtered/short_filter_slower_chol_7_f.txt")
filtered_slower_chol_8_f=np.loadtxt("filtered/short_filter_slower_chol_8_f.txt")
filtered_slower_chol_9_f=np.loadtxt("filtered/short_filter_slower_chol_9_f.txt")
filtered_slower_chol_10_f=np.loadtxt("filtered/short_filter_slower_chol_10_f.txt")

filtered_slower_nochol_1_f=np.loadtxt("filtered/short_filter_slower_nochol_1_f.txt")
filtered_slower_nochol_2_f=np.loadtxt("filtered/short_filter_slower_nochol_2_f.txt")
filtered_slower_nochol_3_f=np.loadtxt("filtered/short_filter_slower_nochol_3_f.txt")
filtered_slower_nochol_4_f=np.loadtxt("filtered/short_filter_slower_nochol_4_f.txt")
filtered_slower_nochol_5_f=np.loadtxt("filtered/short_filter_slower_nochol_5_f.txt")
filtered_slower_nochol_6_f=np.loadtxt("filtered/short_filter_slower_nochol_6_f.txt")
filtered_slower_nochol_7_f=np.loadtxt("filtered/short_filter_slower_nochol_7_f.txt")
filtered_slower_nochol_8_f=np.loadtxt("filtered/short_filter_slower_nochol_8_f.txt")
filtered_slower_nochol_9_f=np.loadtxt("filtered/short_filter_slower_nochol_9_f.txt")
filtered_slower_nochol_10_f=np.loadtxt("filtered/short_filter_slower_nochol_10_f.txt")

filtered_slowest_chol_1_x=np.loadtxt("filtered/short_filter_slowest_chol_1_x.txt")
filtered_slowest_chol_2_x=np.loadtxt("filtered/short_filter_slowest_chol_2_x.txt")
filtered_slowest_chol_3_x=np.loadtxt("filtered/short_filter_slowest_chol_3_x.txt")
filtered_slowest_chol_4_x=np.loadtxt("filtered/short_filter_slowest_chol_4_x.txt")
filtered_slowest_chol_5_x=np.loadtxt("filtered/short_filter_slowest_chol_5_x.txt")
filtered_slowest_chol_6_x=np.loadtxt("filtered/short_filter_slowest_chol_6_x.txt")
filtered_slowest_chol_7_x=np.loadtxt("filtered/short_filter_slowest_chol_7_x.txt")
filtered_slowest_chol_8_x=np.loadtxt("filtered/short_filter_slowest_chol_8_x.txt")
filtered_slowest_chol_9_x=np.loadtxt("filtered/short_filter_slowest_chol_9_x.txt")
filtered_slowest_chol_10_x=np.loadtxt("filtered/short_filter_slowest_chol_10_x.txt")

filtered_slowest_nochol_1_x=np.loadtxt("filtered/short_filter_slowest_nochol_1_x.txt")
filtered_slowest_nochol_2_x=np.loadtxt("filtered/short_filter_slowest_nochol_2_x.txt")
filtered_slowest_nochol_3_x=np.loadtxt("filtered/short_filter_slowest_nochol_3_x.txt")
filtered_slowest_nochol_4_x=np.loadtxt("filtered/short_filter_slowest_nochol_4_x.txt")
filtered_slowest_nochol_5_x=np.loadtxt("filtered/short_filter_slowest_nochol_5_x.txt")
filtered_slowest_nochol_6_x=np.loadtxt("filtered/short_filter_slowest_nochol_6_x.txt")
filtered_slowest_nochol_7_x=np.loadtxt("filtered/short_filter_slowest_nochol_7_x.txt")
filtered_slowest_nochol_8_x=np.loadtxt("filtered/short_filter_slowest_nochol_8_x.txt")
filtered_slowest_nochol_9_x=np.loadtxt("filtered/short_filter_slowest_nochol_9_x.txt")
filtered_slowest_nochol_10_x=np.loadtxt("filtered/short_filter_slowest_nochol_10_x.txt")

filtered_slowest_chol_1_f=np.loadtxt("filtered/short_filter_slowest_chol_1_f.txt")
filtered_slowest_chol_2_f=np.loadtxt("filtered/short_filter_slowest_chol_2_f.txt")
filtered_slowest_chol_3_f=np.loadtxt("filtered/short_filter_slowest_chol_3_f.txt")
filtered_slowest_chol_4_f=np.loadtxt("filtered/short_filter_slowest_chol_4_f.txt")
filtered_slowest_chol_5_f=np.loadtxt("filtered/short_filter_slowest_chol_5_f.txt")
filtered_slowest_chol_6_f=np.loadtxt("filtered/short_filter_slowest_chol_6_f.txt")
filtered_slowest_chol_7_f=np.loadtxt("filtered/short_filter_slowest_chol_7_f.txt")
filtered_slowest_chol_8_f=np.loadtxt("filtered/short_filter_slowest_chol_8_f.txt")
filtered_slowest_chol_9_f=np.loadtxt("filtered/short_filter_slowest_chol_9_f.txt")
filtered_slowest_chol_10_f=np.loadtxt("filtered/short_filter_slowest_chol_10_f.txt")

filtered_slowest_nochol_1_f=np.loadtxt("filtered/short_filter_slowest_nochol_1_f.txt")
filtered_slowest_nochol_2_f=np.loadtxt("filtered/short_filter_slowest_nochol_2_f.txt")
filtered_slowest_nochol_3_f=np.loadtxt("filtered/short_filter_slowest_nochol_3_f.txt")
filtered_slowest_nochol_4_f=np.loadtxt("filtered/short_filter_slowest_nochol_4_f.txt")
filtered_slowest_nochol_5_f=np.loadtxt("filtered/short_filter_slowest_nochol_5_f.txt")
filtered_slowest_nochol_6_f=np.loadtxt("filtered/short_filter_slowest_nochol_6_f.txt")
filtered_slowest_nochol_7_f=np.loadtxt("filtered/short_filter_slowest_nochol_7_f.txt")
filtered_slowest_nochol_8_f=np.loadtxt("filtered/short_filter_slowest_nochol_8_f.txt")
filtered_slowest_nochol_9_f=np.loadtxt("filtered/short_filter_slowest_nochol_9_f.txt")
filtered_slowest_nochol_10_f=np.loadtxt("filtered/short_filter_slowest_nochol_10_f.txt")

filtered_glacial_chol_1_x=np.loadtxt("filtered/short_filter_glacial_chol_1_x.txt")
filtered_glacial_chol_2_x=np.loadtxt("filtered/short_filter_glacial_chol_2_x.txt")
filtered_glacial_chol_3_x=np.loadtxt("filtered/short_filter_glacial_chol_3_x.txt")
filtered_glacial_chol_4_x=np.loadtxt("filtered/short_filter_glacial_chol_4_x.txt")
filtered_glacial_chol_5_x=np.loadtxt("filtered/short_filter_glacial_chol_5_x.txt")
filtered_glacial_chol_6_x=np.loadtxt("filtered/short_filter_glacial_chol_6_x.txt")
filtered_glacial_chol_7_x=np.loadtxt("filtered/short_filter_glacial_chol_7_x.txt")
filtered_glacial_chol_8_x=np.loadtxt("filtered/short_filter_glacial_chol_8_x.txt")
filtered_glacial_chol_9_x=np.loadtxt("filtered/short_filter_glacial_chol_9_x.txt")
filtered_glacial_chol_10_x=np.loadtxt("filtered/short_filter_glacial_chol_10_x.txt")

filtered_glacial_nochol_1_x=np.loadtxt("filtered/short_filter_glacial_nochol_1_x.txt")
filtered_glacial_nochol_2_x=np.loadtxt("filtered/short_filter_glacial_nochol_2_x.txt")
filtered_glacial_nochol_3_x=np.loadtxt("filtered/short_filter_glacial_nochol_3_x.txt")
filtered_glacial_nochol_4_x=np.loadtxt("filtered/short_filter_glacial_nochol_4_x.txt")
filtered_glacial_nochol_5_x=np.loadtxt("filtered/short_filter_glacial_nochol_5_x.txt")
filtered_glacial_nochol_6_x=np.loadtxt("filtered/short_filter_glacial_nochol_6_x.txt")
filtered_glacial_nochol_7_x=np.loadtxt("filtered/short_filter_glacial_nochol_7_x.txt")
filtered_glacial_nochol_8_x=np.loadtxt("filtered/short_filter_glacial_nochol_8_x.txt")
filtered_glacial_nochol_9_x=np.loadtxt("filtered/short_filter_glacial_nochol_9_x.txt")
filtered_glacial_nochol_10_x=np.loadtxt("filtered/short_filter_glacial_nochol_10_x.txt")

filtered_glacial_chol_1_f=np.loadtxt("filtered/short_filter_glacial_chol_1_f.txt")
filtered_glacial_chol_2_f=np.loadtxt("filtered/short_filter_glacial_chol_2_f.txt")
filtered_glacial_chol_3_f=np.loadtxt("filtered/short_filter_glacial_chol_3_f.txt")
filtered_glacial_chol_4_f=np.loadtxt("filtered/short_filter_glacial_chol_4_f.txt")
filtered_glacial_chol_5_f=np.loadtxt("filtered/short_filter_glacial_chol_5_f.txt")
filtered_glacial_chol_6_f=np.loadtxt("filtered/short_filter_glacial_chol_6_f.txt")
filtered_glacial_chol_7_f=np.loadtxt("filtered/short_filter_glacial_chol_7_f.txt")
filtered_glacial_chol_8_f=np.loadtxt("filtered/short_filter_glacial_chol_8_f.txt")
filtered_glacial_chol_9_f=np.loadtxt("filtered/short_filter_glacial_chol_9_f.txt")
filtered_glacial_chol_10_f=np.loadtxt("filtered/short_filter_glacial_chol_10_f.txt")

filtered_glacial_nochol_1_f=np.loadtxt("filtered/short_filter_glacial_nochol_1_f.txt")
filtered_glacial_nochol_2_f=np.loadtxt("filtered/short_filter_glacial_nochol_2_f.txt")
filtered_glacial_nochol_3_f=np.loadtxt("filtered/short_filter_glacial_nochol_3_f.txt")
filtered_glacial_nochol_4_f=np.loadtxt("filtered/short_filter_glacial_nochol_4_f.txt")
filtered_glacial_nochol_5_f=np.loadtxt("filtered/short_filter_glacial_nochol_5_f.txt")
filtered_glacial_nochol_6_f=np.loadtxt("filtered/short_filter_glacial_nochol_6_f.txt")
filtered_glacial_nochol_7_f=np.loadtxt("filtered/short_filter_glacial_nochol_7_f.txt")
filtered_glacial_nochol_8_f=np.loadtxt("filtered/short_filter_glacial_nochol_8_f.txt")
filtered_glacial_nochol_9_f=np.loadtxt("filtered/short_filter_glacial_nochol_9_f.txt")
filtered_glacial_nochol_10_f=np.loadtxt("filtered/short_filter_glacial_nochol_10_f.txt")

filtered_slower_chol_11_x=np.loadtxt("filtered/short_filter_slower_chol_11_x.txt")
filtered_slower_chol_12_x=np.loadtxt("filtered/short_filter_slower_chol_12_x.txt")
filtered_slower_chol_13_x=np.loadtxt("filtered/short_filter_slower_chol_13_x.txt")
filtered_slower_chol_14_x=np.loadtxt("filtered/short_filter_slower_chol_14_x.txt")
filtered_slower_chol_15_x=np.loadtxt("filtered/short_filter_slower_chol_15_x.txt")
filtered_slower_chol_16_x=np.loadtxt("filtered/short_filter_slower_chol_16_x.txt")
filtered_slower_chol_17_x=np.loadtxt("filtered/short_filter_slower_chol_17_x.txt")
filtered_slower_chol_18_x=np.loadtxt("filtered/short_filter_slower_chol_18_x.txt")
filtered_slower_chol_19_x=np.loadtxt("filtered/short_filter_slower_chol_19_x.txt")
filtered_slower_chol_20_x=np.loadtxt("filtered/short_filter_slower_chol_20_x.txt")

filtered_slower_nochol_11_x=np.loadtxt("filtered/short_filter_slower_nochol_11_x.txt")
filtered_slower_nochol_12_x=np.loadtxt("filtered/short_filter_slower_nochol_12_x.txt")
filtered_slower_nochol_13_x=np.loadtxt("filtered/short_filter_slower_nochol_13_x.txt")
filtered_slower_nochol_14_x=np.loadtxt("filtered/short_filter_slower_nochol_14_x.txt")
filtered_slower_nochol_15_x=np.loadtxt("filtered/short_filter_slower_nochol_15_x.txt")
filtered_slower_nochol_16_x=np.loadtxt("filtered/short_filter_slower_nochol_16_x.txt")
filtered_slower_nochol_17_x=np.loadtxt("filtered/short_filter_slower_nochol_17_x.txt")
filtered_slower_nochol_18_x=np.loadtxt("filtered/short_filter_slower_nochol_18_x.txt")
filtered_slower_nochol_19_x=np.loadtxt("filtered/short_filter_slower_nochol_19_x.txt")
filtered_slower_nochol_20_x=np.loadtxt("filtered/short_filter_slower_nochol_20_x.txt")

filtered_slower_chol_11_f=np.loadtxt("filtered/short_filter_slower_chol_11_f.txt")
filtered_slower_chol_12_f=np.loadtxt("filtered/short_filter_slower_chol_12_f.txt")
filtered_slower_chol_13_f=np.loadtxt("filtered/short_filter_slower_chol_13_f.txt")
filtered_slower_chol_14_f=np.loadtxt("filtered/short_filter_slower_chol_14_f.txt")
filtered_slower_chol_15_f=np.loadtxt("filtered/short_filter_slower_chol_15_f.txt")
filtered_slower_chol_16_f=np.loadtxt("filtered/short_filter_slower_chol_16_f.txt")
filtered_slower_chol_17_f=np.loadtxt("filtered/short_filter_slower_chol_17_f.txt")
filtered_slower_chol_18_f=np.loadtxt("filtered/short_filter_slower_chol_18_f.txt")
filtered_slower_chol_19_f=np.loadtxt("filtered/short_filter_slower_chol_19_f.txt")
filtered_slower_chol_20_f=np.loadtxt("filtered/short_filter_slower_chol_20_f.txt")

filtered_slower_nochol_11_f=np.loadtxt("filtered/short_filter_slower_nochol_11_f.txt")
filtered_slower_nochol_12_f=np.loadtxt("filtered/short_filter_slower_nochol_12_f.txt")
filtered_slower_nochol_13_f=np.loadtxt("filtered/short_filter_slower_nochol_13_f.txt")
filtered_slower_nochol_14_f=np.loadtxt("filtered/short_filter_slower_nochol_14_f.txt")
filtered_slower_nochol_15_f=np.loadtxt("filtered/short_filter_slower_nochol_15_f.txt")
filtered_slower_nochol_16_f=np.loadtxt("filtered/short_filter_slower_nochol_16_f.txt")
filtered_slower_nochol_17_f=np.loadtxt("filtered/short_filter_slower_nochol_17_f.txt")
filtered_slower_nochol_18_f=np.loadtxt("filtered/short_filter_slower_nochol_18_f.txt")
filtered_slower_nochol_19_f=np.loadtxt("filtered/short_filter_slower_nochol_19_f.txt")
filtered_slower_nochol_20_f=np.loadtxt("filtered/short_filter_slower_nochol_20_f.txt")

filtered_slowest_chol_11_x=np.loadtxt("filtered/short_filter_slowest_chol_11_x.txt")
filtered_slowest_chol_12_x=np.loadtxt("filtered/short_filter_slowest_chol_12_x.txt")
filtered_slowest_chol_13_x=np.loadtxt("filtered/short_filter_slowest_chol_13_x.txt")
filtered_slowest_chol_14_x=np.loadtxt("filtered/short_filter_slowest_chol_14_x.txt")
filtered_slowest_chol_15_x=np.loadtxt("filtered/short_filter_slowest_chol_15_x.txt")
filtered_slowest_chol_16_x=np.loadtxt("filtered/short_filter_slowest_chol_16_x.txt")
filtered_slowest_chol_17_x=np.loadtxt("filtered/short_filter_slowest_chol_17_x.txt")
filtered_slowest_chol_18_x=np.loadtxt("filtered/short_filter_slowest_chol_18_x.txt")
filtered_slowest_chol_19_x=np.loadtxt("filtered/short_filter_slowest_chol_19_x.txt")
filtered_slowest_chol_20_x=np.loadtxt("filtered/short_filter_slowest_chol_20_x.txt")

filtered_slowest_nochol_11_x=np.loadtxt("filtered/short_filter_slowest_nochol_11_x.txt")
filtered_slowest_nochol_12_x=np.loadtxt("filtered/short_filter_slowest_nochol_12_x.txt")
filtered_slowest_nochol_13_x=np.loadtxt("filtered/short_filter_slowest_nochol_13_x.txt")
filtered_slowest_nochol_14_x=np.loadtxt("filtered/short_filter_slowest_nochol_14_x.txt")
filtered_slowest_nochol_15_x=np.loadtxt("filtered/short_filter_slowest_nochol_15_x.txt")
filtered_slowest_nochol_16_x=np.loadtxt("filtered/short_filter_slowest_nochol_16_x.txt")
filtered_slowest_nochol_17_x=np.loadtxt("filtered/short_filter_slowest_nochol_17_x.txt")
filtered_slowest_nochol_18_x=np.loadtxt("filtered/short_filter_slowest_nochol_18_x.txt")
filtered_slowest_nochol_19_x=np.loadtxt("filtered/short_filter_slowest_nochol_19_x.txt")
filtered_slowest_nochol_20_x=np.loadtxt("filtered/short_filter_slowest_nochol_20_x.txt")

filtered_slowest_chol_11_f=np.loadtxt("filtered/short_filter_slowest_chol_11_f.txt")
filtered_slowest_chol_12_f=np.loadtxt("filtered/short_filter_slowest_chol_12_f.txt")
filtered_slowest_chol_13_f=np.loadtxt("filtered/short_filter_slowest_chol_13_f.txt")
filtered_slowest_chol_14_f=np.loadtxt("filtered/short_filter_slowest_chol_14_f.txt")
filtered_slowest_chol_15_f=np.loadtxt("filtered/short_filter_slowest_chol_15_f.txt")
filtered_slowest_chol_16_f=np.loadtxt("filtered/short_filter_slowest_chol_16_f.txt")
filtered_slowest_chol_17_f=np.loadtxt("filtered/short_filter_slowest_chol_17_f.txt")
filtered_slowest_chol_18_f=np.loadtxt("filtered/short_filter_slowest_chol_18_f.txt")
filtered_slowest_chol_19_f=np.loadtxt("filtered/short_filter_slowest_chol_19_f.txt")
filtered_slowest_chol_20_f=np.loadtxt("filtered/short_filter_slowest_chol_20_f.txt")

filtered_slowest_nochol_11_f=np.loadtxt("filtered/short_filter_slowest_nochol_11_f.txt")
filtered_slowest_nochol_12_f=np.loadtxt("filtered/short_filter_slowest_nochol_12_f.txt")
filtered_slowest_nochol_13_f=np.loadtxt("filtered/short_filter_slowest_nochol_13_f.txt")
filtered_slowest_nochol_14_f=np.loadtxt("filtered/short_filter_slowest_nochol_14_f.txt")
filtered_slowest_nochol_15_f=np.loadtxt("filtered/short_filter_slowest_nochol_15_f.txt")
filtered_slowest_nochol_16_f=np.loadtxt("filtered/short_filter_slowest_nochol_16_f.txt")
filtered_slowest_nochol_17_f=np.loadtxt("filtered/short_filter_slowest_nochol_17_f.txt")
filtered_slowest_nochol_18_f=np.loadtxt("filtered/short_filter_slowest_nochol_18_f.txt")
filtered_slowest_nochol_19_f=np.loadtxt("filtered/short_filter_slowest_nochol_19_f.txt")
filtered_slowest_nochol_20_f=np.loadtxt("filtered/short_filter_slowest_nochol_20_f.txt")

filtered_glacial_chol_11_x=np.loadtxt("filtered/short_filter_glacial_chol_11_x.txt")
filtered_glacial_chol_12_x=np.loadtxt("filtered/short_filter_glacial_chol_12_x.txt")
filtered_glacial_chol_13_x=np.loadtxt("filtered/short_filter_glacial_chol_13_x.txt")
filtered_glacial_chol_14_x=np.loadtxt("filtered/short_filter_glacial_chol_14_x.txt")
filtered_glacial_chol_15_x=np.loadtxt("filtered/short_filter_glacial_chol_15_x.txt")
filtered_glacial_chol_16_x=np.loadtxt("filtered/short_filter_glacial_chol_16_x.txt")
filtered_glacial_chol_17_x=np.loadtxt("filtered/short_filter_glacial_chol_17_x.txt")
filtered_glacial_chol_18_x=np.loadtxt("filtered/short_filter_glacial_chol_18_x.txt")
filtered_glacial_chol_19_x=np.loadtxt("filtered/short_filter_glacial_chol_19_x.txt")
filtered_glacial_chol_20_x=np.loadtxt("filtered/short_filter_glacial_chol_20_x.txt")

filtered_glacial_nochol_11_x=np.loadtxt("filtered/short_filter_glacial_nochol_11_x.txt")
filtered_glacial_nochol_12_x=np.loadtxt("filtered/short_filter_glacial_nochol_12_x.txt")
filtered_glacial_nochol_13_x=np.loadtxt("filtered/short_filter_glacial_nochol_13_x.txt")
filtered_glacial_nochol_14_x=np.loadtxt("filtered/short_filter_glacial_nochol_14_x.txt")
filtered_glacial_nochol_15_x=np.loadtxt("filtered/short_filter_glacial_nochol_15_x.txt")
filtered_glacial_nochol_16_x=np.loadtxt("filtered/short_filter_glacial_nochol_16_x.txt")
filtered_glacial_nochol_17_x=np.loadtxt("filtered/short_filter_glacial_nochol_17_x.txt")
filtered_glacial_nochol_18_x=np.loadtxt("filtered/short_filter_glacial_nochol_18_x.txt")
filtered_glacial_nochol_19_x=np.loadtxt("filtered/short_filter_glacial_nochol_19_x.txt")
filtered_glacial_nochol_20_x=np.loadtxt("filtered/short_filter_glacial_nochol_20_x.txt")

filtered_glacial_chol_11_f=np.loadtxt("filtered/short_filter_glacial_chol_11_f.txt")
filtered_glacial_chol_12_f=np.loadtxt("filtered/short_filter_glacial_chol_12_f.txt")
filtered_glacial_chol_13_f=np.loadtxt("filtered/short_filter_glacial_chol_13_f.txt")
filtered_glacial_chol_14_f=np.loadtxt("filtered/short_filter_glacial_chol_14_f.txt")
filtered_glacial_chol_15_f=np.loadtxt("filtered/short_filter_glacial_chol_15_f.txt")
filtered_glacial_chol_16_f=np.loadtxt("filtered/short_filter_glacial_chol_16_f.txt")
filtered_glacial_chol_17_f=np.loadtxt("filtered/short_filter_glacial_chol_17_f.txt")
filtered_glacial_chol_18_f=np.loadtxt("filtered/short_filter_glacial_chol_18_f.txt")
filtered_glacial_chol_19_f=np.loadtxt("filtered/short_filter_glacial_chol_19_f.txt")
filtered_glacial_chol_20_f=np.loadtxt("filtered/short_filter_glacial_chol_20_f.txt")

filtered_glacial_nochol_11_f=np.loadtxt("filtered/short_filter_glacial_nochol_11_f.txt")
filtered_glacial_nochol_12_f=np.loadtxt("filtered/short_filter_glacial_nochol_12_f.txt")
filtered_glacial_nochol_13_f=np.loadtxt("filtered/short_filter_glacial_nochol_13_f.txt")
filtered_glacial_nochol_14_f=np.loadtxt("filtered/short_filter_glacial_nochol_14_f.txt")
filtered_glacial_nochol_15_f=np.loadtxt("filtered/short_filter_glacial_nochol_15_f.txt")
filtered_glacial_nochol_16_f=np.loadtxt("filtered/short_filter_glacial_nochol_16_f.txt")
filtered_glacial_nochol_17_f=np.loadtxt("filtered/short_filter_glacial_nochol_17_f.txt")
filtered_glacial_nochol_18_f=np.loadtxt("filtered/short_filter_glacial_nochol_18_f.txt")
filtered_glacial_nochol_19_f=np.loadtxt("filtered/short_filter_glacial_nochol_19_f.txt")
filtered_glacial_nochol_20_f=np.loadtxt("filtered/short_filter_glacial_nochol_20_f.txt")



corte=7.3  	#7.3?
rates=[0.004,0.02,0.1]
det_times_chol=[0]*3
det_times_nochol=[0]*3
det_times_chol_stderr=[0]*3
det_times_nochol_stderr=[0]*3
det_force_chol=[0]*3
det_force_nochol=[0]*3
det_force_chol_stderr=[0]*3
det_force_nochol_stderr=[0]*3
det_distance_chol=[0]*3
det_distance_nochol=[0]*3
det_distance_chol_stderr=[0]*3
det_distance_nochol_stderr=[0]*3



forces_glacial_chol=np.zeros(20)

forces_glacial_chol[0]=np.amax(filtered_glacial_chol_1_f[:np.where(filtered_glacial_chol_1_x<corte)[0][-1]])
forces_glacial_chol[1]=np.amax(filtered_glacial_chol_2_f[:np.where(filtered_glacial_chol_2_x<corte)[0][-1]])
forces_glacial_chol[2]=np.amax(filtered_glacial_chol_3_f[:np.where(filtered_glacial_chol_3_x<corte)[0][-1]])
forces_glacial_chol[3]=np.amax(filtered_glacial_chol_4_f[:np.where(filtered_glacial_chol_4_x<corte)[0][-1]])
forces_glacial_chol[4]=np.amax(filtered_glacial_chol_5_f[:np.where(filtered_glacial_chol_5_x<corte)[0][-1]])
forces_glacial_chol[5]=np.amax(filtered_glacial_chol_6_f[:np.where(filtered_glacial_chol_6_x<corte)[0][-1]])
forces_glacial_chol[6]=np.amax(filtered_glacial_chol_7_f[:np.where(filtered_glacial_chol_7_x<corte)[0][-1]])
forces_glacial_chol[7]=np.amax(filtered_glacial_chol_8_f[:np.where(filtered_glacial_chol_8_x<corte)[0][-1]])
forces_glacial_chol[8]=np.amax(filtered_glacial_chol_9_f[:np.where(filtered_glacial_chol_9_x<corte)[0][-1]])
forces_glacial_chol[9]=np.amax(filtered_glacial_chol_10_f[:np.where(filtered_glacial_chol_10_x<corte)[0][-1]])



distance_glacial_chol=np.zeros(20)

distance_glacial_chol[0]=filtered_glacial_chol_1_x[np.argmax(filtered_glacial_chol_1_f[:np.where(filtered_glacial_chol_1_x<corte)[0][-1]])]
distance_glacial_chol[1]=filtered_glacial_chol_2_x[np.argmax(filtered_glacial_chol_2_f[:np.where(filtered_glacial_chol_2_x<corte)[0][-1]])]
distance_glacial_chol[2]=filtered_glacial_chol_3_x[np.argmax(filtered_glacial_chol_3_f[:np.where(filtered_glacial_chol_3_x<corte)[0][-1]])]
distance_glacial_chol[3]=filtered_glacial_chol_4_x[np.argmax(filtered_glacial_chol_4_f[:np.where(filtered_glacial_chol_4_x<corte)[0][-1]])]
distance_glacial_chol[4]=filtered_glacial_chol_5_x[np.argmax(filtered_glacial_chol_5_f[:np.where(filtered_glacial_chol_5_x<corte)[0][-1]])]
distance_glacial_chol[5]=filtered_glacial_chol_6_x[np.argmax(filtered_glacial_chol_6_f[:np.where(filtered_glacial_chol_6_x<corte)[0][-1]])]
distance_glacial_chol[6]=filtered_glacial_chol_7_x[np.argmax(filtered_glacial_chol_7_f[:np.where(filtered_glacial_chol_7_x<corte)[0][-1]])]
distance_glacial_chol[7]=filtered_glacial_chol_8_x[np.argmax(filtered_glacial_chol_8_f[:np.where(filtered_glacial_chol_8_x<corte)[0][-1]])]
distance_glacial_chol[8]=filtered_glacial_chol_9_x[np.argmax(filtered_glacial_chol_9_f[:np.where(filtered_glacial_chol_9_x<corte)[0][-1]])]
distance_glacial_chol[9]=filtered_glacial_chol_10_x[np.argmax(filtered_glacial_chol_10_f[:np.where(filtered_glacial_chol_10_x<corte)[0][-1]])]

frames_glacial_chol=np.zeros(20)

frames_glacial_chol[0]=np.argmax(filtered_glacial_chol_1_f[:np.where(filtered_glacial_chol_1_x<corte)[0][-1]])
frames_glacial_chol[1]=np.argmax(filtered_glacial_chol_2_f[:np.where(filtered_glacial_chol_2_x<corte)[0][-1]])
frames_glacial_chol[2]=np.argmax(filtered_glacial_chol_3_f[:np.where(filtered_glacial_chol_3_x<corte)[0][-1]])
frames_glacial_chol[3]=np.argmax(filtered_glacial_chol_4_f[:np.where(filtered_glacial_chol_4_x<corte)[0][-1]])
frames_glacial_chol[4]=np.argmax(filtered_glacial_chol_5_f[:np.where(filtered_glacial_chol_5_x<corte)[0][-1]])
frames_glacial_chol[5]=np.argmax(filtered_glacial_chol_6_f[:np.where(filtered_glacial_chol_6_x<corte)[0][-1]])
frames_glacial_chol[6]=np.argmax(filtered_glacial_chol_7_f[:np.where(filtered_glacial_chol_7_x<corte)[0][-1]])
frames_glacial_chol[7]=np.argmax(filtered_glacial_chol_8_f[:np.where(filtered_glacial_chol_8_x<corte)[0][-1]])
frames_glacial_chol[8]=np.argmax(filtered_glacial_chol_9_f[:np.where(filtered_glacial_chol_9_x<corte)[0][-1]])
frames_glacial_chol[9]=np.argmax(filtered_glacial_chol_10_f[:np.where(filtered_glacial_chol_10_x<corte)[0][-1]])


forces_glacial_nochol=np.zeros(20)

forces_glacial_nochol[0]=np.amax(filtered_glacial_nochol_1_f[:np.where(filtered_glacial_nochol_1_x<corte)[0][-1]])
forces_glacial_nochol[1]=np.amax(filtered_glacial_nochol_2_f[:np.where(filtered_glacial_nochol_2_x<corte)[0][-1]])
forces_glacial_nochol[2]=np.amax(filtered_glacial_nochol_3_f[:np.where(filtered_glacial_nochol_3_x<corte)[0][-1]])
forces_glacial_nochol[3]=np.amax(filtered_glacial_nochol_4_f[:np.where(filtered_glacial_nochol_4_x<corte)[0][-1]])
forces_glacial_nochol[4]=np.amax(filtered_glacial_nochol_5_f[:np.where(filtered_glacial_nochol_5_x<corte)[0][-1]])
forces_glacial_nochol[5]=np.amax(filtered_glacial_nochol_6_f[:np.where(filtered_glacial_nochol_6_x<corte)[0][-1]])
forces_glacial_nochol[6]=np.amax(filtered_glacial_nochol_7_f[:np.where(filtered_glacial_nochol_7_x<corte)[0][-1]])
forces_glacial_nochol[7]=np.amax(filtered_glacial_nochol_8_f[:np.where(filtered_glacial_nochol_8_x<corte)[0][-1]])
forces_glacial_nochol[8]=np.amax(filtered_glacial_nochol_9_f[:np.where(filtered_glacial_nochol_9_x<corte)[0][-1]])
forces_glacial_nochol[9]=np.amax(filtered_glacial_nochol_10_f[:np.where(filtered_glacial_nochol_10_x<corte)[0][-1]])

distance_glacial_nochol=np.zeros(20)

distance_glacial_nochol[0]=filtered_glacial_nochol_1_x[np.argmax(filtered_glacial_nochol_1_f[:np.where(filtered_glacial_nochol_1_x<corte)[0][-1]])]
distance_glacial_nochol[1]=filtered_glacial_nochol_2_x[np.argmax(filtered_glacial_nochol_2_f[:np.where(filtered_glacial_nochol_2_x<corte)[0][-1]])]
distance_glacial_nochol[2]=filtered_glacial_nochol_3_x[np.argmax(filtered_glacial_nochol_3_f[:np.where(filtered_glacial_nochol_3_x<corte)[0][-1]])]
distance_glacial_nochol[3]=filtered_glacial_nochol_4_x[np.argmax(filtered_glacial_nochol_4_f[:np.where(filtered_glacial_nochol_4_x<corte)[0][-1]])]
distance_glacial_nochol[4]=filtered_glacial_nochol_5_x[np.argmax(filtered_glacial_nochol_5_f[:np.where(filtered_glacial_nochol_5_x<corte)[0][-1]])]
distance_glacial_nochol[5]=filtered_glacial_nochol_6_x[np.argmax(filtered_glacial_nochol_6_f[:np.where(filtered_glacial_nochol_6_x<corte)[0][-1]])]
distance_glacial_nochol[6]=filtered_glacial_nochol_7_x[np.argmax(filtered_glacial_nochol_7_f[:np.where(filtered_glacial_nochol_7_x<corte)[0][-1]])]
distance_glacial_nochol[7]=filtered_glacial_nochol_8_x[np.argmax(filtered_glacial_nochol_8_f[:np.where(filtered_glacial_nochol_8_x<corte)[0][-1]])]
distance_glacial_nochol[8]=filtered_glacial_nochol_9_x[np.argmax(filtered_glacial_nochol_9_f[:np.where(filtered_glacial_nochol_9_x<corte)[0][-1]])]
distance_glacial_nochol[9]=filtered_glacial_nochol_10_x[np.argmax(filtered_glacial_nochol_10_f[:np.where(filtered_glacial_nochol_10_x<corte)[0][-1]])]

frames_glacial_nochol=np.zeros(20)

frames_glacial_nochol[0]=np.argmax(filtered_glacial_nochol_1_f[:np.where(filtered_glacial_nochol_1_x<corte)[0][-1]])
frames_glacial_nochol[1]=np.argmax(filtered_glacial_nochol_2_f[:np.where(filtered_glacial_nochol_2_x<corte)[0][-1]])
frames_glacial_nochol[2]=np.argmax(filtered_glacial_nochol_3_f[:np.where(filtered_glacial_nochol_3_x<corte)[0][-1]])
frames_glacial_nochol[3]=np.argmax(filtered_glacial_nochol_4_f[:np.where(filtered_glacial_nochol_4_x<corte)[0][-1]])
frames_glacial_nochol[4]=np.argmax(filtered_glacial_nochol_5_f[:np.where(filtered_glacial_nochol_5_x<corte)[0][-1]])
frames_glacial_nochol[5]=np.argmax(filtered_glacial_nochol_6_f[:np.where(filtered_glacial_nochol_6_x<corte)[0][-1]])
frames_glacial_nochol[6]=np.argmax(filtered_glacial_nochol_7_f[:np.where(filtered_glacial_nochol_7_x<corte)[0][-1]])
frames_glacial_nochol[7]=np.argmax(filtered_glacial_nochol_8_f[:np.where(filtered_glacial_nochol_8_x<corte)[0][-1]])
frames_glacial_nochol[8]=np.argmax(filtered_glacial_nochol_9_f[:np.where(filtered_glacial_nochol_9_x<corte)[0][-1]])
frames_glacial_nochol[9]=np.argmax(filtered_glacial_nochol_10_f[:np.where(filtered_glacial_nochol_10_x<corte)[0][-1]])


forces_slowest_chol=np.zeros(20)

forces_slowest_chol[0]=np.amax(filtered_slowest_chol_1_f[:np.where(filtered_slowest_chol_1_x<corte)[0][-1]])
forces_slowest_chol[1]=np.amax(filtered_slowest_chol_2_f[:np.where(filtered_slowest_chol_2_x<corte)[0][-1]])
forces_slowest_chol[2]=np.amax(filtered_slowest_chol_3_f[:np.where(filtered_slowest_chol_3_x<corte)[0][-1]])
forces_slowest_chol[3]=np.amax(filtered_slowest_chol_4_f[:np.where(filtered_slowest_chol_4_x<corte)[0][-1]])
forces_slowest_chol[4]=np.amax(filtered_slowest_chol_5_f[:np.where(filtered_slowest_chol_5_x<corte)[0][-1]])
forces_slowest_chol[5]=np.amax(filtered_slowest_chol_6_f[:np.where(filtered_slowest_chol_6_x<corte)[0][-1]])
forces_slowest_chol[6]=np.amax(filtered_slowest_chol_7_f[:np.where(filtered_slowest_chol_7_x<corte)[0][-1]])
forces_slowest_chol[7]=np.amax(filtered_slowest_chol_8_f[:np.where(filtered_slowest_chol_8_x<corte)[0][-1]])
forces_slowest_chol[8]=np.amax(filtered_slowest_chol_9_f[:np.where(filtered_slowest_chol_9_x<corte)[0][-1]])
forces_slowest_chol[9]=np.amax(filtered_slowest_chol_10_f[:np.where(filtered_slowest_chol_10_x<corte)[0][-1]])

distance_slowest_chol=np.zeros(20)

distance_slowest_chol[0]=filtered_slowest_chol_1_x[np.argmax(filtered_slowest_chol_1_f[:np.where(filtered_slowest_chol_1_x<corte)[0][-1]])]
distance_slowest_chol[1]=filtered_slowest_chol_2_x[np.argmax(filtered_slowest_chol_2_f[:np.where(filtered_slowest_chol_2_x<corte)[0][-1]])]
distance_slowest_chol[2]=filtered_slowest_chol_3_x[np.argmax(filtered_slowest_chol_3_f[:np.where(filtered_slowest_chol_3_x<corte)[0][-1]])]
distance_slowest_chol[3]=filtered_slowest_chol_4_x[np.argmax(filtered_slowest_chol_4_f[:np.where(filtered_slowest_chol_4_x<corte)[0][-1]])]
distance_slowest_chol[4]=filtered_slowest_chol_5_x[np.argmax(filtered_slowest_chol_5_f[:np.where(filtered_slowest_chol_5_x<corte)[0][-1]])]
distance_slowest_chol[5]=filtered_slowest_chol_6_x[np.argmax(filtered_slowest_chol_6_f[:np.where(filtered_slowest_chol_6_x<corte)[0][-1]])]
distance_slowest_chol[6]=filtered_slowest_chol_7_x[np.argmax(filtered_slowest_chol_7_f[:np.where(filtered_slowest_chol_7_x<corte)[0][-1]])]
distance_slowest_chol[7]=filtered_slowest_chol_8_x[np.argmax(filtered_slowest_chol_8_f[:np.where(filtered_slowest_chol_8_x<corte)[0][-1]])]
distance_slowest_chol[8]=filtered_slowest_chol_9_x[np.argmax(filtered_slowest_chol_9_f[:np.where(filtered_slowest_chol_9_x<corte)[0][-1]])]
distance_slowest_chol[9]=filtered_slowest_chol_10_x[np.argmax(filtered_slowest_chol_10_f[:np.where(filtered_slowest_chol_10_x<corte)[0][-1]])]

frames_slowest_chol=np.zeros(20)

frames_slowest_chol[0]=np.argmax(filtered_slowest_chol_1_f[:np.where(filtered_slowest_chol_1_x<corte)[0][-1]])
frames_slowest_chol[1]=np.argmax(filtered_slowest_chol_2_f[:np.where(filtered_slowest_chol_2_x<corte)[0][-1]])
frames_slowest_chol[2]=np.argmax(filtered_slowest_chol_3_f[:np.where(filtered_slowest_chol_3_x<corte)[0][-1]])
frames_slowest_chol[3]=np.argmax(filtered_slowest_chol_4_f[:np.where(filtered_slowest_chol_4_x<corte)[0][-1]])
frames_slowest_chol[4]=np.argmax(filtered_slowest_chol_5_f[:np.where(filtered_slowest_chol_5_x<corte)[0][-1]])
frames_slowest_chol[5]=np.argmax(filtered_slowest_chol_6_f[:np.where(filtered_slowest_chol_6_x<corte)[0][-1]])
frames_slowest_chol[6]=np.argmax(filtered_slowest_chol_7_f[:np.where(filtered_slowest_chol_7_x<corte)[0][-1]])
frames_slowest_chol[7]=np.argmax(filtered_slowest_chol_8_f[:np.where(filtered_slowest_chol_8_x<corte)[0][-1]])
frames_slowest_chol[8]=np.argmax(filtered_slowest_chol_9_f[:np.where(filtered_slowest_chol_9_x<corte)[0][-1]])
frames_slowest_chol[9]=np.argmax(filtered_slowest_chol_10_f[:np.where(filtered_slowest_chol_10_x<corte)[0][-1]])


forces_slowest_nochol=np.zeros(20)

forces_slowest_nochol[0]=np.amax(filtered_slowest_nochol_1_f[:np.where(filtered_slowest_nochol_1_x<corte)[0][-1]])
forces_slowest_nochol[1]=np.amax(filtered_slowest_nochol_2_f[:np.where(filtered_slowest_nochol_2_x<corte)[0][-1]])
forces_slowest_nochol[2]=np.amax(filtered_slowest_nochol_3_f[:np.where(filtered_slowest_nochol_3_x<corte)[0][-1]])
forces_slowest_nochol[3]=np.amax(filtered_slowest_nochol_4_f[:np.where(filtered_slowest_nochol_4_x<corte)[0][-1]])
forces_slowest_nochol[4]=np.amax(filtered_slowest_nochol_5_f[:np.where(filtered_slowest_nochol_5_x<corte)[0][-1]])
forces_slowest_nochol[5]=np.amax(filtered_slowest_nochol_6_f[:np.where(filtered_slowest_nochol_6_x<corte)[0][-1]])
forces_slowest_nochol[6]=np.amax(filtered_slowest_nochol_7_f[:np.where(filtered_slowest_nochol_7_x<corte)[0][-1]])
forces_slowest_nochol[7]=np.amax(filtered_slowest_nochol_8_f[:np.where(filtered_slowest_nochol_8_x<corte)[0][-1]])
forces_slowest_nochol[8]=np.amax(filtered_slowest_nochol_9_f[:np.where(filtered_slowest_nochol_9_x<corte)[0][-1]])
forces_slowest_nochol[9]=np.amax(filtered_slowest_nochol_10_f[:np.where(filtered_slowest_nochol_10_x<corte)[0][-1]])

distance_slowest_nochol=np.zeros(20)

distance_slowest_nochol[0]=filtered_slowest_nochol_1_x[np.argmax(filtered_slowest_nochol_1_f[:np.where(filtered_slowest_nochol_1_x<corte)[0][-1]])]
distance_slowest_nochol[1]=filtered_slowest_nochol_2_x[np.argmax(filtered_slowest_nochol_2_f[:np.where(filtered_slowest_nochol_2_x<corte)[0][-1]])]
distance_slowest_nochol[2]=filtered_slowest_nochol_3_x[np.argmax(filtered_slowest_nochol_3_f[:np.where(filtered_slowest_nochol_3_x<corte)[0][-1]])]
distance_slowest_nochol[3]=filtered_slowest_nochol_4_x[np.argmax(filtered_slowest_nochol_4_f[:np.where(filtered_slowest_nochol_4_x<corte)[0][-1]])]
distance_slowest_nochol[4]=filtered_slowest_nochol_5_x[np.argmax(filtered_slowest_nochol_5_f[:np.where(filtered_slowest_nochol_5_x<corte)[0][-1]])]
distance_slowest_nochol[5]=filtered_slowest_nochol_6_x[np.argmax(filtered_slowest_nochol_6_f[:np.where(filtered_slowest_nochol_6_x<corte)[0][-1]])]
distance_slowest_nochol[6]=filtered_slowest_nochol_7_x[np.argmax(filtered_slowest_nochol_7_f[:np.where(filtered_slowest_nochol_7_x<corte)[0][-1]])]
distance_slowest_nochol[7]=filtered_slowest_nochol_8_x[np.argmax(filtered_slowest_nochol_8_f[:np.where(filtered_slowest_nochol_8_x<corte)[0][-1]])]
distance_slowest_nochol[8]=filtered_slowest_nochol_9_x[np.argmax(filtered_slowest_nochol_9_f[:np.where(filtered_slowest_nochol_9_x<corte)[0][-1]])]
distance_slowest_nochol[9]=filtered_slowest_nochol_10_x[np.argmax(filtered_slowest_nochol_10_f[:np.where(filtered_slowest_nochol_10_x<corte)[0][-1]])]

frames_slowest_nochol=np.zeros(20)

frames_slowest_nochol[0]=np.argmax(filtered_slowest_nochol_1_f[:np.where(filtered_slowest_nochol_1_x<corte)[0][-1]])
frames_slowest_nochol[1]=np.argmax(filtered_slowest_nochol_2_f[:np.where(filtered_slowest_nochol_2_x<corte)[0][-1]])
frames_slowest_nochol[2]=np.argmax(filtered_slowest_nochol_3_f[:np.where(filtered_slowest_nochol_3_x<corte)[0][-1]])
frames_slowest_nochol[3]=np.argmax(filtered_slowest_nochol_4_f[:np.where(filtered_slowest_nochol_4_x<corte)[0][-1]])
frames_slowest_nochol[4]=np.argmax(filtered_slowest_nochol_5_f[:np.where(filtered_slowest_nochol_5_x<corte)[0][-1]])
frames_slowest_nochol[5]=np.argmax(filtered_slowest_nochol_6_f[:np.where(filtered_slowest_nochol_6_x<corte)[0][-1]])
frames_slowest_nochol[6]=np.argmax(filtered_slowest_nochol_7_f[:np.where(filtered_slowest_nochol_7_x<corte)[0][-1]])
frames_slowest_nochol[7]=np.argmax(filtered_slowest_nochol_8_f[:np.where(filtered_slowest_nochol_8_x<corte)[0][-1]])
frames_slowest_nochol[8]=np.argmax(filtered_slowest_nochol_9_f[:np.where(filtered_slowest_nochol_9_x<corte)[0][-1]])
frames_slowest_nochol[9]=np.argmax(filtered_slowest_nochol_10_f[:np.where(filtered_slowest_nochol_10_x<corte)[0][-1]])


forces_slower_chol=np.zeros(20)

forces_slower_chol[0]=np.amax(filtered_slower_chol_1_f[:np.where(filtered_slower_chol_1_x<corte)[0][-1]])
forces_slower_chol[1]=np.amax(filtered_slower_chol_2_f[:np.where(filtered_slower_chol_2_x<corte)[0][-1]])
forces_slower_chol[2]=np.amax(filtered_slower_chol_3_f[:np.where(filtered_slower_chol_3_x<corte)[0][-1]])
forces_slower_chol[3]=np.amax(filtered_slower_chol_4_f[:np.where(filtered_slower_chol_4_x<corte)[0][-1]])
forces_slower_chol[4]=np.amax(filtered_slower_chol_5_f[:np.where(filtered_slower_chol_5_x<corte)[0][-1]])
forces_slower_chol[5]=np.amax(filtered_slower_chol_6_f[:np.where(filtered_slower_chol_6_x<corte)[0][-1]])
forces_slower_chol[6]=np.amax(filtered_slower_chol_7_f[:np.where(filtered_slower_chol_7_x<corte)[0][-1]])
forces_slower_chol[7]=np.amax(filtered_slower_chol_8_f[:np.where(filtered_slower_chol_8_x<corte)[0][-1]])
forces_slower_chol[8]=np.amax(filtered_slower_chol_9_f[:np.where(filtered_slower_chol_9_x<corte)[0][-1]])
forces_slower_chol[9]=np.amax(filtered_slower_chol_10_f[:np.where(filtered_slower_chol_10_x<corte)[0][-1]])

distance_slower_chol=np.zeros(20)

distance_slower_chol[0]=filtered_slower_chol_1_x[np.argmax(filtered_slower_chol_1_f[:np.where(filtered_slower_chol_1_x<corte)[0][-1]])]
distance_slower_chol[1]=filtered_slower_chol_2_x[np.argmax(filtered_slower_chol_2_f[:np.where(filtered_slower_chol_2_x<corte)[0][-1]])]
distance_slower_chol[2]=filtered_slower_chol_3_x[np.argmax(filtered_slower_chol_3_f[:np.where(filtered_slower_chol_3_x<corte)[0][-1]])]
distance_slower_chol[3]=filtered_slower_chol_4_x[np.argmax(filtered_slower_chol_4_f[:np.where(filtered_slower_chol_4_x<corte)[0][-1]])]
distance_slower_chol[4]=filtered_slower_chol_5_x[np.argmax(filtered_slower_chol_5_f[:np.where(filtered_slower_chol_5_x<corte)[0][-1]])]
distance_slower_chol[5]=filtered_slower_chol_6_x[np.argmax(filtered_slower_chol_6_f[:np.where(filtered_slower_chol_6_x<corte)[0][-1]])]
distance_slower_chol[6]=filtered_slower_chol_7_x[np.argmax(filtered_slower_chol_7_f[:np.where(filtered_slower_chol_7_x<corte)[0][-1]])]
distance_slower_chol[7]=filtered_slower_chol_8_x[np.argmax(filtered_slower_chol_8_f[:np.where(filtered_slower_chol_8_x<corte)[0][-1]])]
distance_slower_chol[8]=filtered_slower_chol_9_x[np.argmax(filtered_slower_chol_9_f[:np.where(filtered_slower_chol_9_x<corte)[0][-1]])]
distance_slower_chol[9]=filtered_slower_chol_10_x[np.argmax(filtered_slower_chol_10_f[:np.where(filtered_slower_chol_10_x<corte)[0][-1]])]

frames_slower_chol=np.zeros(20)

frames_slower_chol[0]=np.argmax(filtered_slower_chol_1_f[:np.where(filtered_slower_chol_1_x<corte)[0][-1]])
frames_slower_chol[1]=np.argmax(filtered_slower_chol_2_f[:np.where(filtered_slower_chol_2_x<corte)[0][-1]])
frames_slower_chol[2]=np.argmax(filtered_slower_chol_3_f[:np.where(filtered_slower_chol_3_x<corte)[0][-1]])
frames_slower_chol[3]=np.argmax(filtered_slower_chol_4_f[:np.where(filtered_slower_chol_4_x<corte)[0][-1]])
frames_slower_chol[4]=np.argmax(filtered_slower_chol_5_f[:np.where(filtered_slower_chol_5_x<corte)[0][-1]])
frames_slower_chol[5]=np.argmax(filtered_slower_chol_6_f[:np.where(filtered_slower_chol_6_x<corte)[0][-1]])
frames_slower_chol[6]=np.argmax(filtered_slower_chol_7_f[:np.where(filtered_slower_chol_7_x<corte)[0][-1]])
frames_slower_chol[7]=np.argmax(filtered_slower_chol_8_f[:np.where(filtered_slower_chol_8_x<corte)[0][-1]])
frames_slower_chol[8]=np.argmax(filtered_slower_chol_9_f[:np.where(filtered_slower_chol_9_x<corte)[0][-1]])
frames_slower_chol[9]=np.argmax(filtered_slower_chol_10_f[:np.where(filtered_slower_chol_10_x<corte)[0][-1]])


forces_slower_nochol=np.zeros(20)

forces_slower_nochol[0]=np.amax(filtered_slower_nochol_1_f[:np.where(filtered_slower_nochol_1_x<corte)[0][-1]])
forces_slower_nochol[1]=np.amax(filtered_slower_nochol_2_f[:np.where(filtered_slower_nochol_2_x<corte)[0][-1]])
forces_slower_nochol[2]=np.amax(filtered_slower_nochol_3_f[:np.where(filtered_slower_nochol_3_x<corte)[0][-1]])
forces_slower_nochol[3]=np.amax(filtered_slower_nochol_4_f[:np.where(filtered_slower_nochol_4_x<corte)[0][-1]])
forces_slower_nochol[4]=np.amax(filtered_slower_nochol_5_f[:np.where(filtered_slower_nochol_5_x<corte)[0][-1]])
forces_slower_nochol[5]=np.amax(filtered_slower_nochol_6_f[:np.where(filtered_slower_nochol_6_x<corte)[0][-1]])
forces_slower_nochol[6]=np.amax(filtered_slower_nochol_7_f[:np.where(filtered_slower_nochol_7_x<corte)[0][-1]])
forces_slower_nochol[7]=np.amax(filtered_slower_nochol_8_f[:np.where(filtered_slower_nochol_8_x<corte)[0][-1]])
forces_slower_nochol[8]=np.amax(filtered_slower_nochol_9_f[:np.where(filtered_slower_nochol_9_x<corte)[0][-1]])
forces_slower_nochol[9]=np.amax(filtered_slower_nochol_10_f[:np.where(filtered_slower_nochol_10_x<corte)[0][-1]])

distance_slower_nochol=np.zeros(20)

distance_slower_nochol[0]=filtered_slower_nochol_1_x[np.argmax(filtered_slower_nochol_1_f[:np.where(filtered_slower_nochol_1_x<corte)[0][-1]])]
distance_slower_nochol[1]=filtered_slower_nochol_2_x[np.argmax(filtered_slower_nochol_2_f[:np.where(filtered_slower_nochol_2_x<corte)[0][-1]])]
distance_slower_nochol[2]=filtered_slower_nochol_3_x[np.argmax(filtered_slower_nochol_3_f[:np.where(filtered_slower_nochol_3_x<corte)[0][-1]])]
distance_slower_nochol[3]=filtered_slower_nochol_4_x[np.argmax(filtered_slower_nochol_4_f[:np.where(filtered_slower_nochol_4_x<corte)[0][-1]])]
distance_slower_nochol[4]=filtered_slower_nochol_5_x[np.argmax(filtered_slower_nochol_5_f[:np.where(filtered_slower_nochol_5_x<corte)[0][-1]])]
distance_slower_nochol[5]=filtered_slower_nochol_6_x[np.argmax(filtered_slower_nochol_6_f[:np.where(filtered_slower_nochol_6_x<corte)[0][-1]])]
distance_slower_nochol[6]=filtered_slower_nochol_7_x[np.argmax(filtered_slower_nochol_7_f[:np.where(filtered_slower_nochol_7_x<corte)[0][-1]])]
distance_slower_nochol[7]=filtered_slower_nochol_8_x[np.argmax(filtered_slower_nochol_8_f[:np.where(filtered_slower_nochol_8_x<corte)[0][-1]])]
distance_slower_nochol[8]=filtered_slower_nochol_9_x[np.argmax(filtered_slower_nochol_9_f[:np.where(filtered_slower_nochol_9_x<corte)[0][-1]])]
distance_slower_nochol[9]=filtered_slower_nochol_10_x[np.argmax(filtered_slower_nochol_10_f[:np.where(filtered_slower_nochol_10_x<corte)[0][-1]])]

frames_slower_nochol=np.zeros(20)

frames_slower_nochol[0]=np.argmax(filtered_slower_nochol_1_f[:np.where(filtered_slower_nochol_1_x<corte)[0][-1]])
frames_slower_nochol[1]=np.argmax(filtered_slower_nochol_2_f[:np.where(filtered_slower_nochol_2_x<corte)[0][-1]])
frames_slower_nochol[2]=np.argmax(filtered_slower_nochol_3_f[:np.where(filtered_slower_nochol_3_x<corte)[0][-1]])
frames_slower_nochol[3]=np.argmax(filtered_slower_nochol_4_f[:np.where(filtered_slower_nochol_4_x<corte)[0][-1]])
frames_slower_nochol[4]=np.argmax(filtered_slower_nochol_5_f[:np.where(filtered_slower_nochol_5_x<corte)[0][-1]])
frames_slower_nochol[5]=np.argmax(filtered_slower_nochol_6_f[:np.where(filtered_slower_nochol_6_x<corte)[0][-1]])
frames_slower_nochol[6]=np.argmax(filtered_slower_nochol_7_f[:np.where(filtered_slower_nochol_7_x<corte)[0][-1]])
frames_slower_nochol[7]=np.argmax(filtered_slower_nochol_8_f[:np.where(filtered_slower_nochol_8_x<corte)[0][-1]])
frames_slower_nochol[8]=np.argmax(filtered_slower_nochol_9_f[:np.where(filtered_slower_nochol_9_x<corte)[0][-1]])
frames_slower_nochol[9]=np.argmax(filtered_slower_nochol_10_f[:np.where(filtered_slower_nochol_10_x<corte)[0][-1]])



forces_glacial_chol[10]=np.amax(filtered_glacial_chol_11_f[:np.where(filtered_glacial_chol_11_x<corte)[0][-1]])
forces_glacial_chol[11]=np.amax(filtered_glacial_chol_12_f[:np.where(filtered_glacial_chol_12_x<corte)[0][-1]])
forces_glacial_chol[12]=np.amax(filtered_glacial_chol_13_f[:np.where(filtered_glacial_chol_13_x<corte)[0][-1]])
forces_glacial_chol[13]=np.amax(filtered_glacial_chol_14_f[:np.where(filtered_glacial_chol_14_x<corte)[0][-1]])
forces_glacial_chol[14]=np.amax(filtered_glacial_chol_15_f[:np.where(filtered_glacial_chol_15_x<corte)[0][-1]])
forces_glacial_chol[15]=np.amax(filtered_glacial_chol_16_f[:np.where(filtered_glacial_chol_16_x<corte)[0][-1]])
forces_glacial_chol[16]=np.amax(filtered_glacial_chol_17_f[:np.where(filtered_glacial_chol_17_x<corte)[0][-1]])
forces_glacial_chol[17]=np.amax(filtered_glacial_chol_18_f[:np.where(filtered_glacial_chol_18_x<corte)[0][-1]])
forces_glacial_chol[18]=np.amax(filtered_glacial_chol_19_f[:np.where(filtered_glacial_chol_19_x<corte)[0][-1]])
forces_glacial_chol[19]=np.amax(filtered_glacial_chol_20_f[:np.where(filtered_glacial_chol_20_x<corte)[0][-1]])

distance_glacial_chol[10]=filtered_glacial_chol_11_x[np.argmax(filtered_glacial_chol_11_f[:np.where(filtered_glacial_chol_11_x<corte)[0][-1]])]
distance_glacial_chol[11]=filtered_glacial_chol_12_x[np.argmax(filtered_glacial_chol_12_f[:np.where(filtered_glacial_chol_12_x<corte)[0][-1]])]
distance_glacial_chol[12]=filtered_glacial_chol_13_x[np.argmax(filtered_glacial_chol_13_f[:np.where(filtered_glacial_chol_13_x<corte)[0][-1]])]
distance_glacial_chol[13]=filtered_glacial_chol_14_x[np.argmax(filtered_glacial_chol_14_f[:np.where(filtered_glacial_chol_14_x<corte)[0][-1]])]
distance_glacial_chol[14]=filtered_glacial_chol_15_x[np.argmax(filtered_glacial_chol_15_f[:np.where(filtered_glacial_chol_15_x<corte)[0][-1]])]
distance_glacial_chol[15]=filtered_glacial_chol_16_x[np.argmax(filtered_glacial_chol_16_f[:np.where(filtered_glacial_chol_16_x<corte)[0][-1]])]
distance_glacial_chol[16]=filtered_glacial_chol_17_x[np.argmax(filtered_glacial_chol_17_f[:np.where(filtered_glacial_chol_17_x<corte)[0][-1]])]
distance_glacial_chol[17]=filtered_glacial_chol_18_x[np.argmax(filtered_glacial_chol_18_f[:np.where(filtered_glacial_chol_18_x<corte)[0][-1]])]
distance_glacial_chol[18]=filtered_glacial_chol_19_x[np.argmax(filtered_glacial_chol_19_f[:np.where(filtered_glacial_chol_19_x<corte)[0][-1]])]
distance_glacial_chol[19]=filtered_glacial_chol_20_x[np.argmax(filtered_glacial_chol_20_f[:np.where(filtered_glacial_chol_20_x<corte)[0][-1]])]

frames_glacial_chol[10]=np.argmax(filtered_glacial_chol_11_f[:np.where(filtered_glacial_chol_11_x<corte)[0][-1]])
frames_glacial_chol[11]=np.argmax(filtered_glacial_chol_12_f[:np.where(filtered_glacial_chol_12_x<corte)[0][-1]])
frames_glacial_chol[12]=np.argmax(filtered_glacial_chol_13_f[:np.where(filtered_glacial_chol_13_x<corte)[0][-1]])
frames_glacial_chol[13]=np.argmax(filtered_glacial_chol_14_f[:np.where(filtered_glacial_chol_14_x<corte)[0][-1]])
frames_glacial_chol[14]=np.argmax(filtered_glacial_chol_15_f[:np.where(filtered_glacial_chol_15_x<corte)[0][-1]])
frames_glacial_chol[15]=np.argmax(filtered_glacial_chol_16_f[:np.where(filtered_glacial_chol_16_x<corte)[0][-1]])
frames_glacial_chol[16]=np.argmax(filtered_glacial_chol_17_f[:np.where(filtered_glacial_chol_17_x<corte)[0][-1]])
frames_glacial_chol[17]=np.argmax(filtered_glacial_chol_18_f[:np.where(filtered_glacial_chol_18_x<corte)[0][-1]])
frames_glacial_chol[18]=np.argmax(filtered_glacial_chol_19_f[:np.where(filtered_glacial_chol_19_x<corte)[0][-1]])
frames_glacial_chol[19]=np.argmax(filtered_glacial_chol_20_f[:np.where(filtered_glacial_chol_20_x<corte)[0][-1]])


forces_glacial_nochol[10]=np.amax(filtered_glacial_nochol_11_f[:np.where(filtered_glacial_nochol_11_x<corte)[0][-1]])
forces_glacial_nochol[11]=np.amax(filtered_glacial_nochol_12_f[:np.where(filtered_glacial_nochol_12_x<corte)[0][-1]])
forces_glacial_nochol[12]=np.amax(filtered_glacial_nochol_13_f[:np.where(filtered_glacial_nochol_13_x<corte)[0][-1]])
forces_glacial_nochol[13]=np.amax(filtered_glacial_nochol_14_f[:np.where(filtered_glacial_nochol_14_x<corte)[0][-1]])
forces_glacial_nochol[14]=np.amax(filtered_glacial_nochol_15_f[:np.where(filtered_glacial_nochol_15_x<corte)[0][-1]])
forces_glacial_nochol[15]=np.amax(filtered_glacial_nochol_16_f[:np.where(filtered_glacial_nochol_16_x<corte)[0][-1]])
forces_glacial_nochol[16]=np.amax(filtered_glacial_nochol_17_f[:np.where(filtered_glacial_nochol_17_x<corte)[0][-1]])
forces_glacial_nochol[17]=np.amax(filtered_glacial_nochol_18_f[:np.where(filtered_glacial_nochol_18_x<corte)[0][-1]])
forces_glacial_nochol[18]=np.amax(filtered_glacial_nochol_19_f[:np.where(filtered_glacial_nochol_19_x<corte)[0][-1]])
forces_glacial_nochol[19]=np.amax(filtered_glacial_nochol_20_f[:np.where(filtered_glacial_nochol_20_x<corte)[0][-1]])

distance_glacial_nochol[10]=filtered_glacial_nochol_11_x[np.argmax(filtered_glacial_nochol_11_f[:np.where(filtered_glacial_nochol_11_x<corte)[0][-1]])]
distance_glacial_nochol[11]=filtered_glacial_nochol_12_x[np.argmax(filtered_glacial_nochol_12_f[:np.where(filtered_glacial_nochol_12_x<corte)[0][-1]])]
distance_glacial_nochol[12]=filtered_glacial_nochol_13_x[np.argmax(filtered_glacial_nochol_13_f[:np.where(filtered_glacial_nochol_13_x<corte)[0][-1]])]
distance_glacial_nochol[13]=filtered_glacial_nochol_14_x[np.argmax(filtered_glacial_nochol_14_f[:np.where(filtered_glacial_nochol_14_x<corte)[0][-1]])]
distance_glacial_nochol[14]=filtered_glacial_nochol_15_x[np.argmax(filtered_glacial_nochol_15_f[:np.where(filtered_glacial_nochol_15_x<corte)[0][-1]])]
distance_glacial_nochol[15]=filtered_glacial_nochol_16_x[np.argmax(filtered_glacial_nochol_16_f[:np.where(filtered_glacial_nochol_16_x<corte)[0][-1]])]
distance_glacial_nochol[16]=filtered_glacial_nochol_17_x[np.argmax(filtered_glacial_nochol_17_f[:np.where(filtered_glacial_nochol_17_x<corte)[0][-1]])]
distance_glacial_nochol[17]=filtered_glacial_nochol_18_x[np.argmax(filtered_glacial_nochol_18_f[:np.where(filtered_glacial_nochol_18_x<corte)[0][-1]])]
distance_glacial_nochol[18]=filtered_glacial_nochol_19_x[np.argmax(filtered_glacial_nochol_19_f[:np.where(filtered_glacial_nochol_19_x<corte)[0][-1]])]
distance_glacial_nochol[19]=filtered_glacial_nochol_20_x[np.argmax(filtered_glacial_nochol_20_f[:np.where(filtered_glacial_nochol_20_x<corte)[0][-1]])]

frames_glacial_nochol[10]=np.argmax(filtered_glacial_nochol_11_f[:np.where(filtered_glacial_nochol_11_x<corte)[0][-1]])
frames_glacial_nochol[11]=np.argmax(filtered_glacial_nochol_12_f[:np.where(filtered_glacial_nochol_12_x<corte)[0][-1]])
frames_glacial_nochol[12]=np.argmax(filtered_glacial_nochol_13_f[:np.where(filtered_glacial_nochol_13_x<corte)[0][-1]])
frames_glacial_nochol[13]=np.argmax(filtered_glacial_nochol_14_f[:np.where(filtered_glacial_nochol_14_x<corte)[0][-1]])
frames_glacial_nochol[14]=np.argmax(filtered_glacial_nochol_15_f[:np.where(filtered_glacial_nochol_15_x<corte)[0][-1]])
frames_glacial_nochol[15]=np.argmax(filtered_glacial_nochol_16_f[:np.where(filtered_glacial_nochol_16_x<corte)[0][-1]])
frames_glacial_nochol[16]=np.argmax(filtered_glacial_nochol_17_f[:np.where(filtered_glacial_nochol_17_x<corte)[0][-1]])
frames_glacial_nochol[17]=np.argmax(filtered_glacial_nochol_18_f[:np.where(filtered_glacial_nochol_18_x<corte)[0][-1]])
frames_glacial_nochol[18]=np.argmax(filtered_glacial_nochol_19_f[:np.where(filtered_glacial_nochol_19_x<corte)[0][-1]])
frames_glacial_nochol[19]=np.argmax(filtered_glacial_nochol_20_f[:np.where(filtered_glacial_nochol_20_x<corte)[0][-1]])


forces_slowest_chol[10]=np.amax(filtered_slowest_chol_11_f[:np.where(filtered_slowest_chol_11_x<corte)[0][-1]])
forces_slowest_chol[11]=np.amax(filtered_slowest_chol_12_f[:np.where(filtered_slowest_chol_12_x<corte)[0][-1]])
forces_slowest_chol[12]=np.amax(filtered_slowest_chol_13_f[:np.where(filtered_slowest_chol_13_x<corte)[0][-1]])
forces_slowest_chol[13]=np.amax(filtered_slowest_chol_14_f[:np.where(filtered_slowest_chol_14_x<corte)[0][-1]])
forces_slowest_chol[14]=np.amax(filtered_slowest_chol_15_f[:np.where(filtered_slowest_chol_15_x<corte)[0][-1]])
forces_slowest_chol[15]=np.amax(filtered_slowest_chol_16_f[:np.where(filtered_slowest_chol_16_x<corte)[0][-1]])
forces_slowest_chol[16]=np.amax(filtered_slowest_chol_17_f[:np.where(filtered_slowest_chol_17_x<corte)[0][-1]])
forces_slowest_chol[17]=np.amax(filtered_slowest_chol_18_f[:np.where(filtered_slowest_chol_18_x<corte)[0][-1]])
forces_slowest_chol[18]=np.amax(filtered_slowest_chol_19_f[:np.where(filtered_slowest_chol_19_x<corte)[0][-1]])
forces_slowest_chol[19]=np.amax(filtered_slowest_chol_20_f[:np.where(filtered_slowest_chol_20_x<corte)[0][-1]])

distance_slowest_chol[10]=filtered_slowest_chol_11_x[np.argmax(filtered_slowest_chol_11_f[:np.where(filtered_slowest_chol_11_x<corte)[0][-1]])]
distance_slowest_chol[11]=filtered_slowest_chol_12_x[np.argmax(filtered_slowest_chol_12_f[:np.where(filtered_slowest_chol_12_x<corte)[0][-1]])]
distance_slowest_chol[12]=filtered_slowest_chol_13_x[np.argmax(filtered_slowest_chol_13_f[:np.where(filtered_slowest_chol_13_x<corte)[0][-1]])]
distance_slowest_chol[13]=filtered_slowest_chol_14_x[np.argmax(filtered_slowest_chol_14_f[:np.where(filtered_slowest_chol_14_x<corte)[0][-1]])]
distance_slowest_chol[14]=filtered_slowest_chol_15_x[np.argmax(filtered_slowest_chol_15_f[:np.where(filtered_slowest_chol_15_x<corte)[0][-1]])]
distance_slowest_chol[15]=filtered_slowest_chol_16_x[np.argmax(filtered_slowest_chol_16_f[:np.where(filtered_slowest_chol_16_x<corte)[0][-1]])]
distance_slowest_chol[16]=filtered_slowest_chol_17_x[np.argmax(filtered_slowest_chol_17_f[:np.where(filtered_slowest_chol_17_x<corte)[0][-1]])]
distance_slowest_chol[17]=filtered_slowest_chol_18_x[np.argmax(filtered_slowest_chol_18_f[:np.where(filtered_slowest_chol_18_x<corte)[0][-1]])]
distance_slowest_chol[18]=filtered_slowest_chol_19_x[np.argmax(filtered_slowest_chol_19_f[:np.where(filtered_slowest_chol_19_x<corte)[0][-1]])]
distance_slowest_chol[19]=filtered_slowest_chol_20_x[np.argmax(filtered_slowest_chol_20_f[:np.where(filtered_slowest_chol_20_x<corte)[0][-1]])]

frames_slowest_chol[10]=np.argmax(filtered_slowest_chol_11_f[:np.where(filtered_slowest_chol_11_x<corte)[0][-1]])
frames_slowest_chol[11]=np.argmax(filtered_slowest_chol_12_f[:np.where(filtered_slowest_chol_12_x<corte)[0][-1]])
frames_slowest_chol[12]=np.argmax(filtered_slowest_chol_13_f[:np.where(filtered_slowest_chol_13_x<corte)[0][-1]])
frames_slowest_chol[13]=np.argmax(filtered_slowest_chol_14_f[:np.where(filtered_slowest_chol_14_x<corte)[0][-1]])
frames_slowest_chol[14]=np.argmax(filtered_slowest_chol_15_f[:np.where(filtered_slowest_chol_15_x<corte)[0][-1]])
frames_slowest_chol[15]=np.argmax(filtered_slowest_chol_16_f[:np.where(filtered_slowest_chol_16_x<corte)[0][-1]])
frames_slowest_chol[16]=np.argmax(filtered_slowest_chol_17_f[:np.where(filtered_slowest_chol_17_x<corte)[0][-1]])
frames_slowest_chol[17]=np.argmax(filtered_slowest_chol_18_f[:np.where(filtered_slowest_chol_18_x<corte)[0][-1]])
frames_slowest_chol[18]=np.argmax(filtered_slowest_chol_19_f[:np.where(filtered_slowest_chol_19_x<corte)[0][-1]])
frames_slowest_chol[19]=np.argmax(filtered_slowest_chol_20_f[:np.where(filtered_slowest_chol_20_x<corte)[0][-1]])


forces_slowest_nochol[10]=np.amax(filtered_slowest_nochol_11_f[:np.where(filtered_slowest_nochol_11_x<corte)[0][-1]])
forces_slowest_nochol[11]=np.amax(filtered_slowest_nochol_12_f[:np.where(filtered_slowest_nochol_12_x<corte)[0][-1]])
forces_slowest_nochol[12]=np.amax(filtered_slowest_nochol_13_f[:np.where(filtered_slowest_nochol_13_x<corte)[0][-1]])
forces_slowest_nochol[13]=np.amax(filtered_slowest_nochol_14_f[:np.where(filtered_slowest_nochol_14_x<corte)[0][-1]])
forces_slowest_nochol[14]=np.amax(filtered_slowest_nochol_15_f[:np.where(filtered_slowest_nochol_15_x<corte)[0][-1]])
forces_slowest_nochol[15]=np.amax(filtered_slowest_nochol_16_f[:np.where(filtered_slowest_nochol_16_x<corte)[0][-1]])
forces_slowest_nochol[16]=np.amax(filtered_slowest_nochol_17_f[:np.where(filtered_slowest_nochol_17_x<corte)[0][-1]])
forces_slowest_nochol[17]=np.amax(filtered_slowest_nochol_18_f[:np.where(filtered_slowest_nochol_18_x<corte)[0][-1]])
forces_slowest_nochol[18]=np.amax(filtered_slowest_nochol_19_f[:np.where(filtered_slowest_nochol_19_x<corte)[0][-1]])
forces_slowest_nochol[19]=np.amax(filtered_slowest_nochol_20_f[:np.where(filtered_slowest_nochol_20_x<corte)[0][-1]])

distance_slowest_nochol[10]=filtered_slowest_nochol_11_x[np.argmax(filtered_slowest_nochol_11_f[:np.where(filtered_slowest_nochol_11_x<corte)[0][-1]])]
distance_slowest_nochol[11]=filtered_slowest_nochol_12_x[np.argmax(filtered_slowest_nochol_12_f[:np.where(filtered_slowest_nochol_12_x<corte)[0][-1]])]
distance_slowest_nochol[12]=filtered_slowest_nochol_13_x[np.argmax(filtered_slowest_nochol_13_f[:np.where(filtered_slowest_nochol_13_x<corte)[0][-1]])]
distance_slowest_nochol[13]=filtered_slowest_nochol_14_x[np.argmax(filtered_slowest_nochol_14_f[:np.where(filtered_slowest_nochol_14_x<corte)[0][-1]])]
distance_slowest_nochol[14]=filtered_slowest_nochol_15_x[np.argmax(filtered_slowest_nochol_15_f[:np.where(filtered_slowest_nochol_15_x<corte)[0][-1]])]
distance_slowest_nochol[15]=filtered_slowest_nochol_16_x[np.argmax(filtered_slowest_nochol_16_f[:np.where(filtered_slowest_nochol_16_x<corte)[0][-1]])]
distance_slowest_nochol[16]=filtered_slowest_nochol_17_x[np.argmax(filtered_slowest_nochol_17_f[:np.where(filtered_slowest_nochol_17_x<corte)[0][-1]])]
distance_slowest_nochol[17]=filtered_slowest_nochol_18_x[np.argmax(filtered_slowest_nochol_18_f[:np.where(filtered_slowest_nochol_18_x<corte)[0][-1]])]
distance_slowest_nochol[18]=filtered_slowest_nochol_19_x[np.argmax(filtered_slowest_nochol_19_f[:np.where(filtered_slowest_nochol_19_x<corte)[0][-1]])]
distance_slowest_nochol[19]=filtered_slowest_nochol_20_x[np.argmax(filtered_slowest_nochol_20_f[:np.where(filtered_slowest_nochol_20_x<corte)[0][-1]])]

frames_slowest_nochol[10]=np.argmax(filtered_slowest_nochol_11_f[:np.where(filtered_slowest_nochol_11_x<corte)[0][-1]])
frames_slowest_nochol[11]=np.argmax(filtered_slowest_nochol_12_f[:np.where(filtered_slowest_nochol_12_x<corte)[0][-1]])
frames_slowest_nochol[12]=np.argmax(filtered_slowest_nochol_13_f[:np.where(filtered_slowest_nochol_13_x<corte)[0][-1]])
frames_slowest_nochol[13]=np.argmax(filtered_slowest_nochol_14_f[:np.where(filtered_slowest_nochol_14_x<corte)[0][-1]])
frames_slowest_nochol[14]=np.argmax(filtered_slowest_nochol_15_f[:np.where(filtered_slowest_nochol_15_x<corte)[0][-1]])
frames_slowest_nochol[15]=np.argmax(filtered_slowest_nochol_16_f[:np.where(filtered_slowest_nochol_16_x<corte)[0][-1]])
frames_slowest_nochol[16]=np.argmax(filtered_slowest_nochol_17_f[:np.where(filtered_slowest_nochol_17_x<corte)[0][-1]])
frames_slowest_nochol[17]=np.argmax(filtered_slowest_nochol_18_f[:np.where(filtered_slowest_nochol_18_x<corte)[0][-1]])
frames_slowest_nochol[18]=np.argmax(filtered_slowest_nochol_19_f[:np.where(filtered_slowest_nochol_19_x<corte)[0][-1]])
frames_slowest_nochol[19]=np.argmax(filtered_slowest_nochol_20_f[:np.where(filtered_slowest_nochol_20_x<corte)[0][-1]])


forces_slower_chol[10]=np.amax(filtered_slower_chol_11_f[:np.where(filtered_slower_chol_11_x<corte)[0][-1]])
forces_slower_chol[11]=np.amax(filtered_slower_chol_12_f[:np.where(filtered_slower_chol_12_x<corte)[0][-1]])
forces_slower_chol[12]=np.amax(filtered_slower_chol_13_f[:np.where(filtered_slower_chol_13_x<corte)[0][-1]])
forces_slower_chol[13]=np.amax(filtered_slower_chol_14_f[:np.where(filtered_slower_chol_14_x<corte)[0][-1]])
forces_slower_chol[14]=np.amax(filtered_slower_chol_15_f[:np.where(filtered_slower_chol_15_x<corte)[0][-1]])
forces_slower_chol[15]=np.amax(filtered_slower_chol_16_f[:np.where(filtered_slower_chol_16_x<corte)[0][-1]])
forces_slower_chol[16]=np.amax(filtered_slower_chol_17_f[:np.where(filtered_slower_chol_17_x<corte)[0][-1]])
forces_slower_chol[17]=np.amax(filtered_slower_chol_18_f[:np.where(filtered_slower_chol_18_x<corte)[0][-1]])
forces_slower_chol[18]=np.amax(filtered_slower_chol_19_f[:np.where(filtered_slower_chol_19_x<corte)[0][-1]])
forces_slower_chol[19]=np.amax(filtered_slower_chol_20_f[:np.where(filtered_slower_chol_20_x<corte)[0][-1]])

distance_slower_chol[10]=filtered_slower_chol_11_x[np.argmax(filtered_slower_chol_11_f[:np.where(filtered_slower_chol_11_x<corte)[0][-1]])]
distance_slower_chol[11]=filtered_slower_chol_12_x[np.argmax(filtered_slower_chol_12_f[:np.where(filtered_slower_chol_12_x<corte)[0][-1]])]
distance_slower_chol[12]=filtered_slower_chol_13_x[np.argmax(filtered_slower_chol_13_f[:np.where(filtered_slower_chol_13_x<corte)[0][-1]])]
distance_slower_chol[13]=filtered_slower_chol_14_x[np.argmax(filtered_slower_chol_14_f[:np.where(filtered_slower_chol_14_x<corte)[0][-1]])]
distance_slower_chol[14]=filtered_slower_chol_15_x[np.argmax(filtered_slower_chol_15_f[:np.where(filtered_slower_chol_15_x<corte)[0][-1]])]
distance_slower_chol[15]=filtered_slower_chol_16_x[np.argmax(filtered_slower_chol_16_f[:np.where(filtered_slower_chol_16_x<corte)[0][-1]])]
distance_slower_chol[16]=filtered_slower_chol_17_x[np.argmax(filtered_slower_chol_17_f[:np.where(filtered_slower_chol_17_x<corte)[0][-1]])]
distance_slower_chol[17]=filtered_slower_chol_18_x[np.argmax(filtered_slower_chol_18_f[:np.where(filtered_slower_chol_18_x<corte)[0][-1]])]
distance_slower_chol[18]=filtered_slower_chol_19_x[np.argmax(filtered_slower_chol_19_f[:np.where(filtered_slower_chol_19_x<corte)[0][-1]])]
distance_slower_chol[19]=filtered_slower_chol_20_x[np.argmax(filtered_slower_chol_20_f[:np.where(filtered_slower_chol_20_x<corte)[0][-1]])]

frames_slower_chol[10]=np.argmax(filtered_slower_chol_11_f[:np.where(filtered_slower_chol_11_x<corte)[0][-1]])
frames_slower_chol[11]=np.argmax(filtered_slower_chol_12_f[:np.where(filtered_slower_chol_12_x<corte)[0][-1]])
frames_slower_chol[12]=np.argmax(filtered_slower_chol_13_f[:np.where(filtered_slower_chol_13_x<corte)[0][-1]])
frames_slower_chol[13]=np.argmax(filtered_slower_chol_14_f[:np.where(filtered_slower_chol_14_x<corte)[0][-1]])
frames_slower_chol[14]=np.argmax(filtered_slower_chol_15_f[:np.where(filtered_slower_chol_15_x<corte)[0][-1]])
frames_slower_chol[15]=np.argmax(filtered_slower_chol_16_f[:np.where(filtered_slower_chol_16_x<corte)[0][-1]])
frames_slower_chol[16]=np.argmax(filtered_slower_chol_17_f[:np.where(filtered_slower_chol_17_x<corte)[0][-1]])
frames_slower_chol[17]=np.argmax(filtered_slower_chol_18_f[:np.where(filtered_slower_chol_18_x<corte)[0][-1]])
frames_slower_chol[18]=np.argmax(filtered_slower_chol_19_f[:np.where(filtered_slower_chol_19_x<corte)[0][-1]])
frames_slower_chol[19]=np.argmax(filtered_slower_chol_20_f[:np.where(filtered_slower_chol_20_x<corte)[0][-1]])


forces_slower_nochol[10]=np.amax(filtered_slower_nochol_11_f[:np.where(filtered_slower_nochol_11_x<corte)[0][-1]])
forces_slower_nochol[11]=np.amax(filtered_slower_nochol_12_f[:np.where(filtered_slower_nochol_12_x<corte)[0][-1]])
forces_slower_nochol[12]=np.amax(filtered_slower_nochol_13_f[:np.where(filtered_slower_nochol_13_x<corte)[0][-1]])
forces_slower_nochol[13]=np.amax(filtered_slower_nochol_14_f[:np.where(filtered_slower_nochol_14_x<corte)[0][-1]])
forces_slower_nochol[14]=np.amax(filtered_slower_nochol_15_f[:np.where(filtered_slower_nochol_15_x<corte)[0][-1]])
forces_slower_nochol[15]=np.amax(filtered_slower_nochol_16_f[:np.where(filtered_slower_nochol_16_x<corte)[0][-1]])
forces_slower_nochol[16]=np.amax(filtered_slower_nochol_17_f[:np.where(filtered_slower_nochol_17_x<corte)[0][-1]])
forces_slower_nochol[17]=np.amax(filtered_slower_nochol_18_f[:np.where(filtered_slower_nochol_18_x<corte)[0][-1]])
forces_slower_nochol[18]=np.amax(filtered_slower_nochol_19_f[:np.where(filtered_slower_nochol_19_x<corte)[0][-1]])
forces_slower_nochol[19]=np.amax(filtered_slower_nochol_20_f[:np.where(filtered_slower_nochol_20_x<corte)[0][-1]])

distance_slower_nochol[10]=filtered_slower_nochol_11_x[np.argmax(filtered_slower_nochol_11_f[:np.where(filtered_slower_nochol_11_x<corte)[0][-1]])]
distance_slower_nochol[11]=filtered_slower_nochol_12_x[np.argmax(filtered_slower_nochol_12_f[:np.where(filtered_slower_nochol_12_x<corte)[0][-1]])]
distance_slower_nochol[12]=filtered_slower_nochol_13_x[np.argmax(filtered_slower_nochol_13_f[:np.where(filtered_slower_nochol_13_x<corte)[0][-1]])]
distance_slower_nochol[13]=filtered_slower_nochol_14_x[np.argmax(filtered_slower_nochol_14_f[:np.where(filtered_slower_nochol_14_x<corte)[0][-1]])]
distance_slower_nochol[14]=filtered_slower_nochol_15_x[np.argmax(filtered_slower_nochol_15_f[:np.where(filtered_slower_nochol_15_x<corte)[0][-1]])]
distance_slower_nochol[15]=filtered_slower_nochol_16_x[np.argmax(filtered_slower_nochol_16_f[:np.where(filtered_slower_nochol_16_x<corte)[0][-1]])]
distance_slower_nochol[16]=filtered_slower_nochol_17_x[np.argmax(filtered_slower_nochol_17_f[:np.where(filtered_slower_nochol_17_x<corte)[0][-1]])]
distance_slower_nochol[17]=filtered_slower_nochol_18_x[np.argmax(filtered_slower_nochol_18_f[:np.where(filtered_slower_nochol_18_x<corte)[0][-1]])]
distance_slower_nochol[18]=filtered_slower_nochol_19_x[np.argmax(filtered_slower_nochol_19_f[:np.where(filtered_slower_nochol_19_x<corte)[0][-1]])]
distance_slower_nochol[19]=filtered_slower_nochol_20_x[np.argmax(filtered_slower_nochol_20_f[:np.where(filtered_slower_nochol_20_x<corte)[0][-1]])]

frames_slower_nochol[10]=np.argmax(filtered_slower_nochol_11_f[:np.where(filtered_slower_nochol_11_x<corte)[0][-1]])
frames_slower_nochol[11]=np.argmax(filtered_slower_nochol_12_f[:np.where(filtered_slower_nochol_12_x<corte)[0][-1]])
frames_slower_nochol[12]=np.argmax(filtered_slower_nochol_13_f[:np.where(filtered_slower_nochol_13_x<corte)[0][-1]])
frames_slower_nochol[13]=np.argmax(filtered_slower_nochol_14_f[:np.where(filtered_slower_nochol_14_x<corte)[0][-1]])
frames_slower_nochol[14]=np.argmax(filtered_slower_nochol_15_f[:np.where(filtered_slower_nochol_15_x<corte)[0][-1]])
frames_slower_nochol[15]=np.argmax(filtered_slower_nochol_16_f[:np.where(filtered_slower_nochol_16_x<corte)[0][-1]])
frames_slower_nochol[16]=np.argmax(filtered_slower_nochol_17_f[:np.where(filtered_slower_nochol_17_x<corte)[0][-1]])
frames_slower_nochol[17]=np.argmax(filtered_slower_nochol_18_f[:np.where(filtered_slower_nochol_18_x<corte)[0][-1]])
frames_slower_nochol[18]=np.argmax(filtered_slower_nochol_19_f[:np.where(filtered_slower_nochol_19_x<corte)[0][-1]])
frames_slower_nochol[19]=np.argmax(filtered_slower_nochol_20_f[:np.where(filtered_slower_nochol_20_x<corte)[0][-1]])


det_times_chol[0]=np.average(0.0001*frames_glacial_chol)
det_times_nochol[0]=np.average(0.0001*frames_glacial_nochol)
det_times_chol_stderr[0]=error_estandar(0.0001*frames_glacial_chol)
det_times_nochol_stderr[0]=error_estandar(0.0001*frames_glacial_nochol)
det_force_chol[0]=np.average(forces_glacial_chol)
det_force_nochol[0]=np.average(forces_glacial_nochol)
det_force_chol_stderr[0]=error_estandar(forces_glacial_chol)
det_force_nochol_stderr[0]=error_estandar(forces_glacial_nochol)
det_distance_chol[0]=np.average(distance_glacial_chol)
det_distance_nochol[0]=np.average(distance_glacial_nochol)
det_distance_chol_stderr[0]=error_estandar(distance_glacial_chol)
det_distance_nochol_stderr[0]=error_estandar(distance_glacial_nochol)



det_times_chol[1]=np.average(0.0001*frames_slowest_chol)
det_times_nochol[1]=np.average(0.0001*frames_slowest_nochol)
det_times_chol_stderr[1]=error_estandar(0.0001*frames_slowest_chol)
det_times_nochol_stderr[1]=error_estandar(0.0001*frames_slowest_nochol)
det_force_chol[1]=np.average(forces_slowest_chol)
det_force_nochol[1]=np.average(forces_slowest_nochol)
det_force_chol_stderr[1]=error_estandar(forces_slowest_chol)
det_force_nochol_stderr[1]=error_estandar(forces_slowest_nochol)
det_distance_chol[1]=np.average(distance_slowest_chol)
det_distance_nochol[1]=np.average(distance_slowest_nochol)
det_distance_chol_stderr[1]=error_estandar(distance_slowest_chol)
det_distance_nochol_stderr[1]=error_estandar(distance_slowest_nochol)


det_times_chol[2]=np.average(0.0001*frames_slower_chol)
det_times_nochol[2]=np.average(0.0001*frames_slower_nochol)
det_times_chol_stderr[2]=error_estandar(0.0001*frames_slower_chol)
det_times_nochol_stderr[2]=error_estandar(0.0001*frames_slower_nochol)
det_force_chol[2]=np.average(forces_slower_chol)
det_force_nochol[2]=np.average(forces_slower_nochol)
det_force_chol_stderr[2]=error_estandar(forces_slower_chol)
det_force_nochol_stderr[2]=error_estandar(forces_slower_nochol)
det_distance_chol[2]=np.average(distance_slower_chol)
det_distance_nochol[2]=np.average(distance_slower_nochol)
det_distance_chol_stderr[2]=error_estandar(distance_slower_chol)
det_distance_nochol_stderr[2]=error_estandar(distance_slower_nochol)



kJnmtopN=1.661


def func(x, A, B):
    return A+B*np.log(x)
    

popt_chol, pcov_chol = curve_fit(func, np.concatenate((np.repeat(0.004,20),np.repeat(0.02,20),np.repeat(0.1,20))), kJnmtopN*np.concatenate((forces_glacial_chol,forces_slowest_chol,forces_slower_chol)))
popt_PSM, pcov_PSM = curve_fit(func, np.concatenate((np.repeat(0.004,20),np.repeat(0.02,20),np.repeat(0.1,20))), kJnmtopN*np.concatenate((forces_glacial_nochol,forces_slowest_nochol,forces_slower_nochol)))
#perr_chol = np.sqrt(np.diag(pcov_chol))/3.16227766017  # one standard deviation errors on the parameters / sqrt(10)?
#perr_PSM = np.sqrt(np.diag(pcov_PSM))/3.16227766017
perr_chol = np.sqrt(np.diag(pcov_chol))
perr_PSM = np.sqrt(np.diag(pcov_PSM))

plt.figure(figsize=(12,8))

plt.errorbar(rates,kJnmtopN*np.asarray(det_force_chol),yerr=kJnmtopN*np.asarray(det_force_chol_stderr),color='blue',label="MD Chol",fmt='o',capsize=8,elinewidth=3,capthick=3,markersize=12)
plt.errorbar(rates,kJnmtopN*np.asarray(det_force_nochol),yerr=kJnmtopN*np.asarray(det_force_nochol_stderr),color='lime',label="MD SM",fmt='o',capsize=8,elinewidth=3,capthick=3,markersize=12)

plt.plot(rates,func(rates,*popt_chol),label="Fit Chol",lw=6, color="blue")
plt.plot(rates,func(rates,*popt_PSM),label="Fit SM",lw=6, color="lime")

plt.xscale('log')
plt.tick_params(axis='both', which='both', labelsize=32, length=6, width=4)
#plt.legend(fontsize=32)
#plt.title("Detachment force",fontsize=28)
plt.xticks([0.004,0.02,0.1],[0.004,0.02,0.1])
#plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600],[800,900,1000,1100,1200,1300,1400,1500,1600])
plt.yticks([700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800],[700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])
#plt.xlabel("$v_{pull}$ (m/s)",fontsize=36)
#plt.ylabel("$F_{detach}$ (pN)",fontsize=36)
plt.ylim(650, 1850)
#plt.ylim(700, 1700)
plt.savefig("pulling_criteria/force_7p3/det_force_wforce_shortsmooth_nolabel.png", bbox_inches="tight")


fig = plt.figure(figsize=(27,9))
gs = fig.add_gridspec(1,3, wspace=0)
axs = gs.subplots(sharex=True, sharey=True)

axs[2].plot(filtered_slower_chol_1_x,kJnmtopN*filtered_slower_chol_1_f,color='blue',label="Chol",lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_2_x,kJnmtopN*filtered_slower_chol_2_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_3_x,kJnmtopN*filtered_slower_chol_3_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_4_x,kJnmtopN*filtered_slower_chol_4_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_5_x,kJnmtopN*filtered_slower_chol_5_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_6_x,kJnmtopN*filtered_slower_chol_6_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_7_x,kJnmtopN*filtered_slower_chol_7_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_8_x,kJnmtopN*filtered_slower_chol_8_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_9_x,kJnmtopN*filtered_slower_chol_9_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_10_x,kJnmtopN*filtered_slower_chol_10_f,color='blue',lw=0.5, zorder=1)

axs[2].plot(filtered_slower_chol_11_x,kJnmtopN*filtered_slower_chol_11_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_12_x,kJnmtopN*filtered_slower_chol_12_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_13_x,kJnmtopN*filtered_slower_chol_13_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_14_x,kJnmtopN*filtered_slower_chol_14_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_15_x,kJnmtopN*filtered_slower_chol_15_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_16_x,kJnmtopN*filtered_slower_chol_16_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_17_x,kJnmtopN*filtered_slower_chol_17_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_18_x,kJnmtopN*filtered_slower_chol_18_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_19_x,kJnmtopN*filtered_slower_chol_19_f,color='blue',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_chol_20_x,kJnmtopN*filtered_slower_chol_20_f,color='blue',lw=0.5, zorder=1)

axs[2].plot(filtered_slower_nochol_1_x,kJnmtopN*filtered_slower_nochol_1_f,color='lime',label="SM",lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_2_x,kJnmtopN*filtered_slower_nochol_2_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_3_x,kJnmtopN*filtered_slower_nochol_3_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_4_x,kJnmtopN*filtered_slower_nochol_4_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_5_x,kJnmtopN*filtered_slower_nochol_5_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_6_x,kJnmtopN*filtered_slower_nochol_6_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_7_x,kJnmtopN*filtered_slower_nochol_7_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_8_x,kJnmtopN*filtered_slower_nochol_8_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_9_x,kJnmtopN*filtered_slower_nochol_9_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_10_x,kJnmtopN*filtered_slower_nochol_10_f,color='lime',lw=0.5, zorder=1)

axs[2].plot(filtered_slower_nochol_11_x,kJnmtopN*filtered_slower_nochol_11_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_12_x,kJnmtopN*filtered_slower_nochol_12_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_13_x,kJnmtopN*filtered_slower_nochol_13_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_14_x,kJnmtopN*filtered_slower_nochol_14_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_15_x,kJnmtopN*filtered_slower_nochol_15_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_16_x,kJnmtopN*filtered_slower_nochol_16_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_17_x,kJnmtopN*filtered_slower_nochol_17_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_18_x,kJnmtopN*filtered_slower_nochol_18_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_19_x,kJnmtopN*filtered_slower_nochol_19_f,color='lime',lw=0.5, zorder=1)
axs[2].plot(filtered_slower_nochol_20_x,kJnmtopN*filtered_slower_nochol_20_f,color='lime',lw=0.5, zorder=1)

#this is OK, it needs to be divided one more order of magnitude
axs[2].scatter(distance_slower_chol,kJnmtopN*np.asarray(forces_slower_chol),color='blue',s=200,edgecolor='black',zorder=2)
axs[2].scatter(distance_slower_nochol,kJnmtopN*np.asarray(forces_slower_nochol),color='lime',s=200,edgecolor='black',zorder=2)

axs[1].plot(filtered_slowest_chol_1_x,kJnmtopN*filtered_slowest_chol_1_f,color='blue',label="Chol",lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_2_x,kJnmtopN*filtered_slowest_chol_2_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_3_x,kJnmtopN*filtered_slowest_chol_3_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_4_x,kJnmtopN*filtered_slowest_chol_4_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_5_x,kJnmtopN*filtered_slowest_chol_5_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_6_x,kJnmtopN*filtered_slowest_chol_6_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_7_x,kJnmtopN*filtered_slowest_chol_7_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_8_x,kJnmtopN*filtered_slowest_chol_8_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_9_x,kJnmtopN*filtered_slowest_chol_9_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_10_x,kJnmtopN*filtered_slowest_chol_10_f,color='blue',lw=0.5, zorder=1)

axs[1].plot(filtered_slowest_chol_11_x,kJnmtopN*filtered_slowest_chol_11_f,color='blue',label="Chol",lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_12_x,kJnmtopN*filtered_slowest_chol_12_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_13_x,kJnmtopN*filtered_slowest_chol_13_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_14_x,kJnmtopN*filtered_slowest_chol_14_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_15_x,kJnmtopN*filtered_slowest_chol_15_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_16_x,kJnmtopN*filtered_slowest_chol_16_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_17_x,kJnmtopN*filtered_slowest_chol_17_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_18_x,kJnmtopN*filtered_slowest_chol_18_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_19_x,kJnmtopN*filtered_slowest_chol_19_f,color='blue',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_chol_20_x,kJnmtopN*filtered_slowest_chol_20_f,color='blue',lw=0.5, zorder=1)


axs[1].plot(filtered_slowest_nochol_1_x,kJnmtopN*filtered_slowest_nochol_1_f[:2163966],color='lime',label="SM",lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_2_x,kJnmtopN*filtered_slowest_nochol_2_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_3_x,kJnmtopN*filtered_slowest_nochol_3_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_4_x,kJnmtopN*filtered_slowest_nochol_4_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_5_x,kJnmtopN*filtered_slowest_nochol_5_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_6_x,kJnmtopN*filtered_slowest_nochol_6_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_7_x,kJnmtopN*filtered_slowest_nochol_7_f[:2164675],color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_8_x,kJnmtopN*filtered_slowest_nochol_8_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_9_x,kJnmtopN*filtered_slowest_nochol_9_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_10_x,kJnmtopN*filtered_slowest_nochol_10_f,color='lime',lw=0.5, zorder=1)

axs[1].plot(filtered_slowest_nochol_11_x,kJnmtopN*filtered_slowest_nochol_11_f[:2163966],color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_12_x,kJnmtopN*filtered_slowest_nochol_12_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_13_x,kJnmtopN*filtered_slowest_nochol_13_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_14_x,kJnmtopN*filtered_slowest_nochol_14_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_15_x,kJnmtopN*filtered_slowest_nochol_15_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_16_x,kJnmtopN*filtered_slowest_nochol_16_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_17_x,kJnmtopN*filtered_slowest_nochol_17_f[:2164675],color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_18_x,kJnmtopN*filtered_slowest_nochol_18_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_19_x,kJnmtopN*filtered_slowest_nochol_19_f,color='lime',lw=0.5, zorder=1)
axs[1].plot(filtered_slowest_nochol_20_x,kJnmtopN*filtered_slowest_nochol_20_f,color='lime',lw=0.5, zorder=1)

#this is OK, it needs to be divided one more order of magnitude
axs[1].scatter(distance_slowest_chol,kJnmtopN*np.asarray(forces_slowest_chol),color='blue',s=200,edgecolor='black',zorder=2)
axs[1].scatter(distance_slowest_nochol,kJnmtopN*np.asarray(forces_slowest_nochol),color='lime',s=200,edgecolor='black',zorder=2)

axs[0].plot(filtered_glacial_chol_1_x[:9018027],kJnmtopN*filtered_glacial_chol_1_f,color='blue',label="Chol",lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_2_x,kJnmtopN*filtered_glacial_chol_2_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_3_x,kJnmtopN*filtered_glacial_chol_3_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_4_x,kJnmtopN*filtered_glacial_chol_4_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_5_x,kJnmtopN*filtered_glacial_chol_5_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_6_x,kJnmtopN*filtered_glacial_chol_6_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_7_x,kJnmtopN*filtered_glacial_chol_7_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_8_x,kJnmtopN*filtered_glacial_chol_8_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_9_x,kJnmtopN*filtered_glacial_chol_9_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_10_x,kJnmtopN*filtered_glacial_chol_10_f,color='blue',lw=0.5, zorder=1)

axs[0].plot(filtered_glacial_chol_11_x[:9018027],kJnmtopN*filtered_glacial_chol_11_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_12_x,kJnmtopN*filtered_glacial_chol_12_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_13_x,kJnmtopN*filtered_glacial_chol_13_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_14_x,kJnmtopN*filtered_glacial_chol_14_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_15_x,kJnmtopN*filtered_glacial_chol_15_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_16_x,kJnmtopN*filtered_glacial_chol_16_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_17_x,kJnmtopN*filtered_glacial_chol_17_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_18_x,kJnmtopN*filtered_glacial_chol_18_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_19_x,kJnmtopN*filtered_glacial_chol_19_f,color='blue',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_chol_20_x,kJnmtopN*filtered_glacial_chol_20_f,color='blue',lw=0.5, zorder=1)

axs[0].plot(filtered_glacial_nochol_1_x,kJnmtopN*filtered_glacial_nochol_1_f,color='lime',label="SM",lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_2_x,kJnmtopN*filtered_glacial_nochol_2_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_3_x,kJnmtopN*filtered_glacial_nochol_3_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_4_x,kJnmtopN*filtered_glacial_nochol_4_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_5_x,kJnmtopN*filtered_glacial_nochol_5_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_6_x,kJnmtopN*filtered_glacial_nochol_6_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_7_x,kJnmtopN*filtered_glacial_nochol_7_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_8_x,kJnmtopN*filtered_glacial_nochol_8_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_9_x,kJnmtopN*filtered_glacial_nochol_9_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_10_x,kJnmtopN*filtered_glacial_nochol_10_f,color='lime',lw=0.5, zorder=1)

axs[0].plot(filtered_glacial_nochol_11_x,kJnmtopN*filtered_glacial_nochol_11_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_12_x,kJnmtopN*filtered_glacial_nochol_12_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_13_x,kJnmtopN*filtered_glacial_nochol_13_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_14_x,kJnmtopN*filtered_glacial_nochol_14_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_15_x,kJnmtopN*filtered_glacial_nochol_15_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_16_x,kJnmtopN*filtered_glacial_nochol_16_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_17_x,kJnmtopN*filtered_glacial_nochol_17_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_18_x,kJnmtopN*filtered_glacial_nochol_18_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_19_x,kJnmtopN*filtered_glacial_nochol_19_f,color='lime',lw=0.5, zorder=1)
axs[0].plot(filtered_glacial_nochol_20_x,kJnmtopN*filtered_glacial_nochol_20_f,color='lime',lw=0.5, zorder=1)

#this is OK, it needs to be divided one more order of magnitude
axs[0].scatter(distance_glacial_chol,kJnmtopN*np.asarray(forces_glacial_chol),color='blue',s=200,edgecolor='black',zorder=2)
axs[0].scatter(distance_glacial_nochol,kJnmtopN*np.asarray(forces_glacial_nochol),color='lime',s=200,edgecolor='black',zorder=2)

for ax in axs:
    ax.tick_params(axis='x', which='both', labelsize=32,length=6, width=4)
    ax.tick_params(axis='y', which='both', labelsize=32,length=6, width=4)
    ax.set_xlim(6.7,9.7)
    ax.set_ylim(0,2100)
    ax.label_outer()
    ax.set_xticks([7.0, 7.5, 8.0, 8.5, 9.0, 9.5])
axs[0].set_ylabel("$F$ (pN)",fontsize=36)
axs[1].set_xlabel("$d_{COM}$ (nm)",fontsize=36)

plt.tight_layout()
plt.savefig("pulling_criteria/force_7p3/all_param_wF_shortsmooth_nolabel.png")



np.savetxt('pulling_criteria/force_7p3/detachment_frames_glacial_chol.txt',frames_glacial_chol)
np.savetxt('pulling_criteria/force_7p3/detachment_forces.txt',(kJnmtopN*np.asarray(det_force_chol),kJnmtopN*np.asarray(det_force_nochol),kJnmtopN*np.asarray(det_force_chol_stderr),kJnmtopN*np.asarray(det_force_nochol_stderr)))
np.savetxt('pulling_criteria/force_7p3/detachment_forces_values.txt',(kJnmtopN*forces_slower_chol,kJnmtopN*forces_slower_nochol,kJnmtopN*forces_slowest_chol,kJnmtopN*forces_slowest_nochol,kJnmtopN*forces_glacial_chol,kJnmtopN*forces_glacial_nochol))
np.savetxt('pulling_criteria/force_7p3/fit_param_stddev.txt',(popt_chol,popt_PSM,perr_chol,perr_PSM))


