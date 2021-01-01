import scrapy
from ..items import ScrapyprojectItem

class playSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'https://play.google.com/store/search?q=events%20bd&c=apps'
    ]

    def parse(self, response, **kwargs):
        items = ScrapyprojectItem()
        names = response.css('.nnK0zc::text').extract()
        items['names'] = names
        yield items

