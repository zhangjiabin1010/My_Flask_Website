# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AutohomePipeline(object):
    def __init__(self):
#创建文件,以二进制格式存入
        self.f = open("autohomet.json","wb")
#获取到每一个item，
    def process_item(self, item, spider):
#json.dumps无法直接转item，所以需要把item强制转换成dict，即可操作。
#ensure_ascii，json.jump默认为ascii码，所以需要改为false来显示中文
        content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
#把content以utf-8的形式写入
        self.f.write(content.encode("utf-8"))
#把item返回给引擎，告诉引擎可以处理下一个item数据了。所有item数据处理完毕，
# 执行下面关闭方法
        return item

    def close_spider(self,spider):
        self.f.close()
