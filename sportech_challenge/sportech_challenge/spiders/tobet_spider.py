from sportech_challenge.spiders.base_driver_spider import BaseDriverSpider


class TOBetSpider(BaseDriverSpider):
    name = "21Bet_spider"
    start_urls = ['https://www.21bet.co.uk/sportsbook/SOCCER/EU_CL/269006/']

    def parse(self, response):
        selector = super().parse(response)
        team_links = selector.xpath('//div[@class="app--market__row"]//div[@class="app__content"]//li[@class="app--market__list"]')
        result = dict()
        for team_link in team_links:
            name = team_link.xpath('div/span[@class="app--market__entry__name"]/text()').extract_first()
            coeff = team_link.xpath('div/span[@class="app--market__entry__value"]/text()').extract_first()
            result[name] = coeff
        yield result
