import os
from realescraper.realescraper.spiders.estatespider import EstatespiderSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import server.server_setup as srv_stp

if __name__ == "__main__":
    settings_file_path = 'realescraper.realescraper.settings'  # The path seen from root, ie. from main.py
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
    process = CrawlerProcess(get_project_settings())
    process.crawl(EstatespiderSpider)
    process.start()

    srv_stp.run_server()


