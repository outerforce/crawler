
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
    url = "https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?jqlQuery=project+%3D+"+str(i)+"/"+"&tempMax=1000"
    print(url)
    page = request.urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    #bugID_list = soup.find_all("h3","formtitle")
    tabletitle = soup.find_all("tr","issuerow")
    #tbinfo = soup.find_all("table","grid")
    num = len(tabletitle)
    print(num)
    for i in range(num):
        bugid = tabletitle[i].find("td","issuekey").find('a').get_text()
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
        print(bugid) 
    	issuelink = "https://issues.apache.org/jira/si/jira.issueviews:issue-html/"+ str(bugid) + "/" + str(bugid)+".html"
    	print(issuelink)
    	# issuepage = request.urlopen(issuelink)
    	# issuesoup = BeautifulSoup(page,"lxml")
    	# description = issuesoup.find("id","descriptionArea").get_text()  
    	# comments = issuesoup.find_all(re.compile("^comment-body-"))
    	# print(issuelink,description,comments)



        # date = re.sub(r'\n\s*\n', r'\n\n',tabletitle[i].find("h3","formtitle").find("span","subText").contents[0].strip(),flags = re.M)

        # status = re.sub(r'\n\s*\n', r'\n\n', tabletitle[i].find_all("td")[2].contents[0].strip(), flags=re.M)
        # proj = re.sub(r'\n\s*\n', r'\n\n', tabletitle[i].find_all("td")[4].find('a').contents[0].strip(), flags=re.M)
        # #component = re.sub(r'\n\s*\n', r'\n\n', tabletitle[j].find_all("td")[6].contents[0].strip(), flags=re.M)
        # try:
        #     affected_v = re.sub(r'\n\s*\n', r'\n\n', tabletitle[i].find_all("td")[8].find('a').contents[0].strip(),flags = re.M)
        #     fix_v =  re.sub(r'\n\s*\n', r'\n\n',tabletitle[i].find_all("td")[10].find('a').contents[0].strip(),flags = re.M)
        # except Exception:
        #     affected_v = "None"
        #     fix_v = "None"
        #print(bugid, description, date, status,proj,affected_v,fix_v)

        # with open("text", "w") as outfile:
        # json.dump({'bugID': bugid, 'desc': description, 'date': date, 'status': status, 'proj': proj, 'affected_v': affected_v, 'fix_v': fix_v}, outfile, indent=4)
    # for k in range(len(tbinfo)):
    #     if(k%2==1):
    #         bugtype = tbinfo[k].find_all("td")[1].contents[0]
    #         priority = tbinfo[k].find_all("td")[3].contents[0]
    #         reporter = tbinfo[k].find_all("td")[5].find('a').contents[0]
        
    #         assign = tbinfo[k].find_all("td")[7].contents[0]
    #         resolu = tbinfo[k].find_all("td")[9].contents[0]
    #         votes = tbinfo[k].find_all("td")[11].contents[0]
    #         labels= tbinfo[k].find_all("td")[13].contents[0]
    #         print(bugtype,priority,reporter,assign,resolu,votes,labels)
