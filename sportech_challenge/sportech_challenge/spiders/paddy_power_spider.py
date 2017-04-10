from sportech_challenge.spiders.base_driver_spider import BaseDriverSpider


class PaddyPowerSpider(BaseDriverSpider):
    name = "paddy_power_spider"
    start_urls = ['http://www.paddypower.com/football/euro-football/champions-league']

    def parse(self, response):
        selector = super().parse(response)
        team_links = selector.xpath('//div[contains(@class, "fb-market-content")]//a[@class="fb-odds-button"]')
        result = dict()
        for team_link in team_links:
            name = team_link.xpath('span[@class="odds-label"]/text()').extract_first()
            coeff = team_link.xpath('span[@class="odds-value"]/text()').extract_first()
            result[name] = coeff.strip('\n')
        yield result
