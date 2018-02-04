#coding:utf8

import gensim
import sys
import numpy
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-dim',type=int,required=True,help='the dimension of the vector')
parser.add_argument('-m',type=str,required=True,help='the model use for training word embedding')
parser.add_argument('-i',type=str,required=True,help='the input file name')
parser.add_argument('-o',type=str,required=True,help='the output file name')

args = parser.parse_args()


print 'model:',args.m
model = gensim.models.KeyedVectors.load_word2vec_format(args.m,binary=True)

print 'file:',args.i
with open(args.o,'w') as fp:
    for lines in open(args.i):
        vector = []
        word_list = lines.strip().split(' ')
        
        #mean
        for word in word_list:
            try:
                vector.append(list(model[word]))
            except:
                vector.append(list(numpy.zeros(int(args.dim))))
        vector = numpy.array(vector)
        vector = list(vector.mean(axis=0))
        #addition
        """
        for word in word_list:
            try:
                vector.append(list(model[word]))
            except:
                vector.append(list(numpy.zeros(int(args.dim))))
        vector = numpy.array(vector)
        vector = list(vector.sum(axis=0))
        """
        #multiplication
       	""" 
        for word in word_list:
            try:
                vector.append(list(model[word]))
            except:
                #vector.append(list(numpy.zeros(int(args.dim))))
                pass
        vector = numpy.array(vector)
        result = numpy.ones(int(args.dim))
        for vec in vector:
            result *= vec
        vector = list(result)
        """
        
        result = map(lambda x:str(x),vector)
        fp.writelines('\t'.join(result)+'\n')


