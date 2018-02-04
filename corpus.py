#-*- coding:utf-8 -*-
'''
Created on 2017年3月5日

@author: Administrator
'''

import matplotlib.pyplot as plt
import numpy as np

labels = ['1','1/4','1/16','1/64','1/256','1/1024','1/4096']

y_15 = np.array([[0.300,14.495,18.116,0.287,4.780],
            [0.309,14.517,18.094,0.309,5.645],
            [0.281,14.607,18.182,0.277,5.081],
            [0.253,14.654,18.298,0.240,4.364],
            [0.247,14.666,18.328,0.253,4.069],
            [0.271,14.649,18.243,0.258,4.503],
            [0.285,14.624,18.192,0.268,4.773]])
y_16 = np.array([[0.351,13.642,18.209,0.391,6.388],
            [0.360,13.580,18.134,0.395,6.657],
            [0.316,13.832,18.400,0.359,5.902],
            [0.293,13.934,18.598,0.334,5.327],
            [0.272,14.315,18.274,0.307,5.045],
            [0.312,13.868,18.441,0.349,5.763],
            [0.345,13.715,18.269,0.369,6.134]])
#256
"""
y_15 = np.array([[0.300,14.495,18.116,0.287,4.780],
            [0.309,14.554,18.100,0.300,5.513],
            [0.292,14.561,18.123,0.284,5.051],
            [0.262,14.653,18.266,0.246,4.129],
            [0.268,14.645,18.231,0.247,4.531],
            [0.260,14.787,18.312,0.260,4.242],
            [0.287,13.922,18.019,0.268,4.921]])
y_16 = np.array([[0.351,13.642,18.209,0.391,6.388],
            [0.357,13.689,18.213,0.396,6.575],
            [0.313,13.894,18.448,0.353,6.028],
            [0.265,14.349,18.319,0.294,4.805],
            [0.304,14.155,18.084,0.334,5.609],
            [0.304,14.100,18.083,0.333,5.822],
            [0.352,13.709,18.202,0.386,6.390]])
"""
#1024

y_15 = np.array([[0.330,13.711,17.785,0.308,5.262],
            [0.316,13.791,17.853,0.288,5.203],
            [0.290,14.572,18.136,0.286,4.951],
            [0.258,14.645,18.285,0.255,4.06],
            [0.275,14.607,18.216,0.272,4.790],
            [0.308,13.925,17.931,0.281,5.083],
            [0.310,13.902,17.899,0.280,4.993]])
y_16 = np.array([[0.412,13.160,17.600,0.443,7.445],
            [0.362,13.542,18.073,0.394,6.533],
            [0.295,14.193,18.244,0.340,5.653],
            [0.308,13.883,18.409,0.344,5.708],
            [0.309,14.192,18.064,0.333,5.651],
            [0.368,13.569,18.005,0.388,6.714],
            [0.362,13.577,18.027,0.392,6.459]])



x = np.arange(7)
fig,ax = plt.subplots()
########################################
offSet = 0.00
wmt15 = y_15[:,0]
wmt16 = y_16[:,0]
plt.title('dimension=1024')
########################################

ax.plot(x,wmt15,'^k-',x,wmt16,'ok-',ms=8)
ax.set_xticklabels(labels)
"""
for index in x:
    ax.annotate(str(wmt15[index]),xy=(index,wmt15[index]-offSet))
    ax.annotate(str(wmt16[index]),xy=(index,wmt16[index]-offSet))
"""
plt.xlabel('proportion')
plt.ylabel('Pearson r')
#plt.grid()
plt.legend(['wmt15','wmt16'],loc='upper right')
plt.show()













if __name__ == '__main__':
    pass