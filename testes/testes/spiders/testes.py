#from html.parser import HTMLParser
import HTMLParser
import requests
from bs4 import BeautifulSoup
import scrapy

class LoginSpider(scrapy.Spider):
    name = 'tools.keycdn.com'
    start_urls = ['https://tools.keycdn.com/speed']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'url': 'google.com', 'location': 'uklo','public':"1"},
            callback=self.after_login
        )

    def after_login(self, response):
        self.logger.error("------------------------------")
       	#self.logger.error(response.body.decode("utf-8"))
       	k = open("all.html","w")
       	k.write(response.body.decode("utf-8"))
       	k.close
        self.logger.error("------------------------------")
        soup = BeautifulSoup(response.body.decode("utf-8"),"lxml")
        tag = soup.findAll('table', limit=4)

        f = open("table.html","w")
        for i in range(len(tag)):
        	f.write(str(tag[i]))
        f.close
        return





