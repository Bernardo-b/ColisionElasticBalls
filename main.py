
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:56:14 2021

@author: Bernardo
"""
#imports
import pygame
import numpy as np
from constants import *
from classes import Circle
from random import randint

#função de renderização
def render(balls, screen):
    screen.fill(corFundo)
    for i in balls:
        i.draw(screen)
    pygame.display.update()

#inicia a simulção
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(corFundo)

#cria as bolas
balls = [Circle() for i in range(50)]
for i in balls:
    i.position = np.array([float(randint(0,3000)),float(randint(0,3000))])
    i.radius = randint(20,100)

#loop principal
while 1:
    # for to quit game
    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
    # for para expandir as bolas
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        x, y = pygame.mouse.get_pos()
        for i in balls:
            i.expand(np.array([x, y])         )
    # for para aplicar a física nas bolas
    for i in balls:
        x, y = pygame.mouse.get_pos()
        i.applyPhysics(np.array([x, y]))
    # for para colisões
    for n,a in enumerate(balls):
        for b in balls[n+1:]:       
            if a.iscontact(b):
                Circle.bounce(a,b)
    # chama a função de renderização
    render(balls, screen)
