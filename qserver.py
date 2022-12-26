from http.server import HTTPServer, SimpleHTTPRequestHandler
from os.path import exists as path_exists

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        """Serve a GET request."""
        path = self.translate_path(self.path)
        split = path.rsplit(".", 1)
        if not path_exists(path) and (len(split) == 1):
            self.path = "/"
        SimpleHTTPRequestHandler.do_GET(self)

RequestHandler = MyHandler

if __name__ == '__main__':
    myServer = HTTPServer(('0.0.0.0', 3000), RequestHandler)
    print(">> qserver")
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print("Exiting.")
