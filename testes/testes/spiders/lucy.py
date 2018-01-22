# -*- coding: utf-8 -*-
import HTMLParser
import requests
from bs4 import BeautifulSoup
import scrapy
import re
#uklo,frpa,sgsg,usny
#seitestes.ml 
#https://seitestesml.000webhostapp.com/

class LucySpider(scrapy.Spider):
    name = "lucy"
    allowed_domains = ["keycdn.com"]
    start_urls = (
        'URLTOSWAP',
    )
    ID=0
 
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': { 'wait': 8 }
                }
            })
 
    def parse(self, response):
        soup = BeautifulSoup(response.body.decode("utf-8"),"lxml")
        percent=0
        check=True
        check3=True
        halffinish=0
        perchalffinish=0

        #TIRAR AS TIMELINES    FEITO
        tag = soup.findAll('div', {"class": "progress progress-tl"}, limit=20)
        more = soup.findAll('data_content', limit=20)
        s=[]
        for i in tag:
            t = re.sub("[^0-9\.]+","",i.findChildren('span')[0].text)#percentage start 
            if check:
                m = re.sub("[^0-9\.]+","",i.findChildren('span')[1].text)#percentage half
                perchalffinish=float(m)
                n = re.sub("[^0-9\.]+","",i.findChildren('span')[2].text)#percentage end
                check=False
            spl = i['data-content'].split(' ')
            v=0
            check2=0
            s.append(str(halffinish*float(t)/perchalffinish))
            for k in spl:
                k = re.sub("\D+", "", k)
                if k:
                    if check3:
                        if check2==0:
                            halffinish = int(k)
                            check3=False
                    s.append(k)
                    start = int(k)*float(t)/float(m)
                    check2=check2+1
                v=v+1
        for item in s:
            print("%s, " % item)
        print("\n")