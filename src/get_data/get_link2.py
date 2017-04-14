#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import csv
import collections
from urllib import request
from urllib.request import urlopen
#import cookielib
import re
from lxml import html
import glob
import codecs
from bs4 import BeautifulSoup

list = glob.glob(("/home/irene/crawler/temp/*"))
url = []
count = 0
for i in list:
    f=codecs.open(i, 'r', 'utf-8')
    document= BeautifulSoup(f.read(),"lxml")
    #print(document)
    tabletitle = document.find_all("tr", "issuerow")
    num = len(tabletitle)
    count += num
    print(count)
    for j in range(num):
        proj = document.find("span",id ="fieldpid").find('a').contents[0]
        issueKey = tabletitle[j].find("td","issuekey").find('a').contents[0]
        link = "https://issues.apache.org/jira/si/jira.issueviews:issue-html/"+ issueKey+ "/"+issueKey+".html"
        print(link)
        url.append(link)
outF = open("opdetail.txt", "w")
url = map(lambda x: x + "\n", url)
outF.writelines(url)
outF.close()
print(count)

