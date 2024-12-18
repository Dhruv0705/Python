import configparser
import urllib.parse

import scrapy


class Facebook(scrapy.Spider):
    name = 'facebook'

    def __init__(self, keywords: list, exclusions: list,  max_price, min_price, strictmode, facebook_city_id, **kwargs):

        # build the URL
        self.exclusions = exclusions
        self.keywords = keywords
        self.strictmode = strictmode
        url = f"https://www.facebook.com/marketplace/{facebook_city_id}/search?"
        config = configparser.ConfigParser(allow_no_value=False)
        config.read('config.ini')
        if(config['FACEBOOK']['date_listed'] != '0'):
            url += urllib.parse.urlencode({'query': ' '.join(keywords), 'minPrice': min_price,
                                           'maxPrice': max_price, 'sortBy': config['FACEBOOK']['sortby'], 'daysSinceListed': config['FACEBOOK']['date_listed']})
        else:
            url += urllib.parse.urlencode({'query': ' '.join(keywords), 'minPrice': min_price,
                                           'maxPrice': max_price, 'sortBy': config['FACEBOOK']['sortby']})
        self.start_urls = [url]  # set the url to the spider
        super().__init__(**kwargs)

    def parse(self, response):
        # each flex item box (each ad)
        for ads in response.xpath('//div[@class="kbiprv82"]'):
            title = ads.xpath(
                './a/div/div[2]/div[2]/span/div/span/span/text()').extract_first()
            # check for any exclusion is in the title, ignore if so
            if any(exclusions.lower() in title.lower() for exclusions in self.exclusions):
                continue

            # check if title has a keyword, in future this can be an option in the config (strictmode)
            if self.strictmode and not any(keywords.lower() in title.lower() for keywords in self.keywords):
                continue

            yield {
                'price': ads.xpath('./a/div/div[2]/div[1]/span/div/span/text()').extract_first(),
                'title': title,
                'link': 'https://www.facebook.com' + ads.xpath('./a/@href').extract_first(),
            }
