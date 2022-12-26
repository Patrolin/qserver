from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
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
    myServer = ThreadingHTTPServer(('127.0.0.1', 3000), RequestHandler)
    print(">> qserver")
    try:
        myServer.serve_forever(.1)
    except KeyboardInterrupt:
        print("Exiting...")

    myServer.server_close()
