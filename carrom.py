#!/usr/bin/env python

import pygame
from Piece import *
from Controller import *
from common import *
from board2 import *



class Application(object):
    def __init__(self, appName, display_width = 800, display_height = 800):
        self.appName = appName
        self.display_width = display_width
        self.display_height = display_height
        pygame.init()

        self.gameSurface = pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption(appName)
        self.clock = pygame.time.Clock()
        self.running = True
        self.board   = Board("img/carrom_3.png", [100, 50])
        #self.board   = Board2(600, Coordinate(100,100))



def update_text(title, text, app, x, y):
    basicfont = pygame.font.SysFont(None, 20)
    text = basicfont.render("{0} => {1}".format(title, text), True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = x
    textrect.centery = y
    app.gameSurface.blit(text, textrect)

app = Application("Carrom Application")
strikeController = Controller()
start_position = Coordinate(int(app.display_width * 0.5), int(app.display_height * 0.5))
striker = Piece("img/striker_2.png", start_position, Colors.MAROON, 12)
clock = pygame.time.Clock()

flag = True
force = 0
angle = 0

increase_force = False
increase_angle = False
decrease_angle = False
decrease_force = False

def trigger_movement(force, angle):
    app.gameSurface.fill(Colors.WHITE)
    strikeController.translate(striker, force, angle, app)


while app.running:
    for event in pygame.event.get():                                                                          
        if event.type == pygame.QUIT:                                                                         
            app.running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                increase_force = True


            if event.key == pygame.K_DOWN:
                decrease_force = True

            if event.key == pygame.K_RIGHT:
                decrease_angle = True

            if event.key == pygame.K_LEFT:
                increase_angle = True

            if event.key == pygame.K_RSHIFT:
                trigger_movement(force, angle)
                force = angle = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                increase_force = False

            if event.key == pygame.K_DOWN:
                decrease_force = False

            if event.key == pygame.K_LEFT:
                increase_angle = False

            if event.key == pygame.K_RIGHT:
                decrease_angle = False


    if increase_force:
        force += 1

    if increase_angle:
        angle = (angle + 1)%360

    if decrease_force and force >0:
        force += -1

    if decrease_angle:
        angle = (angle - 1)%360
        
    app.gameSurface.fill(Colors.WHITE)
    app.board.blit(app)
    striker.blit(app)
    update_text("force", force, app, 40, 20)        
    update_text("angle", angle, app, 40, 40)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
