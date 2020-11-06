# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from copy import deepcopy
from scrapy.pipelines.images import ImagesPipeline

class LearnkuspiderPipeline:
    def process_item(self, item, spider):
        return item

class LearnkuAvatarPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print("下载",item['src'])
        yield scrapy.Request(url=item['src'],meta={"item":deepcopy(item)})

    # def file_path(self, request, response=None, info=None):
    #     item=scrapy.Request.meta['item']
