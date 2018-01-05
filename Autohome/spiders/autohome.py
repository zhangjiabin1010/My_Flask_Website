# -*- coding: utf-8 -*-
import scrapy
from Autohome.items import AutohomeItem

class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['https://www.autohome.com.cn/all/']
    start_urls = ['https://www.autohome.com.cn/all/']

    def parse(self, response):
#返回该表达式对应的所有selector list列表
        tit_list = response.xpath("//div[@class='article-wrapper']/ul/li/a")
        for tit in tit_list:
            item = AutohomeItem()
            #extract（）序列化为unicode字符串
            title = tit.xpath("./h3").extract()
            url = tit.xpath("./@href").extract()
            jianjie = tit.xpath("./p").extract()

            item['url'] = url[0]
            item['jianjie'] = jianjie[0]
            item['title'] = title[0]
            #返回提取到的每个item数据，传给管道处理，同时还会回来继续处理下一个数据
            yield item


#网址 //div[@class='article-wrapper']/ul/li/a/@href
#标题 //div[@class='article-wrapper']/ul/li/a/h3
#简介 //div[@class='article-wrapper']/ul/li/a/p
