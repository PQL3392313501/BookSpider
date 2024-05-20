import scrapy
from scrapy import Selector, Request
from spider.items import bookItem

class bookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["bqguu.cc"]
    start_urls = ["https://www.bqguu.cc/top/"]

    def parse(self, response):
        sel = Selector(response)
        book_item = sel.css('body > div.wrap.rank')
        for book in book_item:
            item = bookItem()
            # 确保选择器路径正确
            item['bd'] = book.css('div.blocks>h2::text').extract()
            item['itm_text'] = book.css('div.blocks>ul>li>a::text').extract()
            item['item'] = book.css('div.blocks>ul> li::text').extract()
            item['itm_href'] = book.css('div.blocks>ul>li>a::attr(href)').extract()
            # print(item)  # 打印主页面的信息
            yield item
    #         for href in item['itm_href']:
    #             absolute_url = response.urljoin(href)
    #             print(absolute_url)
    #             yield Request(url=absolute_url, callback=self.parse_book_details)
    #
    # def parse_book_details(self, response):
    #     sel = Selector(response)
    #     item = bookItem()
    #     item['title'] = sel.css("dt::text").extract()
    #     item['zj'] = sel.css("dd>a::text").extract()
    #     item['zs'] = sel.css("dd>a::attr(href)").extract()
    #     yield item
