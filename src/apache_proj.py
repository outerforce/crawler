#!/usr/bin/env python3
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

    # with open('names.csv', 'w') as csvfile:
    #     fieldnames = ['first_name', 'last_name']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()
    #     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
        time.sleep(10)


# page = request.urlopen("https://projects.apache.org/projects.html?name").read()
# print(page)
# proj_list = BeautifulSoup(page,"lxml")
# print(proj_list)
# #.find("div","list")
# print (len(proj_list))

# for i in range(2):
#     proj_link = proj_list[i].find("a").get("href")
#     proj_name = proj_list[i].find("a").get_text
#     print (proj_link, proj_name)
        # page=urllib2.urlopen("https://projects.apache.org/"+str(proj_list[i])+"&q=javascript&type=Repositories&utf8=%E2%9C%93").read()
        # chardit = chardet.detect(page)
        # print(chardit['encoding'])
        # t_unicode = page.decode(chardit['encoding'])
        # data = t_unicode.encode('utf-8')
        # soup = BeautifulSoup(data,from_encoding="gb18030")
        # info=soup.find_all("li","repo-list-item public source")

        # for j in range(len(info)):
        #     link = "https://github.com"+info[j].find("h3","repo-list-name").contents[1]['href']
        #     #print link
        #     title = info[j].find("h3","repo-list-name").find("a").get("href")
        #     print title

        #     # descripinfo = info[j].find("p","repo-list-description")

        #     # if descripinfo is None:
        #     #     small_desc = "none"
        #     # else:
        #     #     small_desc = descripinfo.get_text(strip=True)
        #     newpage =urllib2.urlopen(link).read()
        #     chardit = chardet.detect(newpage)
        #     t_unicode = newpage.decode(chardit['encoding'])
        #     newdata = t_unicode.encode('utf-8')
        #     newsoup =BeautifulSoup(newdata,from_encoding="gb18030")

        #     descinfo = newsoup.find("article","markdown-body entry-content")
        #     if descinfo is None:
        #         desc = 'None'
        #     else:
        #         desc = descinfo.get_text(strip=True)
        #     print (link+'\n'+title+'\n'+desc)

    #         try:
    #             self.cur.execute('insert into desc1(repo_name, repo_uri, destext)values(%s,%s,%s)',(title,link,desc))
    #         except Exception:
    #             pass
    #         print "haha"
    #     self.conn.commit()
                
    # self.cur.close()
    # self.conn.close()
            #print soup

            # info=soup.find_all("li","repo-list-item public source")
            # #print info 
            # for j in range(len(info)):
            #     link = "https://github.com"+info[j].find("h3","repo-list-name").contents[1]['href']
            #     #print link
            #     title = info[j].find("h3","repo-list-name").find("a").get_text()
            #     #contents[0]+info[j].find("h3","repo-list-name").find("a").find("em").contents[0]
            #     #print title
            #     update_time = info[j].find("p","repo-list-meta").contents[1]['datetime']
            #     #print update_time
            
            #     newpage =urllib2.urlopen(link).read()
            #     newsoup =BeautifulSoup(newpage)
            #     # #print newsoup
            #     newinfo = newsoup.find("ul","numbers-summary").find("li","commits")
            #     #print newinfo
            #     commit= newinfo.find("span","num text-emphasized").get_text(strip=True)
            #     #print commit
            #     link_commit = "https://github.com"+newinfo.contents[1]['href']
            #     #print link_commit 
            #     for z in range(100):   
            #         newpage2 = urllib2.urlopen(link_commit+"?page="+str(z+1)).read()
            #         newsoup2 = BeautifulSoup(newpage2)
            #         commiterinfo = newsoup2.find_all("ol","commit-group table-list table-list-bordered")
            #         #print commiterinfo
            #         userlist = [];
            #         for x in range(len(commiterinfo)):
            #             contribinfo = commiterinfo[x].find_all("div","avatar-parent-child")
            #             #print contribinfo
            #             for y in range (len(contribinfo)):
            #                 try:
            #                     link_contrib = "https://github.com"+contribinfo[y].contents[1]['href']
            #                     print link_contrib
            #                     userlist.append(link_contrib)
            #                 except Exception:
            #                     pass
            #         print userlist

            #     new_userlist = list(set(userlist))

            #     for k in range(len(new_userlist)):
            #         newpage3 = urllib2.urlopen(link_contrib).read()
            #         newsoup3 = BeautifulSoup(newpage3)
            #         nameinfo = newsoup3.find("div","column one-fourth vcard")
            #         committer_fullname = nameinfo.find("div","vcard-fullname").get_text()
            #         committer_username = nameinfo.find("div","vcard-username").get_text()
            #         print committer_fullname
            #         print committer_username
            #         userinfo = nameinfo.find("ul","vcard-details border-top border-gray-light py-3")
            #         user_uri = nameinfo.find_all("li")[0].find('a').get_text()
            #         print user_uri
            #         join_time= nameinfo.find_all("li")[1].find("local-time")['datetime']
            #         print join_time
            #         try: 

            #             cursor.execute('insert into user1 values(\''+committer_username
            #             +'\',\''+committer_fullname
            #             +'\',\''+join_time
            #             +'\',\''+user_uri+'\')') 
            #         except Exception:
            #             pass
            #     self.conn.commit()
            # except psycopg2.Error as e:
            #     print e.pgerror
            #     print 'error!!! at parse'
            #     pass
            # except:
            #     print 'no'
            #     pass
            # pass

# conn = mysql.connector.connect(host='localhost',user='root',password='a123',database='mytest',port=3306)
# cursor=conn.cursor()
 
# cursor.execute("""
#             SELECT repo_id,repo_name,repo_uri
#             FROM repo3
#             """)
 
# rows = cursor.fetchall()
 
# for row in rows:
#     key_link = row[1]
#     uri = row[2]
#     print key_link
#     page1 = urllib2.urlopen("https://api.github.com/repos/"+key_link).read()
#     repodata = json.loads(page1)
#     author = repodata['owner']['login']
#     contribinfo_link = repodata['contributors_url']
#     time.sleep(30)
#     page2=urllib2.urlopen(contribinfo_link).read()
#     #print page
#     userdata = json.loads(page2)
#     for i in range(len(userdata)):
#         username= userdata[i]['login']
#         userid=userdata[i]['id']
#         userinfo=userdata[i]['url']
#         user_link=userdata[i]['html_url']
#         repos_link=userdata[i]['repos_url']
#         contri_num=userdata[i]['contributions']
#         print repos_link
#         try: 
#             cursor.execute('insert into scmlog(repo_name,repo_uri,author,userid,username,user_link,contri_num)values(%s,%s,%s,%s,%s,%s,%s)',(key_link,uri,author,userid,username,user_link,contri_num)) 
#         except Exception:
#             pass
#     conn.commit()
#     print '11'
#     time.sleep(60)
#     print "haha"
# cursor.close()
# conn.close()
    
    