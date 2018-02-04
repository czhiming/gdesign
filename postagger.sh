#!/bin/sh

qe_dir='/home/czm/workspace/QE_project'

en_de=$qe_dir/data/wmt17/task1_en-de_training-dev/sentence_level
de_en=$qe_dir/data/wmt17/task1_de-en_training-dev/sentence_level

#只对目标语言句子进行，词性标注
python postagger.py -i $en_de/train.mt -o $en_de/wmt17.en-de.train.mt.pos.json -l de
python postagger.py -i $en_de/dev.mt -o $en_de/wmt17.en-de.dev.mt.pos.json -l de

python postagger.py -i $de_en/train.mt -o $de_en/wmt17.de-en.train.mt.pos.json -l en
python postagger.py -i $de_en/dev.mt -o $de_en/wmt17.de-en.dev.mt.pos.json -l en





