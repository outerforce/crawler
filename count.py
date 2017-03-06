import glob
import json
import csv
import collections
from urllib import request
from urllib.request import urlopen
import re
from lxml import html
from bs4 import BeautifulSoup


file = open("/home/irene/crawler/output.txt", "r")
L = []
for line in file:
    L.append(line.strip())
#list = glob.glob(("/home/irene/crawler/temp/*"))
count = 0
# for i in L:
#     url = i
#     # print(url)
#     page = request.urlopen(url)
#     soup = BeautifulSoup(page, "lxml")
#     tabletitle = soup.find_all("tr", "issuerow")
#     # tbinfo = soup.find_all("table","grid")
#     num = len(tabletitle)
#     count += num
# print(count)
import codecs
list = glob.glob(("/home/irene/crawler/temp/*"))
for i in list:
    f=codecs.open(i, 'r', 'utf-8')
    document= BeautifulSoup(f.read(),"lxml")
    print(document)
    tabletitle = document.find_all("tr", "issuerow")
    num = len(tabletitle)
    count += num
    print(count)
print(count)