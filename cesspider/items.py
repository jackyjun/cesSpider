# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

#baidu baike
class BaikeItem(Item):
    title = Field()
    summary = Field()
    category = Field()
    link    = Field()
