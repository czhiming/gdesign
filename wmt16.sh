#!/bin/sh

qe_dir='/home/czm/workspace/QE_project'
learning=$qe_dir/learning

#####################
dim=512
#echo `expr $dim / 2`
######################

:<<!
#combine
$qe_dir/corpus/combine_data_wmt16.sh

echo '========================================='
!
#train word2vec
#./train_w2v_wmt16.sh $dim
#./train_w2v_wmt16.sh `expr $dim / 2`
#./train_w2v_wmt16.sh `expr $dim \* 4`
#./train_w2v_wmt16.sh `expr $dim \* 2`
#./train_w2v_wmt16.sh `expr $dim / 4`
#./train_w2v_wmt16.sh `expr $dim / 8`
#./train_w2v_wmt16.sh `expr $dim / 16`
#./train_w2v_wmt16.sh `expr $dim / 32`
#./train_w2v_wmt16.sh `expr $dim \* 8`
#./train_w2v_wmt16.sh `expr $dim \* 16`

echo '========================================='

#make vector
#./make_vector_wmt16.sh `expr $dim / 2`

echo '========================================='

#train svm
python $learning/src/learn_model.py $learning/config/svr.cfg

echo '========================================='

#evaluate
$learning/evaluateWMT.pl $learning/ref.csv 100 $learning/predicted.csv












