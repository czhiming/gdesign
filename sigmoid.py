#-*- coding:utf-8 -*-
'''
Created on 2017年3月9日

@author: Administrator
'''
import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(-6,6)
y = 1./(1+numpy.exp(-x))

plt.plot(x,y)
plt.show()






if __name__ == '__main__':
    pass