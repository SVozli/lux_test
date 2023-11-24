import scrapy
import json
from ..items import RealescraperItem

class EstatespiderSpider(scrapy.Spider):
    name = "estatespider"
    allowed_domains = ["www.sreality.cz"]
    # We can just query the  site for all 500 items at once.
    start_urls = ["https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&page=1&per_page=500"]

    def parse(self, response):
        # Since we query directly, we get a json response and don't have to extract data from css.
        data = json.loads(response.text)

        for estate in data['_embedded']['estates']:
            estate_item = RealescraperItem()
            estate_item['title'] = estate['name']
            estate_item['location'] = estate['locality']
            # Put all of the image URLs into a ; deliminated string.
            images_url_str = ""
            try:
                for image_href_dict in estate['_links']['images']:
                    images_url_str += image_href_dict['href'] +"; "
            except:
                print("No image url found.")
                pass
            estate_item['images_url'] = images_url_str

            yield estate_item