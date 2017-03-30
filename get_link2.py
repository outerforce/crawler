#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import csv
import collections
#import MySQLdb as mysql
#import mysql.connector
from urllib import request
from urllib.request import urlopen
#import cookielib
import re
from lxml import html
from bs4 import BeautifulSoup

import time
import datetime
import sys
import chardet
import os
from subprocess import call
import re

file = open("/home/irene/crawler/java_list.txt", "r")
L = []
for line in file:
    L.append(line.strip().upper())
url = []
#print(L)
for i in L:
    url.append("https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?"
               "jqlQuery=project+%3D+"+str(i)+"+AND+issuetype+%3D+Bug+AND+status+%3D+Resolved&tempMax=1000")
    #print(url)
print(len(url))
outF = open("opjava.txt", "w")
url = map(lambda x: x + "\n", url)
outF.writelines(url)
outF.close()

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
import codecs
from bs4 import BeautifulSoup

file = open("/home/irene/crawler/output.txt", "r")
L = []
for line in file:
    L.append(line.strip())
#list = glob.glob(("/home/irene/crawler/temp/*"))
count = 0

list = glob.glob(("/home/irene/crawler/temp/*"))
url = []
with open('first.csv', 'w', newline='') as csvfile:
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

