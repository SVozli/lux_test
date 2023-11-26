import logging

import psycopg2

class LoadFromPostgres:

    def open_connection(self):
        ## Connection Details
        hostname = 'db'
        port = 5432
        username = 'postgres'
        password = '12345'  # your password
        database = 'lux_realestates'

        logging.warning("Before  DB connect")
        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,  port=port)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        self.show_query(self.cur, 'current database', 'SELECT current_database()')

    def retrieve_items(self):
        self.open_connection()
        self.show_query(self.cur, 'current database', "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")

        ## Define retrieve statement
        self.cur.execute(""" SELECT * from estates""")
        data = self.cur.fetchall()
        logging.warning(data)
        self.close_connection()


        return self.parse_data_to_html_format(data)

    def show_query(self,cur,title, qry):
        logging.warning('%s' % (title))
        cur.execute(qry)
        for row in cur.fetchall():
            logging.warning((row))
        logging.warning((''))

    def close_connection(self):
        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()

    def parse_data_to_html_format(self, data):
        output = []

        for estate in data:
            title = estate[0]
            location = estate[1]
            images_urls = estate[2]
            images_urls = images_urls.split("; ")
            estate_line = ""
            estate_line += "<div class='myEstate'>\n"
            estate_line += "    <h2>{}</h2>\n".format(title)
            estate_line += "    <p>{}</p>\n".format(location)
            estate_line += '    <img src="{}">\n'.format(images_urls[0])
            estate_line += "</div>\n"
            output.append(estate_line)

        return output