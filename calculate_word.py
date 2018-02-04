#-*- coding:utf-8 -*-
'''
Created on 2017年3月14日

@author: Administrator
'''
import sys


if len(sys.argv) < 2:
    sys.exit(0)

file_name = sys.argv[1]

vocab = set([])
count = 0
for lines in open(file_name):
    lines = lines.strip().split()
    for word in lines:
        if word not in vocab:
            vocab.add(word)
        count += 1
    
print '词汇表大小：',len(vocab)
print '总词数：',count
        





if __name__ == '__main__':
    pass