from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from route import handleRoute
import RPi.GPIO as GPIO
import SocketServer
import livingRoom
import garden

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        handleRoute(self.path, [ \
            ('livingRoom', lambda r: livingRoom.get(self, r)) \
            , ('garden', lambda r: garden.get(self, r)) \
            ])

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
	data = self.rfile.read(int(self.headers['Content-Length']))
        handleRoute(self.path, [ \
            ('livingRoom', lambda r: livingRoom.post(r, data, GPIO)) \
            , ('garden', lambda r: garden.post(r, data, GPIO)) \
            ])

def run(server_class=HTTPServer, handler_class=S, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    GPIO.setmode(GPIO.BOARD)
    garden.setGpioPins(GPIO)
    livingRoom.setGpioPins(GPIO)
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
