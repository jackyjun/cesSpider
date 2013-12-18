# Scrapy settings for cesSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cesSpider'

SPIDER_MODULES = ['cesSpider.spiders']
NEWSPIDER_MODULE = 'cesSpider.spiders'
DOWNLOAD_DELAY = 0.8
DEPTH_LIMIT = 5
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cesSpider (+http://www.yourdomain.com)'
