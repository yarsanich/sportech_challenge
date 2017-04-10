from sportech_challenge.spiders.base_driver_spider import BaseDriverSpider


class CoralSpider(BaseDriverSpider):
    name = "coral_spider"
    start_urls = ['http://sports.coral.co.uk/football/uefa-club-comps/champions-league']

    def parse(self, response):
        selector = super().parse(response)
        matches = selector.xpath('//div[@class="in-play-odds"]//div[@class="matches"]//div[contains(@class, "featured-match")]')
        result = dict()
        for match in matches:
            title = match.xpath('div[@class="bet-title"]/a/span/text()').extract_first()
            team_1, team_2 = title.split(' v ')
            coeff_1 = match.xpath('div[@class="home-odds"]/div/span[@class="odds-decimal"]/text()').extract_first()
            coeff_2 = match.xpath('div[@class="away-odds"]/div/span[@class="odds-decimal"]/text()').extract_first()
            result[team_1] = coeff_1.strip('\n')
            result[team_2] = coeff_2.strip('\n')
        yield result
