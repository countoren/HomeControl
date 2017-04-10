from route import handleRoute

def setGpioPins(gpio):
    gpio.setup(11,gpio.OUT)

def get(self,route):
    self.wfile.write(open('livingRoom.html').read())

def post(route,data,gpio):
    handleRoute(route,[ \
            ( 'light', (lambda _: lightOn(gpio)) if data == 'on' else (lambda _: lightOff(gpio)) ) \
        ])

def lightOn(gpio): gpio.output(11,True)
def lightOff(gpio): gpio.output(11,False)

# class S(BaseHTTPRequestHandler):
#     def _set_headers(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#
#     def do_GET(self):
#         self._set_headers()
#         self.wfile.write(open('livingRoom.html').read())
#
#     def do_HEAD(self):
#         self._set_headers()
#         
#     def do_POST(self):
#         # Doesn't do anything with posted data
# 	self.data_string = self.rfile.read(int(self.headers['Content-Length']))
#
# 	if self.data_string == 'on':
# 		GPIO.output(11,True)
# 	else:
# 		GPIO.output(11,False)
#
#         self._set_headers()
#         self.wfile.write("<html><body><h1>POST!</h1></body></html>")
#         
# def run(server_class=HTTPServer, handler_class=S, port=3000):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print 'Starting httpd...'
#     httpd.serve_forever()
#
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.OUT)
# if __name__ == "__main__":
#     from sys import argv
#
#     if len(argv) == 2:
#         run(port=int(argv[1]))
#     else:
#         run()
