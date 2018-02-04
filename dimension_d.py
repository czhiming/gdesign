#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

labels = ['512','1024','2048','4096']

#向量维数不同时
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

y_15_d = np.array([[0.316,14.454,18.043,0.298,5.008],
        [0.332,13.613,17.745,0.311,5.645],
        [0.338,13.766,17.719,0.305,5.573],
        [0.321,14.070,17.950,0.280,4.998],
        [0.308,14.538,18.098,0.298,4.927],
        [0.311,13.740,17.909,0.294,4.965],
        [0.317,13.847,17.891,0.298,4.877],
        [0.327,14.303, 18.005,0.285,4.810]
        ]) 
y_16_d = np.array([[0.370,13.485,18.021,0.409,6.801],
        [0.392,13.340,17.796,0.427,7.192],
        [0.404,13.243,17.662,0.435,7.337],
        [0.411,13.198,17.542,0.439,7.479],
        [0.372,13.528,18.043,0.414,6.649],
        [0.374,13.469,17.977,0.412,6.854],
        [0.378,13.467,17.947,0.410,6.875],
        [0.381,13.530,17.859,0.407,6.903]
        ])



x = np.arange(4)
fig,ax = plt.subplots()
########################################
offSet = 0.002
i = 0
wmt15 = y_15[-4:,i]
wmt16 = y_16[-4:,i]
wmt15_d_src = y_15_d[0:4,i]
wmt15_d_tgt = y_15_d[4:8,i]
wmt16_d_src = y_16_d[0:4,i]
wmt16_d_tgt = y_16_d[4:8,i]


########################################
#ax.plot(x,wmt15,'ok-',ms=8)
ax.plot(x,wmt16,'ok-',ms=8)
#ax.plot(x,wmt15_d_src,'*k-',x,wmt15_d_tgt,'vk-',ms=8)
ax.plot(x,wmt16_d_src,'*k-',x,wmt16_d_tgt,'vk-',ms=8)

ax.set_xticks([0,1,2,3])
ax.set_xticklabels(labels)

ax.annotate(str(wmt16[2])+'(best)',xy=(2,wmt16[2]-offSet))
#ax.annotate(str(wmt15_d_src[2])+'(best)',xy=(2,wmt15_d_src[2]-offSet))


"""
for index in x:
    ax.annotate(str(wmt15[index]),xy=(index,wmt15[index]-offSet))
    ax.annotate(str(wmt16[index]),xy=(index,wmt16[index]-offSet))
    ax.annotate(str(wmt15_d_src[index]),xy=(index,wmt15_d_src[index]-offSet))
    ax.annotate(str(wmt15_d_tgt[index]),xy=(index,wmt15_d_tgt[index]-offSet))
    ax.annotate(str(wmt16_d_src[index]),xy=(index,wmt16_d_src[index]-offSet))
    ax.annotate(str(wmt16_d_tgt[index]),xy=(index,wmt16_d_tgt[index]-offSet))
"""
plt.title('WMT16 QE')
plt.xlabel('dimension')
plt.ylabel('Pearson r')
plt.legend(['src=tgt','tgt=n*src','src=n*tgt'],loc='lower right')
#plt.grid()
plt.show()








