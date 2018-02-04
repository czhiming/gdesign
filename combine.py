#-*- coding:utf8 -*-
'''
Created on Dec 5, 2016

@author: czm
'''

import sys 

if len(sys.argv) < 4:
    sys.exit(1)
    
file = [open(fp) for fp in sys.argv[1:3]]

with open(sys.argv[3],'w') as fp:
    for lines in file[0]:
        lines = lines.strip()
        lines = lines+'\t'+file[1].readline()
        fp.writelines(lines)
    














if __name__ == '__main__':
    pass
