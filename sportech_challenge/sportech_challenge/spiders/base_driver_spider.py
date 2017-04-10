import scrapy
from scrapy.selector import Selector
from selenium import webdriver


class BaseDriverSpider(scrapy.Spider):
    name = "base_driver_spider"

    def __init__(self):
        self.driver = webdriver.Firefox()
        super().__init__()

    def __del__(self):
        self.driver.stop()
        super().__del__()

    def parse(self, response):
        self.driver.get(response.url)
        selector = Selector(text=self.driver.page_source)
        return selector
