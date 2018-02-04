#-*- coding:utf-8 -*-
'''
Created on 2017年2月28日

@author: Administrator
'''
import numpy

def get_vocab(corpus):
    vocab = {}
    for i,line in enumerate(corpus):
        line = line.split()
        j = i
        for word in line:
            if word not in vocab:
                vocab[word] = 1
            else:
                if j == i:
                    vocab[word] += 1
            j += 1
    return vocab

def count(word_list):
    vocab = {}
    for word in word_list:
        if word not in vocab:
            vocab[word] = 1
        else:
            vocab[word] += 1
    return vocab

def tf_idf(file_name):
    corpus = []
    for lines in open(file_name):
        lines = lines.strip()
        corpus.append(lines)

    N = len(corpus)
    vocab = get_vocab(corpus)
    vec = []
    for line in corpus:
        word_count = count(line.split())
        result = word_count.copy()
        for word in word_count:
            tf = word_count[word]
            idf = numpy.log(float(N)/(1+vocab[word]))
            tfidf = tf*idf
            result[word] = tfidf
        vec.append(result)
    return vec












if __name__ == '__main__':
    pass