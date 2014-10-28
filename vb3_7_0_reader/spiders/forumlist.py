from pip._vendor.pkg_resources import to_filename

__author__ = 'smithg'

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from ..items import VbForum
from urlparse import urlparse, parse_qs
class VbForumSpider(CrawlSpider):
    name = "s2forum_forum"

    def __init__(self, domain="www.s2forum.com", http_user="", http_pass="", to_file=False, *args, **kwargs):
        super(VbForumSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://{0}/forum/index.php'.format(domain)]
        self.http_user = http_user
        self.http_pass = http_pass
        self.to_file = to_file

    def parse(self, response):
        if self.to_file:
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