#-*- coding:utf-8 -*-
'''
Created on 2017年3月13日

@author: Administrator
'''
import sys

if len(sys.argv) < 4:
    sys.exit(0)
    
file = sys.argv[1]
lm_file = open(sys.argv[2])
out_lm_file = sys.argv[3]

with open(out_lm_file,'w') as fo:
    for lines in open(file):
        lines = lines.strip().split()
        length = len(lines)
        
        prob = float(lm_file.readline().strip())
        prob = prob/length
        
        fo.writelines(str(prob)+'\n')












if __name__ == '__main__':
    pass