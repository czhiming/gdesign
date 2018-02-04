#-*- coding:utf8 -*-
'''
Created on Feb 28, 2017

@author: czm
'''
import json
qe_dir = '/home/czm/workspace/QE_project'

pos_dict = None
with open(qe_dir+'/data/wmt15/task1/wmt15.test.source.pos.json') as fp:
    pos_dict = json.load(fp)
i = 0
for word in pos_dict:
    for line in pos_dict[word]:
        print line
    i += 1
    if i>10:
        break 






if __name__ == '__main__':
    pass