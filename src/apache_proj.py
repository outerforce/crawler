#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import collections
from urllib.request import urlopen
from lxml import html
from urllib import request
import re
from bs4 import BeautifulSoup
import time
import datetime
import sys
import chardet
##def parse(self, response):
path = "/home/irene/crawler/project_list.txt"
def openFile(path):
    file = open(path,"r")
    L = []
    for line in file:
        L.append(line.strip().upper())
    return L
    #print(L)
def main(L):
    for i in L:
        url = "https://issues.apache.org/jira/sr/jira.issueviews:searchrequest-fullcontent/temp/SearchRequest.html?" \
              "jqlQuery=project+%3D+"+str(i)+"&tempMax=1000"
        #print(url)
        page = request.urlopen(url)
        soup = BeautifulSoup(page,"lxml")
        tabletitle = soup.find_all("table","tableBorder")
        #tbinfo = soup.find_all("table","grid")
        num = len(tabletitle)
        print(num)
        for i in range(num):
            bugid = tabletitle[i].find("h3","formtitle").contents[0]
            description = tabletitle[i].find("h3","formtitle").find('a').contents[0]
            date = re.sub(r'\n\s*\n', r'\n\n',tabletitle[i].find("h3","formtitle").find("span","subText").contents[0].strip(),flags = re.M)
            status = re.sub(r'\n\s*\n', r'\n\n', tabletitle[i].find_all("td")[2].contents[0].strip(), flags=re.M)
            proj = re.sub(r'\n\s*\n', r'\n\n', tabletitle[i].find_all("td")[4].find('a').contents[0].strip(), flags=re.M)
            try:
                affected_v = re.sub(r'\n\s*\n', r'\n\n', tabletitle[i].find_all("td")[8].find('a').contents[0].strip(),flags = re.M)
                fix_v =  re.sub(r'\n\s*\n', r'\n\n',tabletitle[i].find_all("td")[10].find('a').contents[0].strip(),flags = re.M)
            except Exception:
                affected_v = "None"
                fix_v = "None"
            print(bugid, description, date, status, proj, affected_v, fix_v)
            time.sleep(10)

if __name__ == '__main__':
    L = openFile(path)
    main(L)

# write operation:
# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    