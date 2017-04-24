import nltk
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk.corpus import stopwords
import csv
from sklearn.metrics.pairwise import cosine_similarity
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import difflib
import numpy as np
from numpy import *
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from collections import Counter
import re
import gensim
from sklearn import decomposition
import logging
import numpy as np
import codecs

summary = "/home/irene/crawler/data/sum.csv"
total = "/home/irene/crawler/data/total.csv"
keyword = "/home/irene/crawler/txt/train.csv"
def getcsv(path):
    with open(path, newline='', encoding='utf-8') as f:
        count = 0
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        text = ""
        #dic = {}
        for row in reader:
            count = count + 1
            #project = row[0]
            issueKey = row[1]
            summary = row[2]
            desc = row[3]
            document = (summary + " " + desc).lower()
            text = text + " " + (remove_stopword(document))
            #pair.append(issueKey, document)
            #dic[issueKey] = remove_stopword(document)
        print(count)
        return text

# remove tokens length<2
def remove_stopword(text):
    tokens = nltk.word_tokenize(text.lower())
    english_stopwords = stopwords.words('english')
    # remove symbols and stopwords
    a = ""
    for word in tokens:
        if (not word in english_stopwords) and (len(word) > 1):
            a=a+word
            # stemming process
            # lancaster = nltk.LancasterStemmer()
            # lwords = [lancaster.stem(t) for t in a]
            # for i in lwords:
            #     documentInfo.append(i)
            # print(lwords)
    return a

def tfidf(path):
    corpus = getcsv(path)
    #corpus = []
    vectorizer = CountVectorizer()  # transform text into term frequency matrix, a[i][j] represents the frequency of j in doc i
    transformer = TfidfTransformer()  # cal tfidf weight of each term
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()  # get all terms in bag of words
    weight = tfidf.toarray()

    sFilePath = '/home/irene/crawler/txt'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)
    #write into files
    f = open(sFilePath + '/'+'tfidf.txt', 'w+')
    for i in range(len(weight)):
        print(u"--------Writing all the tf-idf in the", i, u" file into ", sFilePath + '/' + str.zfill(i,5) + '.txt', "--------")
        for j in range(len(word)):
            f.write(word[j] + "	" + str(weight[i][j]) + "\n")
    f.close()


def main():
    #getcsv(total)
    tfidf(total)

if __name__ == '__main__':
    main()



