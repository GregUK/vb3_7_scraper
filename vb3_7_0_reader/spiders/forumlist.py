__author__ = 'smithg'

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from ..items import VbForum
from urlparse import urlparse, parse_qs
class VbForumSpider(CrawlSpider):
    name = "s2forum_forum"

    def __init__(self, domain="www.s2forum.com", http_user="", http_pass="", *args, **kwargs):
        super(VbForumSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://{0}/forum/index.php'.format(domain)]
        self.http_user = http_user
        self.http_pass = http_pass

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)

        items = []
        hxs =Selector(response)
        forum_table = hxs.xpath("/html/body/div/div/div/table//*/div/a[contains(@href, 'forumdisplay')]")
        for table_item in forum_table:
            item = VbForum()
            url_params = urlparse(table_item.xpath('@href').extract()[0])
            if url_params.query:
                item['forum_name'] = table_item.xpath('*/text()').extract()
                forum_id = parse_qs(url_params.query).get('f')
                if forum_id:
                    item['forum_id'] = forum_id
            items.append(item)

        return items