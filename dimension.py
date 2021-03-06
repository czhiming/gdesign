#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

labels = ['16','32','64','128','256','512','1024','2048','4096']

y_15 = np.array([[0.246,14.682,18.340,0.234,4.730],
         [0.283,14.566,18.186,0.282,5.310],
         [0.280,14.509,18.171,0.268,4.781],
         [0.283,14.552,18.166,0.273,4.795],
         [0.300,14.495,18.116,0.287,4.780],
         [0.324,14.496,18.032,0.306,5.224],
         [0.330,13.711,17.785,0.308,5.262],
         [0.329,14.005,17.885,0.291,5.027],
         [0.327,14.303,18.005,0.285,4.810]])
y_16 = np.array([[0.236,14.477,18.464,0.243,4.107],
        [0.258,14.374,18.360,0.279,4.672],
        [0.301,14.149,18.110,0.336,5.414],
        [0.333,13.800,18.405,0.378,6.252],
        [0.351,13.642,18.209,0.391,6.388],
        [0.390,13.346,17.856,0.427,7.023],
        [0.412,13.160,17.600,0.443,7.445],
        [0.416,13.222,17.488,0.432,7.327],
        [0.416,13.294,17.385,0.434,7.339],
        ])

x = np.arange(9)
fig,ax = plt.subplots()
########################################
offSet = 0.01
wmt15 = y_15[:,3]
wmt16 = y_16[:,3]
#plt.title('Pearson r')
########################################

ax.plot(x,wmt15,'^k-',x,wmt16,'ok-',ms=8)
ax.set_xticklabels(labels)
for index in x:
    ax.annotate(str(wmt15[index]),xy=(index,wmt15[index]-offSet))
    ax.annotate(str(wmt16[index]),xy=(index,wmt16[index]-offSet))
plt.xlabel('dimension')
plt.ylabel('Spearman rho')
#plt.grid()
plt.legend(['wmt15 QE','wmt16 QE'],loc='upper left')
plt.show()








