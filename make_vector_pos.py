#coding:utf8

import gensim
import sys
import numpy
import argparse
import nltk
from nltk.tag.stanford import StanfordPOSTagger
import json

#print st.tag("And it doesn't show up on an IQ test .".split())
#实词标签
en_real_words = set(['CD','JJ','JJR','JJS','NN','NNP','NNPS','NNS','PRP','PRP$','RB','RBR','RBS',
                    'VB','VBD','VBG','VBN','VBP','VBZ','WRB'])
de_real_words = set(['ADJA','ADJD','CARD','NN','NE','PDS','PDAT','PIS','PIAT','PIDAT','PPER','PPOSS',
                    'PPOSAT','PRELS','PRELAT','PRF','PWS','PWAT','PWAV','PTKA','VVFIN','VVINF','VVIZU',
                    'VVPP','VAFIN','VAIMP','VAINF','VAPP','VMFIN','VMINF','VMPP','ADV','ART','KOUI','KOUS','KON','KOKOM','PAV'])
#名词，动词，形容词
de_label1 = [('ADJA','ADJD'),('NN','NE'),('VVFIN','VVINF','VVIZU','VVPP','VAFIN',
                    'VAIMP','VAINF','VAPP','VMFIN','VMINF','VMPP')]
w = [1,0.6,0.6,0.1]

def get_index(label,label_dict):
    for i,label_ in enumerate(label_dict):
        if label in label_:
            return i
    return -1

parser = argparse.ArgumentParser()

parser.add_argument('-dim',type=int,required=True,help='the dimension of the vector')
parser.add_argument('-m',type=str,required=True,help='the model use for training word embedding')
parser.add_argument('-i',type=str,required=True,help='the input file name')
parser.add_argument('-o',type=str,required=True,help='the output file name')
parser.add_argument('-pos',type=str,required=False,help='the pos file')
parser.add_argument('-l',type=str,required=True,help='the language')

args = parser.parse_args()

pos_dict = None
if args.l == 'de':
    with open(args.pos) as fp:
        pos_dict = json.load(fp)

print 'model:',args.m
#model = gensim.models.Word2Vec.load_word2vec_format(args.m,binary=True)
model = gensim.models.KeyedVectors.load_word2vec_format(args.m,binary=True)

print 'file:',args.i
with open(args.o,'w') as fp:
    for k,lines in enumerate(open(args.i)):
        vector = []
        weights = []
        word_list = lines.strip().split()

        for j,word in enumerate(word_list):
            try:
                if pos_dict is not None:
                    index = get_index(pos_dict[str(k)][j][1],de_label1)
                    if index != -1:
                        vector.append(list(model[word]))
                        weights.append(w[index])  #实词权重
                    else:
                        vector.append(list(model[word]))
                        weights.append(w[-1])  #虚词权重
                else:
                    vector.append(list(model[word]))
            except:
                vector.append(list(numpy.zeros(int(args.dim))))
                weights.append(w[-1])

	if pos_dict is not None:
            vector = numpy.array(vector)
            weights = numpy.array(weights)
            weights = weights[:,None]
            vector = vector*weights
	else:
	    vector = numpy.array(vector)

        vector = list(numpy.mean(vector,axis=0))
        result = map(lambda x:str(x),vector)
        fp.writelines('\t'.join(result)+'\n')


