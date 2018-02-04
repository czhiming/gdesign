#!/bin/sh

qe_dir='/home/czm/workspace/QE_project'

data_dir=$qe_dir/data/wmt16/task1
vec_dir=$qe_dir/word2vec/vec
features_dir=$qe_dir/learning/data/features/wmt16/word2vec
word2vec=$qe_dir/word2vec

dim=$1
#dim_t=`expr $dim / 2`
dim_t=$2

python make_vector_pos.py -m $word2vec/model/wmt16qe.vectors.en.$dim.tok.bin -dim $dim \
	-i $data_dir/train.src -o $vec_dir/wmt16.train.src.$dim.vec -pos $data_dir/wmt16.train.src.pos.json -l en
python make_vector_pos.py -m $word2vec/model/wmt16qe.vectors.de.$dim_t.tok.bin -dim $dim_t \
	-i $data_dir/train.mt -o $vec_dir/wmt16.train.mt.$dim_t.vec -pos $data_dir/wmt16.train.mt.pos.json -l de
python make_vector_pos.py -m $word2vec/model/wmt16qe.vectors.en.$dim.tok.bin -dim $dim \
	-i $data_dir/test.src -o $vec_dir/wmt16.test.src.$dim.vec -pos $data_dir/wmt16.test.src.pos.json -l en
python make_vector_pos.py -m $word2vec/model/wmt16qe.vectors.de.$dim_t.tok.bin -dim $dim_t \
	-i $data_dir/test.mt -o $vec_dir/wmt16.test.mt.$dim_t.vec -pos $data_dir/wmt16.test.mt.pos.json -l de
	
python combine.py $vec_dir/wmt16.train.src.$dim.vec $vec_dir/wmt16.train.mt.$dim_t.vec $vec_dir/wmt16.train.$dim.pos.vec
python combine.py $vec_dir/wmt16.test.src.$dim.vec $vec_dir/wmt16.test.mt.$dim_t.vec $vec_dir/wmt16.test.$dim.pos.vec
cp $vec_dir/wmt16.train.$dim.pos.vec $features_dir
cp $vec_dir/wmt16.test.$dim.pos.vec $features_dir







