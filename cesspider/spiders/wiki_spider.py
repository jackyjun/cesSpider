#wiki baike
import re
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from cesSpider.items import BaikeItem


class WikiSpider(BaseSpider):
    name = "wiki"
    allow_domains = ['wikipedia.org']
    start_urls = [
        "http://zh.wikipedia.org/wiki/Category:%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6",
        "http://zh.wikipedia.org/wiki/Category:%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD",
        "http://zh.wikipedia.org/wiki/Category:%E4%BF%A1%E6%81%AF%E8%AE%BA",
        "http://zh.wikipedia.org/wiki/Category:%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84",
        "http://zh.wikipedia.org/wiki/Category:%E6%9C%80%E4%BC%98%E5%8C%96",
        "http://zh.wikipedia.org/wiki/Category:%E7%90%86%E8%AE%BA%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6",
        "http://zh.wikipedia.org/wiki/Category:%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF",
        "http://zh.wikipedia.org/wiki/Category:%E7%AE%97%E6%B3%95",
        "http://zh.wikipedia.org/wiki/Category:%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6",
        "http://zh.wikipedia.org/wiki/Category:%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E5%9F%BA%E7%A1%80%E7%90%86%E8%AE%BA",
        "http://zh.wikipedia.org/wiki/Category:%E8%AE%A1%E7%AE%97%E7%A7%91%E5%AD%A6",
        "http://zh.wikipedia.org/wiki/Category:%E8%AE%A1%E7%AE%97%E8%AF%AD%E8%A8%80%E5%AD%A6",
        "http://zh.wikipedia.org/wiki/Category:%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B",
        "http://zh.wikipedia.org/wiki/Category:%E9%9B%BB%E8%85%A6%E5%AE%89%E5%85%A8"

    ]
	
    def parse(self,response):
        sel = Selector(response)
        for category in sel.xpath("//*/li/div[@class='CategoryTreeSection']/div[@class='CategoryTreeItem']/a/@href").extract():
            yield  Request("http://zh.wikipedia.org"+category,callback=self.parse)
        for url in sel.xpath("//*/div[@id='mw-pages']/div[@class='mw-content-ltr']//*/ul/li/a/@href").extract():
            yield Request("http://zh.wikipedia.org"+url,callback=self.parse_item)



    def parse_item(self,response):
        sel = Selector(response)
        item = BaikeItem()
        title = sel.xpath("//*/div[@id='content']/h1[@id='firstHeading']/span[1]/text()").extract()
        summary = sel.xpath("//*/div[@id='content']/div[@id='bodyContent']/div[@id='mw-content-text']/p[1]").extract()
        category = sel.xpath("//*/div[@id='catlinks']/div[@id='mw-normal-catlinks']/ul/li/a/text()").extract()
        re_h = re.compile('</?\w+[^>]*>')
        item['link'] = response.url
        item['title'] = title[0]
        item['summary'] = re_h.sub('',summary[0])
        item['category'] = category
        return item