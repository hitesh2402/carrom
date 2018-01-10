#!/usr/bin/env/python

class Position(object):
    
    def __init__(self, time, point):
        self.time = time
        self.point = point

class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Colors():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED   = (255, 0, 0)
    BLUE  = (0, 0, 255)
    MAROON = (128, 0, 0)
