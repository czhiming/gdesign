#!/bin/sh
###########################
#  word2vec (c)
###########################

current_dir=`pwd`

root_dir=$current_dir/word2vec-master/bin
dim=$1

time $root_dir/word2vec -train $current_dir/data/en-de/train.bpe.en -output $current_dir/model/wmt17qe.vectors.en.$dim.tok.bin -cbow 1 -size $dim -window 10 -negative 10 -hs 0 -sample 1e-5 -threads 20 -binary 1 -iter 15

time $root_dir/word2vec -train $current_dir/data/en-de/train.bpe.de -output $current_dir/model/wmt17qe.vectors.de.$dim.tok.bin -cbow 1 -size $dim -window 10 -negative 10 -hs 0 -sample 1e-5 -threads 20 -binary 1 -iter 15










