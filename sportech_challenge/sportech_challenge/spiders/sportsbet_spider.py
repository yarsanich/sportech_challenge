from sportech_challenge.spiders.base_driver_spider import BaseDriverSpider


class TOBetSpider(BaseDriverSpider):
    name = "sportsbet_spider"
    start_urls = ['http://www.sportsbet.com.au/betting/soccer/uefa-competitions/uefa-champions-league/Champions-League-Outright-2016-17-2710742.html']

    def parse(self, response):
        selector = super().parse(response)
        team_links = selector.xpath('//div[@id="ev_body"]//div[@class="accordion-body"]//a[contains(@class, "price")]')
        result = dict()
        for team_link in team_links:
            name = team_link.xpath('span[contains(@class, "team-name")]/text()').extract_first()
            coeff = team_link.xpath('span[contains(@class, "odd-val")]/text()').extract_first()
            result[name] = coeff.strip('\n')
        yield result
