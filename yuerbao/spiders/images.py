# -*- coding: utf-8 -*-
import json
import logging
from urllib.parse import urlencode

import scrapy

from yuerbao.items import YuerbaoImageItem


class ImagesSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'yuerbao.pipelines.YuerbaoImagePipeline': 1}
    }
    name = 'images'
    allowed_domains = ['yuerbao.com']
    total_page = 316
    page_size = 30
    method = 'yuerbao.web.monent.get'
    bid = 1118523
    type = 0
    queryDict = {
        'page': 1,
        'page_size': 30,
        'method': 'yuerbao.web.monent.get',
        'bid': '1118523',
        'type': 0
    }
    headers = {
        'cookie': 'Hm_lvt_58d4b8228805493be11dfc9ce26e1baa=1612167785; st_au=NDc3OTg2OTU; outer=vIddoLZovI; _last_login_id_=1539%2A%2A%2A1586; _logged_=47798695; _grade_=0; _is_login_=1; _lr_=https%3A%2F%2Fwww.yuerbao.com%2F; JSESSIONID=76732265593vcb5np4n1amk3fud5fg86td93nd843fabed2; hxid=8db024820b2fd9e9d88052f89e6bb245',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    cookies = {
        'JSESSIONID': '76825282859rphs1r4g1oe67cngh1iof8j1ik574a67bed2',
    }

    def start_requests(self):
        url = 'https://api.yuerbao.com/h5_gateway/route.html?'
        queryUrl = url + urlencode(self.queryDict)
        logging.info("开始爬取 %s " % queryUrl)
        yield scrapy.Request(
            url=queryUrl,
            callback=self.parse, headers=self.headers, cookies=self.cookies)

    def parse(self, response):
        data = json.loads(response.body)
        logging.info('解析数据 page %d,size %d' % (data['page'], data['page_size']))
        for image in data['down_urls']:
            logging.debug('图片地址')
            logging.debug(image)
            yield YuerbaoImageItem(image_urls=[image])

        if self.queryDict['page'] < self.total_page:
            self.queryDict['page'] = self.queryDict['page'] + 1
            url = 'https://api.yuerbao.com/h5_gateway/route.html?'
            queryUrl = url + urlencode(self.queryDict)
            logging.info("开始爬取 %s " % queryUrl)
            yield scrapy.Request(
                url=queryUrl,
                callback=self.parse, headers=self.headers, cookies=self.cookies)
