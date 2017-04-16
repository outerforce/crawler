import nltk
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk.corpus import stopwords
import csv
import difflib
from sklearn.metrics.pairwise import cosine_similarity
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

path = "/home/irene/crawler/add.csv"


def remove_stopword(summary):
    tokens = nltk.word_tokenize(summary.lower())
    english_stopwords = stopwords.words('english')
    # remove symbols and stopwords
    a = []
    for word in tokens:
        if (not word in english_stopwords) and (not word in english_punctuations):
            a.append(word)
    return a


def lda_test(train_set):
    # train corpus
    dictionary = Dictionary(train_set)
    corpus = [dictionary.doc2bow(text) for text in train_set]
    print(corpus)
    print(dictionary)
    # lda model training
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=50)
    print(lda)
    return (lda.print_topics(50))


# caselist is the compoenent list...
def case_process(caselist, tokens):
    sum = 0
    count = 0
    resultlist = []
    istoken = False
    for i in caselist:
        for k in range(len(tokens)):
            if tokens[k].find(i) != -1:
                count = count + 1
        resultlist.append(count)
        #     if tokens[k].find(i) != -1:
        #         resultlist.append(1)
        #         istoken = True
        #         break
        #         # else:
        #         #     resultlist.append(0)
        # if istoken == False:
        #     resultlist.append(0)
        # else:
        #     istoken = False
    # print(resultlist)
    for j in range(len(resultlist)):
        sum = sum + resultlist[j]
    if sum == 0:
        return []
    return resultlist


# array1 and array2 are not normalized
# def CosThetaBetweenArray2(array1, array2):
#     sum_square_1 = np.sum((array1 ** 2)) ** 0.5
#     sum_square_2 = np.sum((array2 ** 2)) ** 0.5
#     dot_product = np.dot(array1, array2)
#     cos_theta = dot_product / (sum_square_1 * sum_square_2)
#     return cos_theta

def createCaseArray(case):
    newlist = []
    length = len(case)
    for i in range(length):
        newlist.append(1 / length)
    return newlist


# array1 is list of tokens in documentcase
def getCos(array1, a1, a2, a3, a4):
    # comp_r = case_process(component, array1)
    # print(len(comp_r))
    type = []
    min = 0
    component_r = case_process(component, array1)
    functional_r = case_process(functional, array1)
    datasource_r = case_process(datasource, array1)
    rootcause_r = case_process(rootcause, array1)

    envi_r = case_process(environment, array1)
    api_r = case_process(api, array1)
    net_r = case_process(network, array1)
    frame_r = case_process(framework, array1)

    func_r = case_process(functional, array1)

    data_r = case_process(datasource, array1)
    secur_r = case_process(security, array1)
    seman_r = case_process(semantic, array1)
    mem_r = case_process(memory, array1)
    # root_r = case_process(rootcause, array1)
    if component_r != []:
        num1 = cosine_similarity(component_r, a1)
    else:
        num1 = 0
    if functional_r != []:
        num2 = cosine_similarity(functional_r, a2)
    else:
        num2 = 0
    if datasource_r != []:
        num3 = cosine_similarity(datasource_r, a3)
    else:
        num3 = 0
    if rootcause_r != []:
        num4 = cosine_similarity(rootcause_r, a4)
    else:
        num4 = 0
        # if (envi_r != []):
        #     num1 = cosine_similarity(envi_r, a1)
        #     # vector1 = mat(comp_r)
        #     # vector2 = mat(a1)
        #     # num1 = dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))
        # else:
        #     num1 = 0
        # if (api_r != []):
        #     num2 = cosine_similarity(api_r, a2)
        # else:
        #     num2 = 0
        # if (net_r != []):
        #     num3 = cosine_similarity(net_r, a3)
        # else:
        #     num3 = 0
        # if (frame_r != []):
        #     num4 = cosine_similarity(frame_r, a4)
        # else:
        #     num4 = 0
        #
        # if (func_r != []):
        #     num5 = cosine_similarity(func_r, a5)
        # else:
        #     num5 = 0
        # if (data_r != []):
        #     num6 = cosine_similarity(data_r, a6)
        # else:
        #     num6 = 0
        # if (secur_r != []):
        #     num7 = cosine_similarity(secur_r, a7)
        # else:
        #     num7 = 0
        # if (seman_r != []):
        #     num8 = cosine_similarity(seman_r, a8)
        # else:
        #     num8 = 0
        # if (mem_r != []):
        #     num9 = cosine_similarity(mem_r, a9)
        # else:
        #     num9 = 0
        # sum = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
    sum = num1 + num2 + num3 + num4
    if (sum != 0):
        min = num1
        # type="environment"
        if (num2 < min):
            min = num2
            # type = "api"
        if (num3 < min):
            min = num3
            # type = "network"
        if (num4 < min):
            min = num4
            # type = "framework"
            # if (num5 < min):
            #     min = num5
            #     # type = "functional"
            # if (num6 < min):
            #     min = num6
            #     # type = "datasource"
            # if (num7 < min):
            #     min = num7
            #     # type = "security"
            # if (num8 < min):
            #     min = num8
            #     # type = "semantic"
            # if (num9 < min):
            #     min = num9
            # type = "memory"

        # d = {"environment": num1, "api": num2, "network": num3, "framework": num4,
        #      "functional": num5, "datasource": num6, "security": num7, "semantic": num8,
        #      "memory": num9}
        # min = min(d.items(), key=lambda x: x[1])[1]
        if (min == num1):
            type.append("component")
        if (min == num2):
            type.append("functional")
        if (min == num3):
            type.append("datasource")
        if (min == num4):
            type.append("rootcause")
            # if (min == num5):
            #     type.append("functional")
            # if (min == num6):
            #     type.append("datasource")
            # if (min == num7):
            #     type.append("security")
            # if (min == num8):
            #     type.append("semantic")
            # if (min == num9):
            #     type.append("memory")

    else:
        return ["other"]
    return type


# def getRatio(array1, a1, a2, a3, a4, a5, a6, a7, a8, a9):
#     envi_r = case_process(environment, array1)
#     api_r = case_process(api, array1)
#     net_r = case_process(network, array1)
#     frame_r = case_process(framework, array1)
#
#     func_r = case_process(functional, array1)
#
#     data_r = case_process(datasource, array1)
#     secur_r = case_process(security, array1)
#     seman_r = case_process(semantic, array1)
#     mem_r = case_process(memory, array1)
#     sm1 = difflib.SequenceMatcher(None, a1, envi_r).ratio()
#     sm2 = difflib.SequenceMatcher(None, a2, api_r).ratio()
#     sm3 = difflib.SequenceMatcher(None, a3, net_r).ratio()
#     sm4 = difflib.SequenceMatcher(None, a4, frame_r).ratio()
#     sm5 = difflib.SequenceMatcher(None, a5, func_r).ratio()
#     sm6 = difflib.SequenceMatcher(None, a6, data_r).ratio()
#     sm7 = difflib.SequenceMatcher(None, a7, secur_r).ratio()
#     sm8 = difflib.SequenceMatcher(None, a8, seman_r).ratio()
#     sm9 = difflib.SequenceMatcher(None, a9, mem_r).ratio()
#     d = {"environment": sm1, "api": sm2, "network": sm3, "framework": sm4, "functional": sm5, "datasource": sm6,
#          "security": sm7, "semantic": sm8, "memory": sm9}
#     type = min(d.items(), key=lambda x: x[1])[0]
#     return type


# def getCos2(array1, b1, b2, b3, b4):
#     envir_r = case_process(environment, array1)
#
#     api_r = case_process(api, array1)
#
#     net_r = case_process(network, array1)
#
#     frame_r = case_process(framework, array1)
#
#     num1 = cosine_similarity(envir_r, b1)
#
#     print(num1)
#     num2 = cosine_similarity(api_r, b2)
#     num3 = cosine_similarity(net_r, b3)
#     num4 = cosine_similarity(frame_r, b4)
#     d = {"environment": num1, "api": num2, "network": num3, "framework": num4}
#     type = min(d.items(), key=lambda x: x[1])[0]
#     return type

# def getCos3(array1, r1, r2):
#     sem_r = case_process(semantic, array1)
#
#     mem_r = case_process(memory, array1)
#
#     num1 = cosine_similarity(sem_r, r1)
#
#     print(num1)
#     num2 = cosine_similarity(mem_r, r2)
#
#     d = {"semantic": num1, "memory": num2}
#     type = min(d.items(), key=lambda x: x[1])[0]
#     return type


def getcsv(path):
    with open(path, newline='', encoding='utf-8') as f:
        count = 0
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        d = {}
        pair = []
        for row in reader:
            count = count + 1
            print(count)
            project = row[0]
            issueKey = row[1]
            summary = row[2]
            desc = row[3]
            document = (summary + " " + desc).lower()
            pair.append((issueKey, document))
            d[issueKey] = remove_stopword(document)
            # lancaster = nltk.LancasterStemmer()
            # lwords = [lancaster.stem(t) for t in a]
        return d


def main():
    d = getcsv(path)
    # a1 = createCaseArray(component)
    # a4 = createCaseArray(rootcause)
    # a1 = createCaseArray(environment)
    # a2 = createCaseArray(api)
    # a3 = createCaseArray(network)
    # a4 = createCaseArray(framework)
    # a5 = createCaseArray(functional)
    # a6 = createCaseArray(datasource)
    # a7 = createCaseArray(security)
    # a8 = createCaseArray(semantic)
    # a9 = createCaseArray(memory)
    a1 = createCaseArray(component)
    a2 = createCaseArray(functional)
    a3 = createCaseArray(datasource)
    a4 = createCaseArray(rootcause)
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    # n5 = 0
    # n6 = 0
    # n7 = 0
    # n8 = 0
    # n9 = 0
    n10 = 0
    for key in d:
        # list of tokens in a document
        type = []
        value = d[key]
        type = getCos(value, a1, a2, a3, a4)
        for i in range(len(type)):
            if type[i] is "component":
                d[key].append('component')
                n1 += 1
            if type[i] is "functional":
                d[key].append('functional')
                n2 += 1
            if type[i] is "datasource":
                d[key].append('datasource')
                n3 += 1
            if type[i] is "rootcause":
                d[key].append('rootcause')
                n4 += 1
            if type[i] is "other":
                d[key].append('other')
                n10 += 1
                # if type[i] is "environment":
                #     d[key].append('environment')
                #     n1 += 1
                # if type[i] is "api":
                #     d[key].append('api')
                #     n2 += 1
                # if type[i] is "network":
                #     d[key].append('network')
                #     n3 += 1
                # if type[i] is "framework":
                #     d[key].append('framework')
                #     n4 += 1
                # if type[i] is "functional":
                #     d[key].append('functional')
                #     n5 += 1
                # if type[i] is "datasource":
                #     d[key].append('datasource')
                #     n6 += 1
                # if type[i] is "security":
                #     d[key].append('security')
                #     n7 += 1
                # if type[i] is "semantic":
                #     d[key].append('semantic')
                #     n8 += 1
                # if type[i] is "memory":
                #     d[key].append('memory')
                #     n9 += 1
                # if type[i] is "other":
                #     d[key].append('other')
                #     n10 += 1
                otherlist.append(value)
    print(n1, n2, n3, n4, n10)
    print(otherlist)
    # print(d)

    # for key1 in d:
    #     value = d[key1]
    #     type = value[-1]
    #     print(type)
    #     b1 = createCaseArray(environment)
    #     b2 = createCaseArray(api)
    #     b3 = createCaseArray(network)
    #     b4 = createCaseArray(framework)
    #     r1 = createCaseArray(semantic)
    #     r2 = createCaseArray(memory)
    #     m1 = 0
    #     m2 = 0
    #     m3 = 0
    #     m4 = 0
    #     k1 = 0
    #     k2 = 0
    #     if type is "component":
    #         newtype = getCos2(value, b1, b2, b3, b4)
    #         if newtype is "environment":
    #             m1 += 1
    #         if newtype is "api":
    #             m2 += 1
    #         if newtype is "network":
    #             m3 += 1
    #         if newtype is "framework":
    #             m4 += 1
    #     print(m1, m2, m3, m4)
    #     if type is "rootcause":
    #         newtype = getCos3(value, r1, r2)
    #         if newtype is "semantic":
    #             k1+=1
    #         if newtype is "memory":
    #             k2+=1
    #     print(k1,k2)


if __name__ == '__main__':
    main()

    # documentInfo.append(d[1])
    # print(documentInfo)

    # for i in List:
    #     counts = Counter(i)
    #     print(counts)
    #     for i in# array1 is list of tokens in documentcaseresultlist


    # documentInfo.append(lwords)
    # stemming process
    # print(texts_stemmed[0])
    # print(count)
    # counts = Counter(List)
    # print(counts)
    # print(documentInfo)
