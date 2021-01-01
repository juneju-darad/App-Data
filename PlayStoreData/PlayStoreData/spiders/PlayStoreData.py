import scrapy
from ..items import PlaystoredataItem

class PlayStoreData(scrapy.Spider):
    name = 'PlayStoreData'
    start_urls = [
        'https://play.google.com/store/search?q=Auto%20%26%20Vehicles%20bangladeshi%20app&c=apps'
    ]

    def _parse(self, response, **kwargs):
        items = PlaystoredataItem()

        names = response.css('.nnK0zc::text').extract()

        items = names

        yield items