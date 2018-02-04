#!/bin/sh

import os
import sys

if len(sys.argv)<2:
    sys.exit()

file_names = sys.argv[1:]



for file_ in file_names:
    word_sets = set()
    word_length = 0
    length = 0
    for i,lines in enumerate(open(file_)):
        lines = lines.strip().split()
        for word in lines:
            word = word.strip()
            if word != '':
                word_length += 1
                if word not in word_sets:
                    word_sets.add(word)
        length += 1
    print file_
    print 'sentence num:',length
    print 'word(unique):',len(word_sets)
    print 'word:',word_length
    print






