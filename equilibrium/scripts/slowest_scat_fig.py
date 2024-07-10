import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  scipy.ndimage.filters import gaussian_filter1d as filtro_gaussiano
from scipy.stats import sem as error_estandar


slowest_chol_1_x=pd.read_csv("slowest/chol/1/pullx_format.xvg",header=None,sep=" ")
slowest_chol_2_x=pd.read_csv("slowest/chol/2/pullx_format.xvg",header=None,sep=" ")
slowest_chol_3_x=pd.read_csv("slowest/chol/3/pullx_format.xvg",header=None,sep=" ")
slowest_chol_4_x=pd.read_csv("slowest/chol/4/pullx_format.xvg",header=None,sep=" ")
slowest_chol_5_x=pd.read_csv("slowest/chol/5/pullx_format.xvg",header=None,sep=" ")
slowest_chol_6_x=pd.read_csv("slowest/chol/6/pullx_format.xvg",header=None,sep=" ")
slowest_chol_7_x=pd.read_csv("slowest/chol/7/pullx_format.xvg",header=None,sep=" ")
slowest_chol_8_x=pd.read_csv("slowest/chol/8/pullx_format.xvg",header=None,sep=" ")
slowest_chol_9_x=pd.read_csv("slowest/chol/9/pullx_format.xvg",header=None,sep=" ")
slowest_chol_10_x=pd.read_csv("slowest/chol/10/pullx_format.xvg",header=None,sep=" ")


slowest_nochol_1_x=pd.read_csv("slowest/no_chol/1/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_2_x=pd.read_csv("slowest/no_chol/2/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_3_x=pd.read_csv("slowest/no_chol/3/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_4_x=pd.read_csv("slowest/no_chol/4/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_5_x=pd.read_csv("slowest/no_chol/5/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_6_x=pd.read_csv("slowest/no_chol/6/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_7_x=pd.read_csv("slowest/no_chol/7/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_8_x=pd.read_csv("slowest/no_chol/8/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_9_x=pd.read_csv("slowest/no_chol/9/pullx_format.xvg",header=None,sep=" ")
slowest_nochol_10_x=pd.read_csv("slowest/no_chol/10/pullx_format.xvg",header=None,sep=" ")


slowest_chol_1_f=pd.read_csv("slowest/chol/1/pullf_format.xvg",header=None,sep=" ")
slowest_chol_2_f=pd.read_csv("slowest/chol/2/pullf_format.xvg",header=None,sep=" ")
slowest_chol_3_f=pd.read_csv("slowest/chol/3/pullf_format.xvg",header=None,sep=" ")
slowest_chol_4_f=pd.read_csv("slowest/chol/4/pullf_format.xvg",header=None,sep=" ")
slowest_chol_5_f=pd.read_csv("slowest/chol/5/pullf_format.xvg",header=None,sep=" ")
slowest_chol_6_f=pd.read_csv("slowest/chol/6/pullf_format.xvg",header=None,sep=" ")
slowest_chol_7_f=pd.read_csv("slowest/chol/7/pullf_format.xvg",header=None,sep=" ")
slowest_chol_8_f=pd.read_csv("slowest/chol/8/pullf_format.xvg",header=None,sep=" ")
slowest_chol_9_f=pd.read_csv("slowest/chol/9/pullf_format.xvg",header=None,sep=" ")
slowest_chol_10_f=pd.read_csv("slowest/chol/10/pullf_format.xvg",header=None,sep=" ")


slowest_nochol_1_f=pd.read_csv("slowest/no_chol/1/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_2_f=pd.read_csv("slowest/no_chol/2/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_3_f=pd.read_csv("slowest/no_chol/3/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_4_f=pd.read_csv("slowest/no_chol/4/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_5_f=pd.read_csv("slowest/no_chol/5/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_6_f=pd.read_csv("slowest/no_chol/6/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_7_f=pd.read_csv("slowest/no_chol/7/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_8_f=pd.read_csv("slowest/no_chol/8/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_9_f=pd.read_csv("slowest/no_chol/9/pullf_format.xvg",header=None,sep=" ")
slowest_nochol_10_f=pd.read_csv("slowest/no_chol/10/pullf_format.xvg",header=None,sep=" ")


filtered_slowest_chol_1_x=np.loadtxt('filt_slowest_chol_1_x.txt')
filtered_slowest_chol_2_x=np.loadtxt('filt_slowest_chol_2_x.txt')
filtered_slowest_chol_3_x=np.loadtxt('filt_slowest_chol_3_x.txt')
filtered_slowest_chol_4_x=np.loadtxt('filt_slowest_chol_4_x.txt')
filtered_slowest_chol_5_x=np.loadtxt('filt_slowest_chol_5_x.txt')
filtered_slowest_chol_6_x=np.loadtxt('filt_slowest_chol_6_x.txt')
filtered_slowest_chol_7_x=np.loadtxt('filt_slowest_chol_7_x.txt')
filtered_slowest_chol_8_x=np.loadtxt('filt_slowest_chol_8_x.txt')
filtered_slowest_chol_9_x=np.loadtxt('filt_slowest_chol_9_x.txt')
filtered_slowest_chol_10_x=np.loadtxt('filt_slowest_chol_10_x.txt')

filtered_slowest_nochol_1_x=np.loadtxt('filt_slowest_nochol_1_x.txt')
filtered_slowest_nochol_2_x=np.loadtxt('filt_slowest_nochol_2_x.txt')
filtered_slowest_nochol_3_x=np.loadtxt('filt_slowest_nochol_3_x.txt')
filtered_slowest_nochol_4_x=np.loadtxt('filt_slowest_nochol_4_x.txt')
filtered_slowest_nochol_5_x=np.loadtxt('filt_slowest_nochol_5_x.txt')
filtered_slowest_nochol_6_x=np.loadtxt('filt_slowest_nochol_6_x.txt')
filtered_slowest_nochol_7_x=np.loadtxt('filt_slowest_nochol_7_x.txt')
filtered_slowest_nochol_8_x=np.loadtxt('filt_slowest_nochol_8_x.txt')
filtered_slowest_nochol_9_x=np.loadtxt('filt_slowest_nochol_9_x.txt')
filtered_slowest_nochol_10_x=np.loadtxt('filt_slowest_nochol_10_x.txt')

filtered_slowest_chol_1_f=np.loadtxt('filt_slowest_chol_1_f.txt')
filtered_slowest_chol_2_f=np.loadtxt('filt_slowest_chol_2_f.txt')
filtered_slowest_chol_3_f=np.loadtxt('filt_slowest_chol_3_f.txt')
filtered_slowest_chol_4_f=np.loadtxt('filt_slowest_chol_4_f.txt')
filtered_slowest_chol_5_f=np.loadtxt('filt_slowest_chol_5_f.txt')
filtered_slowest_chol_6_f=np.loadtxt('filt_slowest_chol_6_f.txt')
filtered_slowest_chol_7_f=np.loadtxt('filt_slowest_chol_7_f.txt')
filtered_slowest_chol_8_f=np.loadtxt('filt_slowest_chol_8_f.txt')
filtered_slowest_chol_9_f=np.loadtxt('filt_slowest_chol_9_f.txt')
filtered_slowest_chol_10_f=np.loadtxt('filt_slowest_chol_10_f.txt')

filtered_slowest_nochol_1_f=np.loadtxt('filt_slowest_nochol_1_f.txt')
filtered_slowest_nochol_2_f=np.loadtxt('filt_slowest_nochol_2_f.txt')
filtered_slowest_nochol_3_f=np.loadtxt('filt_slowest_nochol_3_f.txt')
filtered_slowest_nochol_4_f=np.loadtxt('filt_slowest_nochol_4_f.txt')
filtered_slowest_nochol_5_f=np.loadtxt('filt_slowest_nochol_5_f.txt')
filtered_slowest_nochol_6_f=np.loadtxt('filt_slowest_nochol_6_f.txt')
filtered_slowest_nochol_7_f=np.loadtxt('filt_slowest_nochol_7_f.txt')
filtered_slowest_nochol_8_f=np.loadtxt('filt_slowest_nochol_8_f.txt')
filtered_slowest_nochol_9_f=np.loadtxt('filt_slowest_nochol_9_f.txt')
filtered_slowest_nochol_10_f=np.loadtxt('filt_slowest_nochol_10_f.txt')



corte=7.3
rates=[0.004,0.02,0.1]
det_times_chol=[0]*3
det_times_nochol=[0]*3
det_times_chol_stderr=[0]*3
det_times_nochol_stderr=[0]*3
det_force_chol=[0]*3
det_force_nochol=[0]*3
det_force_chol_stderr=[0]*3
det_force_nochol_stderr=[0]*3


frames_slowest_chol=np.zeros(10)

frames_slowest_chol[0]=np.where(filtered_slowest_chol_1_x<corte)[0][-1]
frames_slowest_chol[1]=np.where(filtered_slowest_chol_2_x<corte)[0][-1]
frames_slowest_chol[2]=np.where(filtered_slowest_chol_3_x<corte)[0][-1]
frames_slowest_chol[3]=np.where(filtered_slowest_chol_4_x<corte)[0][-1]
frames_slowest_chol[4]=np.where(filtered_slowest_chol_5_x<corte)[0][-1]
frames_slowest_chol[5]=np.where(filtered_slowest_chol_6_x<corte)[0][-1]
frames_slowest_chol[6]=np.where(filtered_slowest_chol_7_x<corte)[0][-1]
frames_slowest_chol[7]=np.where(filtered_slowest_chol_8_x<corte)[0][-1]
frames_slowest_chol[8]=np.where(filtered_slowest_chol_9_x<corte)[0][-1]
frames_slowest_chol[9]=np.where(filtered_slowest_chol_10_x<corte)[0][-1]

forces_slowest_chol=np.zeros(10)

forces_slowest_chol[0]=filtered_slowest_chol_1_f[frames_slowest_chol[0].astype(int)]
forces_slowest_chol[1]=filtered_slowest_chol_2_f[frames_slowest_chol[1].astype(int)]
forces_slowest_chol[2]=filtered_slowest_chol_3_f[frames_slowest_chol[2].astype(int)]
forces_slowest_chol[3]=filtered_slowest_chol_4_f[frames_slowest_chol[3].astype(int)]
forces_slowest_chol[4]=filtered_slowest_chol_5_f[frames_slowest_chol[4].astype(int)]
forces_slowest_chol[5]=filtered_slowest_chol_6_f[frames_slowest_chol[5].astype(int)]
forces_slowest_chol[6]=filtered_slowest_chol_7_f[frames_slowest_chol[6].astype(int)]
forces_slowest_chol[7]=filtered_slowest_chol_8_f[frames_slowest_chol[7].astype(int)]
forces_slowest_chol[8]=filtered_slowest_chol_9_f[frames_slowest_chol[8].astype(int)]
forces_slowest_chol[9]=filtered_slowest_chol_10_f[frames_slowest_chol[9].astype(int)]

frames_slowest_nochol=np.zeros(10)

frames_slowest_nochol[0]=np.where(filtered_slowest_nochol_1_x<corte)[0][-1]
frames_slowest_nochol[1]=np.where(filtered_slowest_nochol_2_x<corte)[0][-1]
frames_slowest_nochol[2]=np.where(filtered_slowest_nochol_3_x<corte)[0][-1]
frames_slowest_nochol[3]=np.where(filtered_slowest_nochol_4_x<corte)[0][-1]
frames_slowest_nochol[4]=np.where(filtered_slowest_nochol_5_x<corte)[0][-1]
frames_slowest_nochol[5]=np.where(filtered_slowest_nochol_6_x<corte)[0][-1]
frames_slowest_nochol[6]=np.where(filtered_slowest_nochol_7_x<corte)[0][-1]
frames_slowest_nochol[7]=np.where(filtered_slowest_nochol_8_x<corte)[0][-1]
frames_slowest_nochol[8]=np.where(filtered_slowest_nochol_9_x<corte)[0][-1]
frames_slowest_nochol[9]=np.where(filtered_slowest_nochol_10_x<corte)[0][-1]

forces_slowest_nochol=np.zeros(10)

forces_slowest_nochol[0]=filtered_slowest_nochol_1_f[frames_slowest_nochol[0].astype(int)]
forces_slowest_nochol[1]=filtered_slowest_nochol_2_f[frames_slowest_nochol[1].astype(int)]
forces_slowest_nochol[2]=filtered_slowest_nochol_3_f[frames_slowest_nochol[2].astype(int)]
forces_slowest_nochol[3]=filtered_slowest_nochol_4_f[frames_slowest_nochol[3].astype(int)]
forces_slowest_nochol[4]=filtered_slowest_nochol_5_f[frames_slowest_nochol[4].astype(int)]
forces_slowest_nochol[5]=filtered_slowest_nochol_6_f[frames_slowest_nochol[5].astype(int)]
forces_slowest_nochol[6]=filtered_slowest_nochol_7_f[frames_slowest_nochol[6].astype(int)]
forces_slowest_nochol[7]=filtered_slowest_nochol_8_f[frames_slowest_nochol[7].astype(int)]
forces_slowest_nochol[8]=filtered_slowest_nochol_9_f[frames_slowest_nochol[8].astype(int)]
forces_slowest_nochol[9]=filtered_slowest_nochol_10_f[frames_slowest_nochol[9].astype(int)]




det_times_chol[0]=np.average(0.0001*frames_slowest_chol)
det_times_nochol[0]=np.average(0.0001*frames_slowest_nochol)
det_times_chol_stderr[0]=error_estandar(0.0001*frames_slowest_chol)
det_times_nochol_stderr[0]=error_estandar(0.0001*frames_slowest_nochol)
det_force_chol[0]=np.average(forces_slowest_chol)
det_force_nochol[0]=np.average(forces_slowest_nochol)
det_force_chol_stderr[0]=error_estandar(forces_slowest_chol)
det_force_nochol_stderr[0]=error_estandar(forces_slowest_nochol)



plt.figure(figsize=(12,12))

plt.plot(0.001*slowest_chol_1_x.iloc[:,0],filtered_slowest_chol_1_x,color='blue',label="Chol.")
plt.plot(0.001*slowest_chol_2_x.iloc[:,0],filtered_slowest_chol_2_x,color='blue')
plt.plot(0.001*slowest_chol_3_x.iloc[:,0],filtered_slowest_chol_3_x,color='blue')
plt.plot(0.001*slowest_chol_4_x.iloc[:,0],filtered_slowest_chol_4_x,color='blue')
plt.plot(0.001*slowest_chol_5_x.iloc[:,0],filtered_slowest_chol_5_x,color='blue')
plt.plot(0.001*slowest_chol_6_x.iloc[:,0],filtered_slowest_chol_6_x,color='blue')
plt.plot(0.001*slowest_chol_7_x.iloc[:,0],filtered_slowest_chol_7_x,color='blue')
plt.plot(0.001*slowest_chol_8_x.iloc[:,0],filtered_slowest_chol_8_x,color='blue')
plt.plot(0.001*slowest_chol_9_x.iloc[:,0],filtered_slowest_chol_9_x,color='blue')
plt.plot(0.001*slowest_chol_10_x.iloc[:,0],filtered_slowest_chol_10_x,color='blue')

plt.plot(0.001*slowest_nochol_1_x.iloc[:,0],filtered_slowest_nochol_1_x,color='red',label="No chol.")
plt.plot(0.001*slowest_nochol_2_x.iloc[:,0],filtered_slowest_nochol_2_x,color='red')
plt.plot(0.001*slowest_nochol_3_x.iloc[:,0],filtered_slowest_nochol_3_x,color='red')
plt.plot(0.001*slowest_nochol_4_x.iloc[:,0],filtered_slowest_nochol_4_x,color='red')
plt.plot(0.001*slowest_nochol_5_x.iloc[:,0],filtered_slowest_nochol_5_x,color='red')
plt.plot(0.001*slowest_nochol_6_x.iloc[:,0],filtered_slowest_nochol_6_x,color='red')
plt.plot(0.001*slowest_nochol_7_x.iloc[:,0],filtered_slowest_nochol_7_x,color='red')
plt.plot(0.001*slowest_nochol_8_x.iloc[:,0],filtered_slowest_nochol_8_x,color='red')
plt.plot(0.001*slowest_nochol_9_x.iloc[:,0],filtered_slowest_nochol_9_x,color='red')
plt.plot(0.001*slowest_nochol_10_x.iloc[:,0],filtered_slowest_nochol_10_x,color='red')

#this is OK, it needs to be divided one more order of magnitude
plt.scatter(0.0001*frames_slowest_chol,[7.3]*10,color='blue',s=100)
plt.scatter(0.0001*frames_slowest_nochol,[7.3]*10,color='red',s=100)

plt.tick_params(axis='x', which='major', labelsize=24)
plt.tick_params(axis='y', which='major', labelsize=24)
plt.legend(fontsize=24)
plt.title("$V_{pull}$ = 0.02 m/s",fontsize=28)
#xticks(np.arange(0,500,200), ["",200,400])
plt.xlabel("Time (ns)",fontsize=26)
plt.ylabel("$D_{tet-tet}$ (nm)",fontsize=26)
plt.savefig("smooth_slowest_scat.png")



plt.figure(figsize=(12,12))

plt.plot(0.001*slowest_chol_1_f.iloc[:,0],filtered_slowest_chol_1_f,color='blue',label="Chol.")
plt.plot(0.001*slowest_chol_2_f.iloc[:,0],filtered_slowest_chol_2_f,color='blue')
plt.plot(0.001*slowest_chol_3_f.iloc[:,0],filtered_slowest_chol_3_f,color='blue')
plt.plot(0.001*slowest_chol_4_f.iloc[:,0],filtered_slowest_chol_4_f,color='blue')
plt.plot(0.001*slowest_chol_5_f.iloc[:,0],filtered_slowest_chol_5_f,color='blue')
plt.plot(0.001*slowest_chol_6_f.iloc[:,0],filtered_slowest_chol_6_f,color='blue')
plt.plot(0.001*slowest_chol_7_f.iloc[:,0],filtered_slowest_chol_7_f,color='blue')
plt.plot(0.001*slowest_chol_8_f.iloc[:,0],filtered_slowest_chol_8_f,color='blue')
plt.plot(0.001*slowest_chol_9_f.iloc[:,0],filtered_slowest_chol_9_f,color='blue')
plt.plot(0.001*slowest_chol_10_f.iloc[:,0],filtered_slowest_chol_10_f,color='blue')

plt.plot(0.001*slowest_nochol_1_f.iloc[:,0],filtered_slowest_nochol_1_f,color='red',label="No chol.")
plt.plot(0.001*slowest_nochol_2_f.iloc[:,0],filtered_slowest_nochol_2_f,color='red')
plt.plot(0.001*slowest_nochol_3_f.iloc[:,0],filtered_slowest_nochol_3_f,color='red')
plt.plot(0.001*slowest_nochol_4_f.iloc[:,0],filtered_slowest_nochol_4_f,color='red')
plt.plot(0.001*slowest_nochol_5_f.iloc[:,0],filtered_slowest_nochol_5_f,color='red')
plt.plot(0.001*slowest_nochol_6_f.iloc[:,0],filtered_slowest_nochol_6_f,color='red')
plt.plot(0.001*slowest_nochol_7_f.iloc[:,0],filtered_slowest_nochol_7_f,color='red')
plt.plot(0.001*slowest_nochol_8_f.iloc[:,0],filtered_slowest_nochol_8_f,color='red')
plt.plot(0.001*slowest_nochol_9_f.iloc[:,0],filtered_slowest_nochol_9_f,color='red')
plt.plot(0.001*slowest_nochol_10_f.iloc[:,0],filtered_slowest_nochol_10_f,color='red')

#this is OK, it needs to be divided one more order of magnitude
plt.scatter(0.0001*frames_slowest_chol,forces_slowest_chol,color='blue',s=100)
plt.scatter(0.0001*frames_slowest_nochol,forces_slowest_nochol,color='red',s=100)

plt.tick_params(axis='x', which='major', labelsize=24)
plt.tick_params(axis='y', which='major', labelsize=24)
plt.legend(fontsize=24)
plt.title("$V_{pull}$ = 0.02 m/s",fontsize=28)
#xticks(np.arange(0,500,200), ["",200,400])
plt.xlabel("Time (ns)",fontsize=26)
plt.ylabel("F (kJ/mol/nm)",fontsize=26)
plt.savefig("smooth_slowest_f_scat.png")
