#coding:utf8


from nltk.tag.stanford import StanfordPOSTagger
import json
import sys
from collections import OrderedDict
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i',type=str,required=True,help='the input file name')
parser.add_argument('-o',type=str,required=True,help='the output file name')
parser.add_argument('-l',type=str,required=True,help='the language of the input')

args = parser.parse_args()


pos_dict = OrderedDict()
tag = StanfordPOSTagger

pos = None
if args.l == 'en':
    pos = StanfordPOSTagger('wsj-0-18-bidirectional-distsim.tagger')
elif args.l == 'de':
    pos = StanfordPOSTagger('german-hgc.tagger')
elif args.l == 'es':
    pos = StanfordPOSTagger('spanish.tagger')

print 'file:',args.i
with open(args.i) as fp:
    total = len(fp.readlines())

with open(args.o,'w') as fp:
    for i,lines in enumerate(open(args.i)):
        lines = lines.strip().split()
        pos_dict[i] = pos.tag(lines)
        print args.i,'the line number: %s/%s' % (i+1,total)
    print len(pos_dict)
    print '==============================='
    json.dump(pos_dict,fp)













