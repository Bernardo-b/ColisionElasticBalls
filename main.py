
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:56:14 2021

@author: Bernardo
"""

import pygame
import numpy as np
from constants import *
from classes import Circle
from random import randint


def render(balls, screen):
    screen.fill(corFundo)
    for i in balls:
        i.draw(screen)
    pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(corFundo)
balls = [Circle() for i in range(10)]
for i in balls:
    i.position = np.array([float(randint(0,1500)),float(randint(0,1000)) ])


while 1:

    # for to quit game
    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.MOUSEBUTTONUP:
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:  
        screen.fill(corFundo)

    for i in balls:
        x, y = pygame.mouse.get_pos()
        i.applyPhysics(np.array([x, y]))

    for n,a in enumerate(balls):
        for b in balls[n+1:]:       
            if a.iscontact(b):
                Circle.bounce(a,b)
                

    render(balls, screen)
