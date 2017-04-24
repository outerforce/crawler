import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
from collections import Counter
import re
from nltk.stem.lancaster import LancasterStemmer
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import gensim
from sklearn import decomposition
import logging
import sklearn.feature_extraction.text as text
import numpy as np  # a conventional alias
import logging
import codecs

count = 0
List = []
with open('/home/irene/crawler/data/total.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    documentInfo = []
    for row in reader:
        issueKey = row[1]
        summary = row[2]
        desc = row[3]
        document = (summary + " " + desc).lower()
        count += 1
        #print(issueKey,document)
        print(count)
        tokens = nltk.word_tokenize(document)
        english_stopwords = stopwords.words('english')
        a = []
        # remove symbols and stopwords
        for word in tokens:
            if (not word in english_stopwords):
                if len(word)>1:
                    a.append(word)
        lancaster = nltk.LancasterStemmer()
        lwords = [lancaster.stem(t) for t in a]
        for i in lwords:
            List.append(i)
        print(lwords)
        documentInfo.append(lwords)
    # stemming process
    print(count)
    #print(List)
    #counts = Counter(List)
    #print(counts)
    print(documentInfo)
    train_set = documentInfo

# construct training corpus
    dictionary = Dictionary(train_set)
    corpus = [ dictionary.doc2bow(text) for text in train_set]
    print(corpus)
    print(dictionary)
# train lda model
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=30)
    print(lda)
    print(lda.print_topics(5))


#
# def lda_test(train_set):
#     # train corpus
#     dictionary = Dictionary(train_set)
#     corpus = [dictionary.doc2bow(text) for text in train_set]
#     print(corpus)
#     print(dictionary)
#     # lda model training
#     lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=50)
#     print(lda)
#     return (lda.print_topics(50))