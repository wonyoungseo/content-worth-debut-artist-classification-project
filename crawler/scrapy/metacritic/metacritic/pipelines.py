# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class metacriticPipeline(object):
    def __init__(self):
        self.csvwriter = csv.writer(open("scrapy-metacritic-1118.csv", "w"))
        self.csvwriter.writerow(["artist", "album", "metascore", "userscore", "release_date"])

    def process_item(self, item, spider):

        row = []
        row.append(item["artist"])
        row.append(item["album"])
        row.append(item["metascore"])
        row.append(item["userscore"])
        row.append(item["release_date"])
        self.csvwriter.writerow(row)

        return item
