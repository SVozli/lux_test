import psycopg2

class LoadFromPostgres:

    def open_connection(self):
        ## Connection Details
        hostname = '127.0.0.1'
        username = 'postgres'
        password = '12345'  # your password
        database = 'lux_realestates'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()

    def retrieve_items(self):
        self.open_connection()

        ## Define retrieve statement
        self.cur.execute(""" SELECT * from ESTATES""" )
        data = self.cur.fetchall()
        self.close_connection()


        return self.parse_data_to_html_format(data)

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