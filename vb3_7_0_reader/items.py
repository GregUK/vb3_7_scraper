# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class VbForum(Item):
    """
    List of forum areas on the site
    """
    forum_id = Field()
    forum_name = Field()
    valid_forum = Field()

class VbPost(Item):
    # define the fields for your item here like:
    post_id = Field()
    user_id = Field()
    title = Field()
    content = Field()
    tags = Field()
    attachments = Field()

class VbThread(Item):
    """
    Vbulletin Thread
    """
    thread_id = Field()
    last_update = Field()
    title = Field()
    user_id = Field()

class VbUser(Item):
    """
    vbulletin user
    """
    username = Field()
    realname = Field()
    user_id  = Field()
    location = Field()



