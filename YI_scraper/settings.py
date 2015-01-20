# -*- coding: utf-8 -*-

# Scrapy settings for YI_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'YI_scraper'

SPIDER_MODULES = ['YI_scraper.spiders']
NEWSPIDER_MODULE = 'YI_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'YI_scraper (+http://www.yourdomain.com)'

# cache
HTTPCACHE_ENABLED = True
HTTPCACHE_POLICY = 'scrapy.contrib.httpcache.DummyPolicy'

FEED_FORMAT = 'json'