#!/bin/sh

qe_dir='/home/czm/workspace/QE_project'

data_dir=$qe_dir/data/wmt16/task1
vec_dir=$qe_dir/word2vec/vec
features_dir=$qe_dir/learning/data/features/wmt16/word2vec
word2vec=$qe_dir/word2vec


dim=512
python make_vector.py -m $word2vec/model/wmt16qe.vectors.en.$dim.tok.bin -dim $dim \
	-i $data_dir/train.src -o $vec_dir/train.src.$dim.wmt16.vec -l en
	
python make_vector.py -m $word2vec/model/wmt16qe.vectors.de.$dim.tok.bin -dim $dim \
	-i $data_dir/train.mt -o $vec_dir/train.mt.$dim.wmt16.vec -l de




