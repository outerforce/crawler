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




count = 0

otherlist = []

summary = "/home/irene/crawler/data/sum.csv"
total = "/home/irene/crawler/data/total.csv"
keyword = "/home/irene/crawler/txt/train.csv"


# read keyword as a list of bag of words
def get_keyword(path):
    List = []
    with open(path, newline='\n', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for line in reader:
            List.append(line)
            # print(len(List))
    #print(List)
    return List


# remove tokens length<2
def remove_stopword(text):
    tokens = nltk.word_tokenize(text.lower())
    english_stopwords = stopwords.words('english')
    # remove symbols and stopwords
    a = []
    documentInfo = []
    for word in tokens:
        if (not word in english_stopwords) and (len(word) > 1):
            a.append(word)
            #stemming process
            #lancaster = nltk.LancasterStemmer()
            #lwords = [lancaster.stem(t) for t in a]
            #for i in lwords:
             #   List.append(i)
            #print(lwords)
            #documentInfo.append(lwords)
    return a


# category into topics, tokens is the processed text ,topic process
def get_topicvector(topic, tokens):
    # List = get_keyword(keyword)
    sum = 0
    count = 0
    resultList = []
    isToken = False
    for i in topic:
        for k in range(len(tokens)):
            if tokens[k].find(i) != -1:
                print(tokens[k])
                count = count + 1
                resultList.append(1)
                isToken = True
                break
        if isToken == False:
            resultList.append(0)
        else:
            isToken = False
    #print("--------vector" + str(len(resultList)) + "------------")
    # print(count)
    for i in range(len(resultList)):
        sum += resultList[i]
    if sum == 0:
        return []
    print(resultList)
    return resultList


# transform keywords into vector, add weight here
def createCaseArray(type):
    newlist = []
    length = len(type)
    #print("------------orignin----------" + str(length) + "--------------")
    for i in range(length):
        newlist.append(1/length)
        #print(newlist)
    return newlist


# array1 is list of tokens in document
def getCos_topic(tokens):
    List = get_keyword(keyword)
    component = List[0] + List[1] + List[2] + List[3]
    print(component)
    function = List[4] + List[5]
    data = List[6]
    rootcause = List[7] + List[8] + List[9]
    type = []

    t1 = get_topicvector(component, tokens)
    t2 = get_topicvector(function, tokens)
    t3 = get_topicvector(data, tokens)
    t4 = get_topicvector(rootcause, tokens)

    a1 = createCaseArray(component)
    a2 = createCaseArray(function)
    a3 = createCaseArray(data)
    a4 = createCaseArray(rootcause)
    print("-------------" + "topic similarity -----------------------------")
    minnum = 0
    if t1 != []:
        num1 = cosine_similarity(t1, a1)
        print(num1)
    else:
        num1 = 0
    if t2 != []:
        num2 = cosine_similarity(t2, a2)
    else:
        num2 = 0
    if t3 != []:
        num3 = cosine_similarity(t3, a3)
    else:
        num3 = 0
    if t4 != []:
        num4 = cosine_similarity(t4, a4)
    else:
        num4 = 0
    sum = num1 + num2 + num3 + num4
    minnum = min(num1, num2, num3, num4)
    #num = [num1, num2, num3, num4]
    if (sum != 0):
        print(minnum)
        if (num1 == minnum):
            #minnum = num2
            type.append("component")
        if (num2 == minnum):
            #minnum = num3
            type.append("function")
        if (num3 == minnum):
            #minmun = num4
            type.append("data")
        if (num4 == minnum):
            type.append("rootcause")
    else:
        return ["other"]
    print(type)
    return type


def get_Costype(tokens):
    List = get_keyword(keyword)
    type = []
    t0 = get_topicvector(List[0], tokens)
    t1 = get_topicvector(List[1], tokens)
    t2 = get_topicvector(List[2], tokens)
    t3 = get_topicvector(List[3], tokens)
    t4 = get_topicvector(List[4], tokens)
    t5 = get_topicvector(List[5], tokens)
    t6 = get_topicvector(List[6], tokens)
    t7 = get_topicvector(List[7], tokens)
    t8 = get_topicvector(List[8], tokens)
    t9 = get_topicvector(List[9], tokens)

    b0 = createCaseArray(List[0])
    b1 = createCaseArray(List[1])
    b2 = createCaseArray(List[2])
    b3 = createCaseArray(List[3])
    b4 = createCaseArray(List[4])
    b5 = createCaseArray(List[5])
    b6 = createCaseArray(List[6])
    b7 = createCaseArray(List[7])
    b8 = createCaseArray(List[8])
    b9 = createCaseArray(List[9])

    print("-------------" + "type similarity -----------------------------")

    if t0 != []:
        num1 = cosine_similarity(t0, b0)
        print(num1)
    else:
        num1 = 0
    if t1 != []:
        num2 = cosine_similarity(t1, b1)
    else:
        num2 = 0
    if t2 != []:
        num3 = cosine_similarity(t2, b2)
    else:
        num3 = 0
    if t3 != []:
        num4 = cosine_similarity(t3, b3)
    else:
        num4 = 0
    if t4 != []:
        num5 = cosine_similarity(t4, b4)
    else:
        num5 = 0
    if t5 != []:
        num6 = cosine_similarity(t5, b5)
    else:
        num6 = 0
    if t6 != []:
        num7 = cosine_similarity(t6, b6)
    else:
        num7 = 0
    if t7 != []:
        num8 = cosine_similarity(t7, b7)
    else:
        num8 = 0
    if t8 != []:
        num9 = cosine_similarity(t8, b8)
    else:
        num9 = 0
    if t9 != []:
        num10 = cosine_similarity(t9, b9)
    else:
        num10 = 0
    minnum = 0
    sum = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    num = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
    if (sum != 0):
        minnum = min(num)
        print(min)
        if (num1 == minnum):
            type.append("environment")
        if (num2 == minnum):
            type.append("api")
        if (num3 == minnum):
            type.append("network")
        if (num4 == minnum):
            type.append("framework")
        if (num5 == minnum):
            type.append("functional")
        if (num6 == minnum):
            type.append("security")
        if (num7 == minnum):
            type.append("data")
        if (num8 == minnum):
            type.append("semantic")
        if (num9 == minnum):
            type.append("memory")
        if (num10 == minnum):
            type.append("concurrency")
    else:
        return ["other"]
    return type


# input for summary + desc
def getcsv2(path):
    with open(path, newline='', encoding='utf-8') as f:
        count = 0
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        # pair = []
        dic = {}
        for row in reader:
            count = count + 1
            # project = row[0]
            issueKey = row[1]
            summary = row[2]
            desc = row[3]
            document = (summary + " " + desc).lower()
            # pair.append(issueKey, document)
            dic[issueKey] = remove_stopword(document)
        # print(count)
        return dic


# input for summary
def getcsv1(path):
    with open(path, newline='', encoding='utf-8') as f:
        count = 0
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        # pair = []
        dic = {}
        for row in reader:
            count = count + 1
            # project = row[0]
            issueKey = row[1]
            summary = row[2].lower()
            dic[issueKey] = remove_stopword(summary)
        # print(count)
        return dic

def get_topicResult():
    d1 = getcsv1(total)
    m = [0, 0, 0, 0, 0]
    for key in d1:
        # list of tokens in a document
        # result = []
        value = d1[key]
        type = getCos_topic(value)
        for i in range(len(type)):
            if type[i] is "component":
                d1[key].append('component')
                m[0] += 1
            if type[i] is "function":
                d1[key].append('function')
                m[1] += 1
            if type[i] is "data":
                d1[key].append('data')
                m[2] += 1
            if type[i] is "rootcause":
                d1[key].append('rootcause')
                m[3] += 1
            if type[i] is "other":
                d1[key].append('other')
                m[4] += 1
    print(m)
def get_cateResult():
    d2 = getcsv2(total)
    n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for key in d2:
        # list of tokens in a document
        # result = []
        value = d2[key]
        type = get_Costype(value)
        for i in range(len(type)):
            if type[i] is "environment":
                d2[key].append('environment')
                n[0] += 1
            if type[i] is "api":
                d2[key].append('api')
                n[1] += 1
            if type[i] is "network":
                d2[key].append('network')
                n[2] += 1
            if type[i] is "framework":
                d2[key].append('framework')
                n[3] += 1
            if type[i] is "functional":
                d2[key].append('functional')
                n[4] += 1
            if type[i] is "data":
                d2[key].append('data')
                n[5] += 1
            if type[i] is "security":
                d2[key].append('security')
                n[6] += 1
            if type[i] is "semantic":
                d2[key].append('semantic')
                n[7] += 1
            if type[i] is "memory":
                d2[key].append('memory')
                n[8] += 1
            if type[i] is "concurrency":
                d2[key].append('concurrency')
                n[9] += 1
            if type[i] is "other":
                d2[key].append('other')
                n[10] += 1
    print(n)



def main():
    get_topicResult()
    #get_cateResult()


if __name__ == '__main__':
    main()