from realescraper.realescraper.spiders.estatespider import EstatespiderSpider
from scrapy.crawler import CrawlerProcess
import server.server_setup as srv_stp

if __name__ == "__main__":
    process = CrawlerProcess({})
    process.crawl(EstatespiderSpider)
    process.start()

    srv_stp.run_server()


