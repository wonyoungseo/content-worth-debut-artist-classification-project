from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import scrapy

from metacritic.items import metacriticItem

class MakeError(Exception):

    def __str__(self):
        return "self check"

class MetaSpider(scrapy.Spider):
    name = "meta_music"
    allow_domain = ["metacritic.com"]

    def start_requests(self):
        for i in range(49+1):
            url = 'http://www.metacritic.com/browse/albums/release-date/available/date' + '?page={}'.format(i)
            yield scrapy.Request(url, self.parse)


    def parse(self, response):

            for each in response.xpath('//*[@id="main"]/div[1]/div[2]/div[3]/div/ol/li'):

                item = metacriticItem()

                try:
                    item['artist'] = each.xpath('./div/div[3]/ul/li[1]/span[2]/text()')[0].extract()
                except:
                    item['artist'] = each.xpath('./div/div[3]/ul/li[1]/span[2]/text()').extract()


                try:
                    tmp = each.xpath('./div/div[1]/a/text()')[0].extract()
                except:
                    tmp = each.xpath('./div/div[1]/a/text()').extract()

                item['album'] = tmp[29:-53]

                try:
                    item["metascore"] = each.xpath('./div/div[2]/div/text()')[0].extract()
                except:
                    item["metascore"] = each.xpath('./div/div[2]/div/text()').extract()

                try:
                    item["userscore"] = each.xpath('./div/div[3]/ul/li[2]/span[2]/text()')[0].extract()
                except:
                    item["userscore"] = each.xpath('./div/div[3]/ul/li[2]/span[2]/text()').extract()

                try:
                    item["release_date"] = each.xpath('./div/div[3]/ul/li[3]/span[2]/text()')[0].extract()
                except:
                    item["release_date"] = each.xpath('./div/div[3]/ul/li[3]/span[2]/text()').extract()

                yield item

    # # 각페이지의 link로 접속하여 데이터를 가져옴
    # def parse_page_contents(self, response):
