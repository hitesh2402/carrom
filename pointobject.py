#!/usr/bin/env/python

class PointObject(object):
    
    def __init__(self, weight, position):
        self.weight = weight
        self.position = position

    def set_position(self, position):
       self.position = position

if __name__ == '__main__':
    main()

