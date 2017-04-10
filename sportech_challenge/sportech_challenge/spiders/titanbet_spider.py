from sportech_challenge.spiders.base_driver_spider import BaseDriverSpider


class TitanBetSpider(BaseDriverSpider):
    name = "titanbet_spider"
    start_urls = ['http://sports.titanbet.com/en/t/19161/UEFA-Champions-League?mkt_sort=X086']

    def parse(self, response):
        selector = super().parse(response)
        team_buttons = selector.xpath('//div[@id="main-area"]//div[@class="expander-content"]//li[@class="limited-row"]/button[contains(@class, "price")]')
        result = dict()
        for button in team_buttons:
            name = button.xpath('span/span/span/span[@class="seln-name"]/text()').extract_first()
            coeff = button.xpath('span/span[contains(@class, "dec")]/text()').extract_first()
            result[name] = coeff
        yield result
