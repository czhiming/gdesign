#coding:UTF8

from sklearn.cluster import KMeans
import numpy as np
import sys
###############################
# python kmeans.py input_file feature_file n_clusters ouput_file
##############################

########################################
qe_dir = '/home/liutuan/czm/workspace/QE_project/'
out_dir = '/new_home/czm/workspace/QE_project/'
#np.random.seed(123)
number = 3999549
input_file = qe_dir+'data/wmt15/wmt15qe.train.tok.en'
########################################

def make_file(ratio=None,input_file=None,output_file=None):
    doc = []
    with open(output_file,'w') as fp:
        index = set(np.random.choice(number,int(ratio*number)))
        for i,lines in enumerate(open(input_file)):
            if i in index:
                lines = lines.strip()
                fp.writelines(lines+'\n')

#----------------------------------------#    
ratio = 1./4
output_file = out_dir+'data/wmt15/wmt15qe.train.tok.4.en'
make_file(ratio=ratio, input_dict=input_file, output_file=output_file)
#----------------------------------------#

#----------------------------------------#    
ratio = 1./16
output_file = out_dir+'data/wmt15/wmt15qe.train.tok.16.en'
make_file(ratio=ratio, input_dict=input_file, output_file=output_file)
#----------------------------------------#

#----------------------------------------#    
ratio = 1./64
output_file = out_dir+'data/wmt15/wmt15qe.train.tok.64.en'
make_file(ratio=ratio, input_dict=input_file, output_file=output_file)
#----------------------------------------#

#----------------------------------------#    
ratio = 1./256
output_file = out_dir+'data/wmt15/wmt15qe.train.tok.256.en'
make_file(ratio=ratio, input_dict=input_file, output_file=output_file)
#----------------------------------------#

#----------------------------------------#    
ratio = 1./1024
output_file = out_dir+'data/wmt15/wmt15qe.train.tok.1024.en'
make_file(ratio=ratio, input_dict=input_file, output_file=output_file)
#----------------------------------------#

#----------------------------------------#    
ratio = 1./2048
output_file = out_dir+'data/wmt15/wmt15qe.train.tok.2048.en'
make_file(ratio=ratio, input_dict=input_file, output_file=output_file)
#----------------------------------------#




