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
# list = glob.glob(("/home/irene/crawler/temp/*"))

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
import os

list = glob.glob("/home/irene/crawler/detail_file/issues/*")
result = []
count = 0
with open('short_desc.csv', 'w', newline='') as csvfile:
    for i in list:
        base = os.path.basename(i)
        # x = os.path.splitext(base)
        issueKey = os.path.splitext(base)[0]
        # print(x1)
        f = codecs.open(i, 'r', 'utf-8')
        document = BeautifulSoup(f.read(), "lxml")
        # print(document)
        # issueKey = document.find("h3","formtitle").get_text().strip()
        # str = re.sub(r"\([^()]*\)|\[[^\[\]]*\]", "", issueKey)
        # issue = issueKey.strip('[]').strip(']')
        try:
            #get the description
            desc1 = document.find("td", id="descriptionArea").find_all('p')
            num = len(desc1)
            print(num)
            str = ""
            if num > 1:
                for i in range(num-1):
                    temp =  desc1[i].get_text()
                    #print(temp)
                    str = str+temp
            else:
                str = desc1[0].get_text()

            desc = re.sub('[^A-Za-z]+', ' ', str)
            if len(desc) > 2000:
                desc = desc[:2000]
            print(desc)
            # get the comment
            comments = document.find_all("tr", id=lambda value: value and value.startswith("comment-body"))
            comm = ""
            if len(comm) > 1:
                for i in range(len(comm) - 1):
                    temp1 = comments[i].get_text()
                    comm = comm + temp1
            else:
                comm = comments[0].get_text()
            comment = re.sub('[^A-Za-z]+', ' ', comm)
            if len(comment) > 2000:
                comment = comment[:2000]
            print(comment)
        except Exception:
            desc = "null"
            comment = "null"
        # print(issueKey, desc)
        # table = document.find_all("table", {"class": "grid"})[0]
        # priority = table.find_all("tr")[0].find_all("td")[3].contents[0].strip()
        # proj = table.find_all("tr")[2].find_all("td")[1].contents[0].strip()
        # print(desc)
        # comments = document.find_all("tr", id=lambda value: value and value.startswith("comment-body"))
        # c_num = len(comments)
        # out_str = ''
        # for c in range(len(comments)):
        #     " ".join(comments[c].split())
        #     str = " ".join(comments[c].get_text().strip().split())
        #     out_str += str
        # if len(out_str) > 10000:
        #     out_str = out_str[:10000]
        # print(out_str)
        # versions = document.find("table", "tableBorder").find_all("tr")[4].find_all("td")[2].contents[0]
        #print(issueKey,desc)
        print("1")
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
        spamwriter.writerow([issueKey, desc, comment])
        # time.sleep(10)
        # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
print(count)
