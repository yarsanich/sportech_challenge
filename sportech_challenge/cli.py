import time
import argparse
from scrapy.crawler import CrawlerProcess
from spiders.cl_spider import CloddsSpider


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='parse delay for scrap')
    parser.add_argument('-d', '--delay', type=int,
                        help='minutes for delay between requests', default=1)

    args = parser.parse_args()

    try:
        while True:
            process = CrawlerProcess({
                'USER_AGENT': 'Firefox/41.0'
            })
            process.crawl(CloddsSpider)
            process.start()
            time.sleep(args.delay * 60)
    except KeyboardInterrupt:
        print ("Stopped")
