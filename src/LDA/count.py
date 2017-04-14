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

count = 0
list = glob.glob(("/home/irene/crawler/summary/*"))
result = []
with open('summary.csv', 'w', newline='') as csvfile:
    for i in list:
        f = codecs.open(i, 'r', 'utf-8')
        document = BeautifulSoup(f.read(), "lxml")
        # print(document)
        tabletitle = document.find_all("tr", "issuerow")
        num = len(tabletitle)
        count += num
        print(count)
        for j in range(num):
            proj = document.find("span", id="fieldpid").find('a').contents[0]
            issueKey = tabletitle[j].find("td", "issuekey").find('a').contents[0]
            str = tabletitle[j].find("td", "summary").find('a').contents[0]
            summary = re.sub('[^A-Za-z]+', ' ', str)
            # url = tabletitle[j].find("td","issuekey").find('a').get("href")
            link = "https://issues.apache.org/jira/si/jira.issueviews:issue-html/" + issueKey + "/" + issueKey + ".html"
            #print(link)
            result.append(link)
            created = tabletitle[j].find("td", "created").find('time').contents[0]
            updated = tabletitle[j].find("td", "updated").find('time').contents[0]
            print(proj, summary, created, updated)
            # newpage = request.urlopen(link)
            # newsoup = BeautifulSoup(newpage, "lxml")
            # desc = newsoup.find("td",id="descriptionArea").get_text().strip()
            # print(desc)
            # table = newsoup.find_all("table", {"class": "grid"})[0]
            # priority = table.find_all("tr")[0].find_all("td")[3].contents[0].strip()
            # print(priority)
            # comments = newsoup.find_all("tr", id=lambda value: value and value.startswith("comment-body"))
            # c_num = len(comments)
            # out_str = ''
            # for c in range(len(comments)):
            #     #" ".join(sentence.split())
            #     str = " ".join(comments[c].get_text().strip().split())
            #     out_str += str
            # if len(out_str)>10000:
            #     out_str = out_str[:10000]
            # print(out_str)
            # versions = newsoup.find("table","tableBorder").find_all("tr")[4].find_all("td")[2].contents[0]
            # tabletitle = soup.find_all("table", "tableBorder")
            # with open('egg.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
            spamwriter.writerow([proj, issueKey, summary])
            # time.sleep(10)
            # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
outF = open("opdetail.txt", "w")
url = map(lambda x: x + "\n", result)
outF.writelines(url)
outF.close()
print(count)
