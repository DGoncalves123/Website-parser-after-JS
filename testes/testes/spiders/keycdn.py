# -*- coding: utf-8 -*-
import scrapy


class KeycdnSpider(scrapy.Spider):
    name = "keycdn"
    allowed_domains = ["google.com"]
    start_urls = ['google.com']

    def parse(self, response):
        pass
