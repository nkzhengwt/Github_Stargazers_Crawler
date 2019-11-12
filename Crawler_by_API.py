# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:10:52 2019

@author: Wentao
"""


import requests
import pandas as pd
from time import time
from multiprocessing import Pool
import os
import traceback
#from bs4 import BeautifulSoup
#url = 'https://api.github.com/repos/hashicorp/terraform/stargazers?page=2'
def star(name):
    name1 = name.replace('_','/')
    url = 'https://api.github.com/repos/'+name1+'/stargazers?page='
    star = pd.DataFrame(columns = ['login','starred_at'])
    filePath = 'E:\\7_Intern\\GGV\\com'
    files = os.listdir(filePath)
    nums = []
    file_name = 'star_'+name
    status = False
    for i in files:
        if i[0:len(file_name)] == file_name:
            status = True
            nums.append(int(i[(len(file_name)+1):-4]))
    if status == False:
        num = 0
    else:
        num = max(nums) - 1
    over = False
    while 1:
        try:
            b = time()
            num += 1
            url2 = url + str(num)
            headers = {"Accept": "application/vnd.github.v3.star+json","Authorization": "token ##"}
            r = requests.get(url2,headers=headers)
            false = False
            true = True
            null = "Null"
            with requests.get(url2,headers=headers) as r:
                x=eval(r.text)
            if len(x) == 0:
                print(url2,' Over')
                over = True
                break
            for i in range(len(x)):
                temp = pd.DataFrame([(x[i]['user']['login'],x[i]['starred_at'])],columns = ['login','starred_at'])
                star = star.append(temp)
            e = time()
            print(url2,str(e-b)+' Cost')
        except:
            traceback.print_exc()
            print(name,num,'stop')
            break
    if over == False:
        if not os.path.exist(filePath+'\\star_'+name+'_'+str(num)+'.csv') and num > 1:
            star.to_csv(filePath+'\\star_'+name+'_'+str(num)+'.csv',index = False,header = False)
    else:
        star.to_csv(filePath+'\\star_'+name+'.csv',index = False,header = False)

def fork(name):

    name1 = name.replace('_','/')
    url = 'https://api.github.com/repos/'+name1+'/forks?page='
    star = pd.DataFrame(columns = ['login','created_at'])
    filePath = 'E:\\7_Intern\\GGV\\fork'
    files = os.listdir(filePath)
    nums = []
    file_name = 'fork_'+name
    status = False
    for i in files:
        if i[0:len(file_name)] == file_name:
            status = True
            nums.append(int(i[(len(file_name)+1):-4]))
    if status == False:
        num = 0
    else:
        num = max(nums) - 1
    over = False
    while 1:
        try:
            b = time()
            num += 1
            url2 = url + str(num)
            headers = {"Authorization": "token ##"}
            false = False
            true = True
            null = "Null"
            with requests.get(url2,headers=headers) as r:
                x=eval(r.text)
            if len(x) == 0:
                print(url2,' Over')
                over = True
                break
            for i in range(len(x)):
                login = x[i]['owner']['login']
                time1 = x[i]['created_at']
                temp = pd.DataFrame([(login,time1)],columns = ['login','created_at'])
                star = star.append(temp)
            e = time()
            print(url2,str(e-b)+' Cost')
        except:
            traceback.print_exc()
            print(name,num,'stop')
            break
    if over == False:
        if not os.path.exist(filePath+'\\fork_'+name+'_'+str(num)+'.csv') and num > 1:
            star.to_csv(filePath+'\\fork_'+name+'_'+str(num)+'.csv',index = False,header = False)
    else:
        star.to_csv(filePath+'\\fork_'+name+'.csv',index = False,header = False)
def commits(name):
    name1 = name.replace('_','/')
    url = 'https://api.github.com/repos/'+name1+'/commits?page='
    star = pd.DataFrame(columns = ['author','author_date','commiter','commiter_date'])
    filePath = 'E:\\7_Intern\\GGV\\commits'
    files = os.listdir(filePath)
    nums = []
    file_name = 'comm_'+name
    status = False
    for i in files:
        if i[0:len(file_name)] == file_name:
            status = True
            nums.append(int(i[(len(file_name)+1):-4]))
    if status == False:
        num = 0
    else:
        num = max(nums) - 1
    over = False
    while 1:
        try:
            b = time()
            num += 1
            url2 = url + str(num)
            headers = {"Authorization": "token ##"}
            false = False
            true = True
            null = "Null"
            with requests.get(url2,headers=headers) as r:
                x=eval(r.text)
            if len(x) == 0:
                print(url2,' Over')
                over = True
                break
            for i in range(len(x)):
                author  = x[i]['commit']['author']['name']
                author_date = x[i]['commit']['author']['date']
                commiter = x[i]['commit']['committer']['name']
                commiter_date  = x[i]['commit']['committer']['date']
                temp = pd.DataFrame([(author,author_date,commiter,commiter_date)],columns = ['author','author_date','commiter','commiter_date'])
                star = star.append(temp)
            e = time()
            print(url2,str(e-b)+' Cost')
        except:
            traceback.print_exc()
            print(name,num,'stop')
            break
    if over == False:
        if not os.path.exist(filePath+'\\comm_'+name+'_'+str(num)+'.csv') and num > 1:
            star.to_csv(filePath+'\\comm_'+name+'_'+str(num)+'.csv',index = False,header = False)
    else:
        star.to_csv(filePath+'\\comm_'+name+'.csv',index = False,header = False)

def issues(name):
    name1 = name.replace('_','/')
    url = 'https://api.github.com/repos/'+name1+'/issues?page='
    star = pd.DataFrame(columns = ['id','text','time','tag','type'])
    filePath = 'E:\\7_Intern\\GGV\\issues'
    files = os.listdir(filePath)
    nums = []
    file_name = 'issu_'+name
    status = False
    for i in files:
        if i[0:len(file_name)] == file_name:
            status = True
            nums.append(int(i[(len(file_name)+1):-4]))
    if status == False:
        num = 0
    else:
        num = max(nums) - 1
    over = False
    while 1:
        try:
            b = time()
            num += 1
            url2 = url + str(num)
            headers = {"Authorization": "token ##"}
            false = False
            true = True
            null = "Null"
            with requests.get(url2,headers=headers) as r:
                x=eval(r.text)
            if len(x) == 0:
                print(url2,' Over')
                over = True
                break
            for i in range(len(x)):
                id1  = x[i]['id']
                text = x[i]['title']
                time1 = x[i]['created_at']
                type1 = x[i]['closed_at']
                tags  = x[i]['labels']
                tag = ''
                for j in range(len(tags)):
                    tag += tags[j]['name']+','
                temp = pd.DataFrame([(id1,text,time1,tag,type1)],columns = ['id','text','time','tag','type'])
                star = star.append(temp)
            e = time()
            print(url2,str(e-b)+' Cost')
        except:
            traceback.print_exc()
            print(name,num,'stop')
            break
    if over ==False:
        if not os.path.exist(filePath+'\\issu_'+name+'_'+str(num)+'.csv') and num > 1:
            star.to_csv(filePath+'\\issu_'+name+'_'+str(num)+'.csv',index = False,header = False)
    else:
        star.to_csv(filePath+'\\issu_'+name+'.csv',index = False,header = False)
if __name__ == '__main__':
#    fork("chef_chef")
    com = list(pd.read_csv('company.txt',header = None)[0])
    com1=[]
    for i in range(len(com)):
        com1.append(com[i].split('/')[-2]+'_'+com[i].split('/')[-1])
    option = input("Input option:\nstar or fork or commits or issues:")
    if option == "star":
        com_dir = os.listdir('E:\\7_Intern\\GGV\\com')
    elif option == "fork":
        com_dir = os.listdir('E:\\7_Intern\\GGV\\fork')
    elif option == "commits":
        com_dir = os.listdir('E:\\7_Intern\\GGV\\commits')
    elif option =='issues':
        com_dir = os.listdir('E:\\7_Intern\\GGV\\issues')
    for j in range(len(com_dir)):
        com_dir[j] = com_dir[j][5:-4]
    name = list(set(com1).difference(set(com_dir)))


    n = int(input("Pool num:"))
    pool = Pool(n)
    if option == "star":
        pool.map(star, name)
    elif option == "fork":
        pool.map(fork, name)
    elif option == "commits":
        pool.map(commits, name)
    elif option == "issues":
        pool.map(issues, name)
    pool.close()
    pool.join()

