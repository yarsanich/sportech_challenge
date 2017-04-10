from sportech_challenge.spiders.base_driver_spider import BaseDriverSpider


class WilliamHillSpider(BaseDriverSpider):
    name = "william_hill_spider"
    start_urls = ['http://sports.williamhill.com/bet/en-gb/betting/e/9380759/Champions+League+2016+17+-+Outright.html']

    def parse(self, response):
        selector = super().parse(response)
        team_links = selector.xpath('//div[@class="marketHolderExpanded"]//td[@scope="col"]')
        result = dict()
        for team_link in team_links:
            name = team_link.xpath('div/div[@class="eventselection"]/text()').extract_first()
            coeff = team_link.xpath('div/div[@class="eventprice"]/text()').extract_first()
            name = name.replace("\t", "").replace("\n", "")
            name = name.strip()
            result[name] = coeff.replace("\t", "").replace("\n", "")
        yield result
