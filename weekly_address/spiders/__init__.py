# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy import Spider, Request
from weekly_address.items import WeeklyAddressItem

class WeeklySpider(Spider):
    name = "dmoz"
    allowed_domains = ["whitehouse.gov"]
    start_urls = ["https://www.whitehouse.gov/briefing-room/weekly-address"]

    def parse(self, response):
        for href in response.xpath('//div/h3/a/@href'):
            url = response.urljoin(href.extract())
            yield Request(url, callback=self.parse_content)
        next_url = response.xpath('//*[@id="content-start"]/div[4]/div/div[3]/ul/li[3]/a/@href')
        if next_url:
            next_url = response.urljoin(next_url.extract()[0])
            yield Request(next_url, callback=self.parse)

    def parse_content(self, response):
        item = WeeklyAddressItem()
        item['date'] = response.xpath('//*[@id="press_article_date_created"]/text()').extract()
        item['mp3_url'] = response.xpath('//*[@id="content-start"]/div[5]/a[2]/@href').extract()
        item['mp4_url'] = response.xpath('//*[@id="content-start"]/div[5]/a[1]/@href').extract()
        item['title'] = response.xpath('//*[@id="content-start"]/div[2]/h1/text()').extract()
        item['transcribe'] = "\n".join(response.xpath('//*[@id="content-start"]/div[6]/div/div/div/p/text()').extract()[1:-1])
        yield item
