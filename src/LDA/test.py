import nltk
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from nltk.corpus import stopwords
import csv
from sklearn.metrics.pairwise import cosine_similarity
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
a =[0,0,0,0]
b =[0,0,0,0,0,0,0,0,0]
