# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

from scrapy.http import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils import spider


class YuerbaoPipeline(object):
    def process_item(self, item, spider):
        return item


class YuerbaoVideoPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        ## start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('FilesPipeline.file_key(url) method is deprecated, please use '
                          'file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() method has been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        ## end of deprecation warning block
        spider.logger.debug('视频地址:%s' % url)
        name = re.findall(r"^http:\/\/v0\.beicdn\.com\/upload\/time\/(\d{4}\/\d{2}.*\.mp4).*", url)
        video_name = name[0]
        spider.logger.info('视频名称:%s' % video_name)
        # media_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        # media_ext = os.path.splitext(url)[1]  # change to request.url after deprecation
        return 'videos/%s' % video_name


class TestPipeline(FilesPipeline):
    pass


class YuerbaoImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        ## start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        ## end of deprecation warning block

        spider.logger.debug('图片地址:%s' % url)
        name = re.findall(r"^http:\/\/b8\.beicdn\.com\/upload\/time\/(\d{4}\/\d{2}.*)\.jpg$", url)
        image_guid = name[0]
        spider.logger.info('图片名称:%s' % image_guid)

        # image_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        return 'images/%s.jpg' % (image_guid)
