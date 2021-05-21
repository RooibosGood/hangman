# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:04:55 2021

@author: Takai
"""

import re
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
      #  print(html)
        url_list =[]
        match_list =["economy", "medical", "national"]
        for tag in sp.find_all("a"):
#            print(tag)
            url = tag.get("href")
#            print(tag)
            if url is None:
                continue
            if "medical" in url:
                if "http" in url:
                    r_sub = urllib.request.urlopen(url)
                    html_sub = r_sub.read()
                    sp_sub = BeautifulSoup(html_sub, parser)
                    for tag_sub in sp_sub.find("title"):
                        if url not in url_list:
                            url_list.append(url)
                            print(tag_sub)
#                        print(url)
#                print("\n" + url)
                
#news = 'https://news.google.com/'
news = 'https://www.yomiuri.co.jp/'
#news = 'https://www.yahoo.co.jp/'
Scraper(news).scrape()