# -*- coding: utf-8 -*-
import scrapy

from job51.items import Job51Item


class GdJobSpider(scrapy.Spider):
    name = "gd_job"
    allowed_domains = ["www.51job.com",'search.51job.com','jobs.51job.com']
    start_urls = ['http://www.51job.com/']

    search_url = 'http://search.51job.com/list/{city},000000,0000,00,9,99,%2B,2,{page}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    def start_requests(self):
        for page_num in range(1,2001):
            yield scrapy.Request(self.search_url.format(city='030200', page=page_num), callback=self.parse)
            yield scrapy.Request(self.search_url.format(city='040000', page=page_num), callback=self.parse)
        for page_x in range(1,506):
            yield scrapy.Request(self.search_url.format(city='030500', page=page_x), callback=self.parse)

    def parse(self, response):
        jobs_list = response.css('.el p.t1 span a::attr(href)').extract()
        for jobs in jobs_list:
            yield scrapy.Request(jobs,callback=self.parse_jobs)

    def parse_jobs(self, response):
        item = Job51Item()
        item['title'] = response.css('.in .cn h1::text').extract_first()
        item['address'] = response.css('.in .cn span.lname::text').extract_first()
        item['company_name'] = response.css('.in .cn p.cname a::text').extract_first()
        item['income'] = response.css('.in .cn strong::text').extract_first()
        require = response.css('div.jtag.inbox div.t1 span.sp4')
        for x in require:
            em_num = x.css('em::attr(class)').extract_first()
            if em_num =='i1':
                item['experience'] = x.css('::text').extract_first()
            if em_num =='i2':
                item['diploma'] = x.css('::text').extract_first()
            if em_num =='i3':
                item['need_num'] = x.css('::text').extract_first()
            if em_num == 'i4':
                item['post_time'] = x.css('::text').extract_first()
        item['welfare'] = ','.join(response.css('div.jtag.inbox p.t2 span::text').extract())
        item['job_msg'] = ','.join(response.css('div.bmsg.job_msg.inbox::text').extract())
        yield item