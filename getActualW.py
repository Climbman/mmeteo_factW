#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import json
import datetime

import config_test

def reqToList():
    
    htmlRaw = requests.get(config._DATA_URL)
    htmlParsed = BeautifulSoup(htmlRaw.text, 'html.parser')
    jsonRaw = htmlParsed.find('div', attrs={'class':'json'}).text
    json_list = json.loads(jsonRaw)

    return json_list

def prntList():

    json_dict = reqToList()
    i = 0
    print("\n")
    for x in json_dict:
        i = i + 1
        print(x)
        print("\n")
    
    print(i)


def prntNice(prnt=False, n=99):

    json_dict = reqToList()
    length = len(json_dict)
    
    if not isinstance(n, int) or n < 0 or n > 24:
        m = length - 1
    else:
        m = n
        
    lastitem = json_dict[m]
    
    nice = json.dumps(lastitem, sort_keys=True, indent=4, separators=(',', ': '))

    if prnt:
        print(nice)

    return nice


def writeJson(text):

    path = config._DATAPATH
    
    now = "default"
    now = datetime.datetime.now().strftime("%Y%m%d%H%M")

    with open(path + "wm_" + now + ".json",'w',encoding = 'utf-8') as f:
        f.write(text)

    
writeJson(prntNice())
