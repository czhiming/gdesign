#!/bin/sh
###########################
#  word2vec (c)
###########################

qe_dir='/home/czm/workspace/QE_project'

root_dir=$qe_dir/word2vec/word2vec-master/bin

dim=$1

time $root_dir/word2vec -train $qe_dir/data/wmt15/wmt15qe.train.tok.en -output $qe_dir/word2vec/model/wmt15qe.vectors.en.$dim.tok.bin -cbow 1 -size $dim -window 10 -negative 10 -hs 0 -sample 1e-5 -threads 20 -binary 1 -iter 15

time $root_dir/word2vec -train $qe_dir/data/wmt15/wmt15qe.train.tok.es -output $qe_dir/word2vec/model/wmt15qe.vectors.es.$dim.tok.bin -cbow 1 -size $dim -window 10 -negative 10 -hs 0 -sample 1e-5 -threads 20 -binary 1 -iter 15















