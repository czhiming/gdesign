#!/bin/sh

qe_dir='/home/czm/workspace/QE_project'

data_dir=$qe_dir/data/wmt15/task1
vec_dir=$qe_dir/word2vec/vec
features_dir=$qe_dir/learning/data/features/wmt15/word2vec
word2vec=$qe_dir/word2vec

dim=$1
dim_t=$2
#dim_t=$dim

python make_vector.py -m $word2vec/model/wmt15qe.vectors.en.$dim.tok.bin -dim $dim \
	-i $data_dir/train.source -o $vec_dir/wmt15.train.source.$dim.vec
python make_vector.py -m $word2vec/model/wmt15qe.vectors.es.$dim_t.tok.bin -dim $dim_t \
	-i $data_dir/train.target -o $vec_dir/wmt15.train.target.$dim_t.vec
python make_vector.py -m $word2vec/model/wmt15qe.vectors.en.$dim.tok.bin -dim $dim \
	-i $data_dir/test.source -o $vec_dir/wmt15.test.source.$dim.vec
python make_vector.py -m $word2vec/model/wmt15qe.vectors.es.$dim_t.tok.bin -dim $dim_t \
	-i $data_dir/test.target -o $vec_dir/wmt15.test.target.$dim_t.vec
	
python combine.py $vec_dir/wmt15.train.source.$dim.vec $vec_dir/wmt15.train.target.$dim_t.vec $vec_dir/wmt15.train.$dim.vec
python combine.py $vec_dir/wmt15.test.source.$dim.vec $vec_dir/wmt15.test.target.$dim_t.vec $vec_dir/wmt15.test.$dim.vec
cp $vec_dir/wmt15.train.$dim.vec $features_dir
cp $vec_dir/wmt15.test.$dim.vec $features_dir







