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
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    #f = open(sFilePath + '/' + str.zfill(i, 5) + '.txt', 'w+')
    # for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    #     print
    #     u"-------这里输出第", i, u"类文本的词语tf-idf权重------"
    #     for j in range(len(word)):
    #         print(word[j], weight[i][j])

    sFilePath = '/home/irene/crawler/txt'
    if not os.path.exists(sFilePath):
        os.mkdir(sFilePath)

    # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
        # 这里将每份文档词语的TF-IDF写入tfidffile文件夹中保存
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



