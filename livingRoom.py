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
