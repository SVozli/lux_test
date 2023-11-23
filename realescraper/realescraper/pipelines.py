# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class RealescraperPipeline:
    def process_item(self, item, spider):
        return item

class SaveToPostgresPipeline:

    def __init__(self):
        ## Connection Details
        hostname = 'localhost'
        username = 'postgres'
        password = '********'  # your password
        database = 'lux_realestates'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        ## Create books table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS estates(
            title text,
            location text,
            images_url text
        )
        """)


    def process_item(self, item, spider):
        print(item["images_url"])
        ## Define insert statement
        self.cur.execute(""" insert into estates (
            title, 
            location,
            images_url
            ) values (
                %s,
                %s,
                %s
                )""", (
            item["title"],
            item["location"],
            item["images_url"]
        ))

        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()