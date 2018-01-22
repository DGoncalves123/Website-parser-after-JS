from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import scrapy

setting = get_project_settings()
spider_loader = scrapy.loader.spiderloader.SpiderLoader.from_settings(settings)

for spider_name in spider_loader.list():
    print ("Running spider %s" % (spider_name))
    process.crawl(spider_name) 
process.start()