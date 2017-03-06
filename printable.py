
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

##def parse(self, response):
file = open("/home/irene/crawler/project_list.txt","r")
L = []
for line in file:
    L.append(line.strip().upper())
#print(L)
for i in L:
    #https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?jqlQuery=project+%3D+ABDERA&tempMax=1000
    url = "https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?jqlQuery=project+%3D+"+str(i)+"&tempMax=1000"
    print(url)
    page = request.urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    #bugID_list = soup.find_all("h3","formtitle")
    tabletitle = soup.find_all("tr","issuerow")
    #tbinfo = soup.find_all("table","grid")
    num = len(tabletitle)
    print(num)
    for j in range(len(tabletitle)):
        bugid = tabletitle[j].find("td","issuekey").find('a').get_text()
        str = bugid.split("\\-")
        print (str)
        # issuelink = tabletitle[i].find("td","issuekey").find('a').get("href")
        # summary = tabletitle[i].find("td","summary").find('a').contents[0]
        # assignee = tabletitle[i].find("td","assignee").get_text()
        # reporter = tabletitle[i].find("td","reporter").get_text()
        # priority = tabletitle[i].find("td","priority").find("img").get("title")
        # status = tabletitle[i].find("td","status").contents[0]
        # resolu = tabletitle[i].find("td","resolution").get_text()
        # createdtime = tabletitle[i].find("td","created").find("time").contents[0]
        # updatedtime = tabletitle[i].find("td","updated").find("time").contents[0]
        #print(bugid,issuelink,summary,assignee,priority,status,resolu,createdtime,updatedtime)
        #ise_id = re.sub(r'\n\s*\n', r'\n\n', bugid.strip(), flags=re.M).upper()
        #print (ise_id)
        # print(bugid)
    	#issuelink = "https://issues.apache.org/jira/si/jira.issueviews:issue-html/"+str(bugid)+str(bugid)+"\\.html"
    	# print(issuelink)
    	# issuepage = request.urlopen(issuelink)
    	# issuesoup = BeautifulSoup(page,"lxml")
    	# description = issuesoup.find("id","descriptionArea").get_text()  
    	# comments = issuesoup.find_all(re.compile("^comment-body-"))
    	# print(issuelink,description,comments)


