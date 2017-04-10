#!/usr/bin/env python
from route import handleRoute

def setGpioPins(gpio):
    gpio.setup(7,gpio.OUT)

def get(self,route):
    self.wfile.write(open('garden.html').read())

def post(route,data,gpio):
    handleRoute(route,[ \
            ( '1', (lambda _: berez1On(gpio)) if data == 'on' else (lambda _: berez1Off(gpio)) ) \
        ])

def berez1On(gpio): gpio.output(7,True)
def berez1Off(gpio): gpio.output(7,False)
