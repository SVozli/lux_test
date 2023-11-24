from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from server.db_read import LoadFromPostgres

hostName = "127.0.0.1"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("before estates")
        loader = LoadFromPostgres()
        estates = loader.retrieve_items()
        print("did we read estates?")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Luxonis test</title></head>", "utf-16"))
        self.wfile.write(bytes("<h1>Scraped estates</h1>", "utf-16"))
        self.wfile.write(bytes("<body>", "utf-16"))

        for line in estates:
            self.wfile.write(bytes(line, "utf-16"))
        self.wfile.write(bytes("<body>", "utf-16"))
        self.wfile.write(bytes("</body></html>", "utf-16"))

def  run_server():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        pass

    webServer.server_close()
    print("Server stopped.")

