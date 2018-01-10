#!/usr/bin/env python

import pygame
from common import *

class Board2(object):
    def __init__(self, size, position):
        self.width = self.height = size
        self.position = position
        self.pocket_size = int(.04 * size)
        self.side_length = int(.63 * size)
        self.side_shift  = int(.14 * size)
        self.strip_width = int(.03 * size)


    def blit(self, app):
        surface = app.gameSurface
        surface.fill(Colors.WHITE)
        pygame.draw.rect(surface, Colors.BLACK,(self.position.x, self.position.y, self.width, self.height), 1)
        pygame.draw.circle(  surface \
                            ,Colors.BLUE \
                            ,(self.position.x + self.pocket_size, self.position.y + self.pocket_size) \
                            ,self.pocket_size \
                            , 0)
        pygame.draw.circle(  surface \
                            ,Colors.BLUE \
                            ,(self.position.x + self.pocket_size, self.position.y + self.height - self.pocket_size) \
                            ,self.pocket_size \
                            , 0)
        pygame.draw.circle(  surface \
                            ,Colors.BLUE \
                            ,(self.position.x + self.width - self.pocket_size, self.position.y + self.height - self.pocket_size) \
                            ,self.pocket_size \
                            , 0)
        pygame.draw.circle(  surface \
                            ,Colors.BLUE \
                            ,(self.position.x + self.width - self.pocket_size, self.position.y + self.pocket_size) \
                            ,self.pocket_size \
                            , 0)

        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + int(self.width/2) + self.side_length/2 , self.position.y + self.height - self.side_shift - self.strip_width/2) \
                            ,self.strip_width/2 \
                            , 1)

        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + int(self.width/2) + self.side_length/2 , self.position.y + self.side_shift + self.strip_width/2) \
                            ,self.strip_width/2 \
                            , 1)

        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + int(self.width/2) - self.side_length/2 , self.position.y + self.height - self.side_shift - self.strip_width/2) \
                            ,self.strip_width/2 \
                            , 1)
        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + int(self.width/2) - self.side_length/2 , self.position.y + self.side_shift + self.strip_width/2) \
                            ,self.strip_width/2 \
                            , 1)

        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + self.side_shift + self.strip_width/2, self.position.y + self.height/2 + self.side_length/2)\
                            ,self.strip_width/2\
                            , 1)
        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + self.side_shift + self.strip_width/2, self.position.y + self.height/2 - self.side_length/2)\
                            ,self.strip_width/2\
                            , 1)
        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + self.width - self.side_shift - self.strip_width/2, self.position.y + self.height/2 - self.side_length/2)\
                            ,self.strip_width/2\
                            , 1)
        pygame.draw.circle(  surface \
                            ,Colors.RED \
                            ,(self.position.x + self.width - self.side_shift - self.strip_width/2, self.position.y + self.height/2 + self.side_length/2)\
                            ,self.strip_width/2\
                            , 1)


        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + int(self.width/2) + self.side_length/2, self.position.y + self.side_shift),\
                                                            (self.position.x + int(self.width/2) - self.side_length/2, self.position.y + self.side_shift)]\
                                                            ,1)
        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + int(self.width/2) + self.side_length/2, self.position.y + self.strip_width + self.side_shift),\
                                                            (self.position.x + int(self.width/2) - self.side_length/2, self.position.y + self.strip_width + self.side_shift)]\
                                                            ,1)

        
        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + int(self.width/2) + self.side_length/2, self.position.y + self.height - self.side_shift),\
                                                            (self.position.x + int(self.width/2) - self.side_length/2, self.position.y + self.height - self.side_shift)]\
                                                            ,1)
        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + int(self.width/2) + self.side_length/2, self.position.y + self.height - self.strip_width - self.side_shift),\
                                                            (self.position.x + int(self.width/2) - self.side_length/2, self.position.y + self.height - self.strip_width - self.side_shift)]\
                                                            ,1)




        
        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + self.side_shift, self.position.y + int(self.height/2) + self.side_length/2),\
                                                            (self.position.x + self.side_shift, self.position.y + int(self.height/2) - self.side_length/2)]\
                                                            ,1)
        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + self.side_shift + self.strip_width, self.position.y + int(self.height/2) + self.side_length/2),\
                                                            (self.position.x + self.side_shift + self.strip_width, self.position.y + int(self.height/2) - self.side_length/2)]\
                                                            ,1)

        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + self.width - self.side_shift, self.position.y + int(self.height/2) + self.side_length/2),\
                                                            (self.position.x + self.width - self.side_shift, self.position.y + int(self.height/2) - self.side_length/2)]\
                                                            ,1)
        pygame.draw.lines(   surface, Colors.BLACK, False, [(self.position.x + self.width - self.side_shift - self.strip_width, self.position.y + int(self.height/2) + self.side_length/2),\
                                                            (self.position.x + self.width - self.side_shift - self.strip_width, self.position.y + int(self.height/2) - self.side_length/2)]\
                                                            ,1)

#gameSurface = pygame.display.set_mode((800, 800))
#
#pygame.display.set_caption("test Canvas")
#board = Board(400, Coordinate(100,100))
#
#
#running = True
#
#while running:
#
#    for event in pygame.event.get():                                                                          
#        if event.type == pygame.QUIT:                                                                         
#            running = False
#    
#    gameSurface.fill(Colors.WHITE)
#    board.blit(gameSurface)
#    pygame.display.update()
#    clock.tick(60)



