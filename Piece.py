#!/usr/bin/env/python

import pygame
from common import *

class Piece(object):
    
    def __init__(self, image, start_position, color=None, radius=None, weight=None):
        self.image      = image
        self.position   = start_position
        self.color      = color
        self.weight     = weight
        self.radius     = radius
        self.velocity   = 0
        self.surface    = pygame.image.load(self.image)

    def set_position(self, new_position):
        self.position = new_position

    def current_position(self):
        return self.position

    def blit(self, app):
        surface = app.gameSurface
        #surface.blit(self.surface, (self.position.x, self.position.y))
        pygame.draw.circle(app.gameSurface, self.color, (self.position.x, self.position.y), self.radius, 0) 


class Board(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def blit(self, app):
        surface = app.gameSurface
        surface.blit(self.image, self.rect)


