# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:40:04 2019

@author: Wentao
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
def info(url):
    with requests.get(url) as r:
        demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
#    tot = soup.find_all('a',class_="social-count js-social-count")
    tot = soup.find_all('a',class_="social-count")
    watch = tot[0].text.replace(' ','').replace('\n','')
    star = tot[1].text.replace(' ','').replace('\n','')
    fork = tot[2].text.replace(' ','').replace('\n','')
    tot2 = soup.find_all('span',class_="Counter")
    if len(tot2) == 1:
        issues = tot2[0].text.replace(' ','').replace('\n','')
        pull = np.nan
        projects = np.nan
    elif len(tot2) == 2:
        issues = tot2[0].text.replace(' ','').replace('\n','')
        pull = tot2[1].text.replace(' ','').replace('\n','')
        projects = np.nan
    else:
        issues = tot2[0].text.replace(' ','').replace('\n','')
        pull = tot2[1].text.replace(' ','').replace('\n','')
        projects = tot2[2].text.replace(' ','').replace('\n','')
    tot3 = soup.find_all('span',class_="num text-emphasized")
    commits = tot3[0].text.replace(' ','').replace('\n','')
    branches =tot3[1].text.replace(' ','').replace('\n','')
    releases = tot3[2].text.replace(' ','').replace('\n','')
    return watch,star,fork,issues,pull,projects,commits,branches,releases

if __name__ == '__main__':
#    fork("chef_chef")
    com = list(pd.read_csv('company.txt',header = None)[0])
    tot = pd.DataFrame(columns = ["repo","watch","star","fork","issues","pull","projects","commits","branches","releases"])
    for i in com:
        name = i.split('/')[-2]+'_'+i.split('/')[-1]
        print(name," Begin")
        watch,star,fork,issues,pull,projects,commits,branches,releases = info(i)
        temp = pd.DataFrame([(name,watch,star,fork,issues,pull,projects,commits,branches,releases)],columns = ["repo","watch","star","fork","issues","pull","projects","commits","branches","releases"])
        tot = tot.append(temp)
        print(name," Over")
    tot.to_csv("info.csv",index=False)


