#!/usr/bin/python
# -*- coding: UTF-8 -*-
import glob
import json
import csv
import collections
from urllib import request
from urllib.request import urlopen
import re
from lxml import html
import time
from bs4 import BeautifulSoup

# file = open("/home/irene/crawler/output.txt", "r")
# L = []
# for line in file:
#     L.append(line.strip())
#list = glob.glob(("/home/irene/crawler/temp/*"))

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
list = glob.glob(("/home/irene/crawler/temp2/*"))
result =[]
count = 0
with open('second.csv', 'w', newline='') as csvfile:
    for i in list:
        f=codecs.open(i, 'r', 'utf-8')
        document= BeautifulSoup(f.read(),"lxml")
        #print(document)
        issueKey = document.find("h3","formtitle").get_text().strip()
        desc = document.find("td", id="descriptionArea").get_text().strip()
        print(issueKey,desc)

        table = document.find_all("table", {"class": "grid"})[0]
        priority = table.find_all("tr")[0].find_all("td")[3].contents[0].strip()
        proj = table.find_all("tr")[2].find_all("td")[1].contents[0].strip()
        print(priority,proj)
        comments = document.find_all("tr", id=lambda value: value and value.startswith("comment-body"))
        c_num = len(comments)
        out_str = ''
        for c in range(len(comments)):
            # " ".join(sentence.split())
            str = " ".join(comments[c].get_text().strip().split())
            out_str += str
        if len(out_str) > 10000:
            out_str = out_str[:10000]
        print(out_str)
        versions = document.find("table", "tableBorder").find_all("tr")[4].find_all("td")[2].contents[0]
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)
        spamwriter.writerow([proj,issueKey,desc,priority,c_num,out_str])
            #time.sleep(10)
            #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
print(count)
