# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:42:02 2019

@author: Wentao
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time

class github(object):
    def __init__(self,url):
        self.url = url
        self.name = url.split('/')[-2]
        r = requests.get(url)
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        temp1 = soup.find('a', class_="social-count js-social-count")
        self.star_num = int(temp1.text.split()[0].replace(",",""))
        self.name_list = None
        r.keep_alive = False
    def get_list(self):
        j = 1
        url2 = self.url
        self.name_list = []
        temp = self.star_num//30+1
        for i in range(temp):
            if len(self.name_list) > self.star_num-1:
                break
            attempts = 0
            success = False
            while attempts < 10 and not success:
                try:
                    r = requests.get(url2)
                    demo = r.text
                    soup = BeautifulSoup(demo, "html.parser")
                    temp1 = soup.find_all('h3', class_="follow-list-name")
                    i = 0
                    while i < len(temp1):
                        temp1_2=temp1[i].find('a')
                        i = i+1
                        self.name_list.append(temp1_2.text)
                        print(self.name,':      star_num:  ',self.star_num,'      name:',temp1_2.text,' round: ', str(j),'  num: ',str(i),"   Done")
                    temp2=soup.find('a', rel="nofollow", class_="btn btn-outline BtnGroup-item",text = 'Next')
                    url2 = temp2['href']
                    r.keep_alive = False
                    success = True
                    j = j + 1
                except BaseException as e:
                    print(e)
                    attempts += 1
                    if attempts <= 5:
                        time.sleep(5)
                    elif attempts <= 8 :
                        time.sleep(20)
                    else:
                        time.sleep(120)
                    if attempts >= 10:
                        break

        pd.Series(self.name_list).to_csv('github_'+self.name+'.txt')

    def get_table(self):
        if self.name_list == None:
            name_list = list(pd.read_csv('github_'+self.name+'.txt',header = None).iloc[:,1])
        else:
            name_list = self.name_list
        self.result = pd.DataFrame(np.full([len(name_list),6], np.nan),columns = ["Repositories","Projects",\
                              "Stars", "Followers","Following","Contributions in the last year"])
        self.result.index = pd.Series(name_list)
        j = 0
        for i in name_list:
            if j > self.star_num - 1:
                break
            attempts = 0
            success = False
            while attempts < 10 and not success:
                try:
                    start = time.time()
                    url = 'https://github.com/' + i
                    r = requests.get(url)
                    demo = r.text
                    soup = BeautifulSoup(demo, "html.parser")
                    temp = soup.find_all('a', class_="UnderlineNav-item mr-0 mr-md-1 mr-lg-3 ")
                    temp_num = []
                    for k in range(5):
                        num = temp[k].find('span', class_="Counter hide-lg hide-md hide-sm").text
                        temp_num.append(num.split()[0])
                    temp2 = soup.find('h2', class_="f4 text-normal mb-2")
                    temp_num.append(temp2.text.split()[0])
                    self.result.loc[i] = temp_num
                    end = time.time()
                    print('time cost',end-start,'s')
                    r.keep_alive = False
                    success = True
                    j = j + 1
                    print(self.name,":     star_num:  ",self.star_num,"   num:  ", str(j),"   name:   ", i,"    Done")
                except BaseException as e:
                    print(e)
                    attempts += 1
                    if attempts <= 5:
                        time.sleep(5)
                    elif attempts <= 8 :
                        time.sleep(20)
                    else:
                        time.sleep(120)
                    if attempts >= 10:
                        break
        self.result.to_csv('github_'+self.name+'.csv')

    def run(self):
        self.get_list()
        self.get_table()

if __name__ == '__main__':
#    star=github('https://github.com/taosdata/TDengine/stargazers')  #1
#    star=github("https://github.com/zstackio/zstack/stargazers")  #2
#    star=github('https://github.com/pingcap/tidb/stargazers')  #3
#    star=github('https://github.com/influxdata/telegraf/stargazers')  #4
#    star=github('https://github.com/Kong/kong/stargazers')  #5
#    star=github('https://github.com/hashicorp/terraform/stargazers')   #6
#    star=github('https://github.com/elastic/elasticsearch/stargazers')    #7
    star=github('https://github.com/mongodb/mongo/stargazers')   #8
    print("star num: ",str(star.star_num))
#    star.get_list()
#    star.get_table()
    star.run()
