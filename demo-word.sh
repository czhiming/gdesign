#!/bin/bash

BIN_DIR=Debug
TEXT_DATA=text8
VECTOR_DATA=text8-vector.bin

echo -----------------------------------------------------------------------------------------------------
echo -- Training vectors...
time $BIN_DIR/word2vec -train $TEXT_DATA -output $VECTOR_DATA -cbow 0 -size 200 -window 5 \
	-negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 1
echo -----------------------------------------------------------------------------------------------------












