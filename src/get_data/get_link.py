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


