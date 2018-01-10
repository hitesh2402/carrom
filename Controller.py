#!/usr/bin/env python

from common import *
import math
import pygame

clock = pygame.time.Clock() 
class Controller(object):

    def __init__(self, state=0, step=3, factor=1, counter=0, direction=False):
        self.state = state
        self.step = step
        self.factor = factor
        self.counter = counter
        self.direction = direction
        self.angle = 0
    
    def getNextPosition(self, current_position):
        x = current_position.x
        y = current_position.y
        self.counter += 1
        if not self.counter % 80:
            self.state = (self.state + 1)%2
            if not self.state:
                self.factor *= -1
            self.direction = not self.direction

        if self.direction:
            y = y + (self.factor * self.step)
        else:
            x = x + (self.factor * self.step)

        return Coordinate(x, y)

    def getNextPosition3(self, current_position):
        radius = 90 
        x = 400 + radius * math.cos(math.radians(self.angle))
        y = 300 + radius * math.sin(math.radians(self.angle))
        self.angle = (self.angle + 5)%360
        return Coordinate(int(x), int(y))

    def translate(self, obj, distance, angle, app):
        surface = app.gameSurface
        if distance <= 0:
            return
        curr_position = obj.current_position()
        x = curr_position.x + 2*math.cos(math.radians(angle))
        y = curr_position.y + 2*math.sin(math.radians(angle))
        new_position = Coordinate(int(x), int(y))
        obj.set_position(new_position)
        app.board.blit(app)
        obj.blit(app)
        pygame.display.update()
        clock.tick(40)
        self.translate(obj, distance-2, angle, app)

