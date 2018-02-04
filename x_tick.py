#-*- coding:utf-8 -*-
'''
Created on 2016年7月25日

@author: Administrator
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
y2 = y + 0.1 * np.random.normal(size=x.shape)

fig, ax = plt.subplots()
ax.plot(x, y, 'k--')
ax.plot(x, y2, 'ro')

# set ticks and tick labels
#ax.set_xlim((0, 2*np.pi))
ax.set_xticks([0, np.pi, 2*np.pi])  #行标的值
ax.set_xticklabels(['0', '$\pi$', '2$\pi$']) #行标

#ax.set_ylim((-1.5, 1.5))
#ax.set_yticks([-1, 0, 1])
"""
# Only dimension spine between the y-ticks
ax.spines['left'].set_bounds(-1, 1)
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')   #行标的位置
"""
plt.show()














if __name__ == '__main__':
    pass