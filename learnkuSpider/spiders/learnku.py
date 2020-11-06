import scrapy
from ..items import LearnkuspiderItem

class LearnkuSpider(scrapy.Spider):
    name = 'learnku'
    allowed_domains = ['learnku.com']
    start_urls = ['https://learnku.com/laravel?page=1']

    def parse(self, response):
        item=LearnkuspiderItem()
        div_list=response.xpath("//div[contains(@class,'user-avatar')]")
        for div in div_list:
            item['src']=div.xpath("./a/img/@src").get()
            yield item
        nex_page=response.xpath("//a[@rel='next']/@href").get()
        if(nex_page):
             yield scrapy.Request(nex_page,callback=self.parse)