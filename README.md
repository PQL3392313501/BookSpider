#读取依赖项清单
pip install -r requirements.txt
#修改setting
ITEM_PIPELINES = {
  "spider.pipelines.BookSPipeline": 300,
   "spider.pipelines.DBSPipeline": 290,
}
#爬取小说到数据库或excel
scrapy crawl book 
