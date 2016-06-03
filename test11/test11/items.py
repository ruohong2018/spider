# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LkischoolItem(scrapy.Item):
    # define the fields for your item here like:
    school_url = scrapy.Field()
    school_name = scrapy.Field()
    school_logo = scrapy.Field()
    school_img = scrapy.Field()
    work_direction=scrapy.Field()
    work_field=scrapy.Field()
    gen_message=scrapy.Field()
    website=scrapy.Field()
    contact_number=scrapy.Field()
    address=scrapy.Field()
    school_year=scrapy.Field()
    school_type=scrapy.Field()
    ts_statistic=scrapy.Field()
    finance_infor=scrapy.Field()
    location = scrapy.Field()
    '''
    
    
    website=scrapy.Field()
    
    #similar = scrapy.Field()
    school_img = scrapy.Field()
    work_direction=scrapy.Field()
    work_field=scrapy.Field()
    
    
    '''
    pass
