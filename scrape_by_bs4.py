# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:21:25 2021

@author: Takai
"""

import re
import urllib.request
from bs4 import BeautifulSoup

# HTMLファイルを読み込んでBeautifulSoupオブジェクトを得る
#url = 'https://www.yomiuri.co.jp'
url = 'https://gihyo.jp/'
#url ='https://www.holisticheal.com/'
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
parser = 'html.parser'
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)
sp = BeautifulSoup(html, parser)

# select() メソッドで、セレクターに該当するa要素のリストを取得して、個々のa要素に対して処理を行う。
