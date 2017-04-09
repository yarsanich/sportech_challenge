import scrapy
from selenium import webdriver


class CloddsSpider(scrapy.Spider):
    name = "clodds"

    def __init__(self):
        self.driver = webdriver.Firefox()

    def start_requests(self):
        urls = [
            'http://sports.williamhill.com/bet/en-gb/betting/e/9380759/Champions+League+2016+17+-+Outright.html',
            'http://www.paddypower.com/football/euro-football/champions-league',
            'https://www.21bet.co.uk/sportsbook/SOCCER/EU_CL/269006/',
            'https://www.spreadex.com/sports/en-GB/spread-betting/Football-European/Champions-League/Champions-League-2016-17/p461635',
            'http://www.sportsbet.com.au/betting/soccer/uefa-competitions/uefa-champions-league/Champions-League-Outright-2016-17-2710742.html',
            'http://sports.coral.co.uk/football/uefa-club-comps/champions-league',
            'http://sports.titanbet.com/en/t/19161/UEFA-Champions-League?mkt_sort=X086',
            'https://mobile.bet365.com/#type=Coupon;key=1-172-1-29101630-2-0-0-0-2-0-0-4063-0-0-1-0-0-0-0-0-0;ip=0;lng=1;anim=1',
            'https://www.betstars.com/#/soccer/outrights/4167945',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.driver.get(response.url)
        title = self.driver.title
        page = self.driver.page_source
        filename = '{}.html'.format(title)
        with open(filename, 'w') as f:
            f.write(page)
        self.log('Saved file %s' % filename)
