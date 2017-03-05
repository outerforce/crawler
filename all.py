
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

##def parse(self, response):
file = open("/home/irene/crawler/project_list.txt","r")
L = []
for line in file:
    L.append(line.strip().upper())
#print(L)
for i in L:
   #https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?jqlQuery=project+%3D+ZOOKEEPER+AND+issuetype+%3D+Bug&tempMax=1000
    url = "https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?jqlQuery=project+%3D+"+str(i)+"+AND+issuetype+%3D+Bug&tempMax=1000"
    print(url)
    # content = call(["curl","url"])
	# page = request.urlopen(url)
	# soup = BeautifulSoup(page,"lxml")
	# print(soup)
    # with open('/home/irene/crawler/output.txt', 'w') as f:
    #     f.write(url)
    #     f.close()

	
	# text_file = open("Output.txt","w")
	# text_file.write(soup)
	# text_file.close()
