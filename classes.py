# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:56:33 2021

@author: Bernardo
"""

from random import randint,choice
import pygame
from constants import *
from math import hypot, atan
import numpy as np


class Circle():
    def __init__(self):
        self.position = np.array([0.,0.])
        self.velocity = np.array([0.,0.])
        self.acceleration = np.array([0.,0.])
        self.force = np.array([0.,0.])
        self.color = choice(colorlist)
        self.radius = 50
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(round(i)) for i in self.position], self.radius , 0)
        
    def applyPhysics(self,mousePos):
        self.force = (mousePos-self.position)-(self.velocity*amortConst*self.radius)
        self.acceleration = self.force/((self.radius**2)*massConst)
        self.velocity += self.acceleration
        self.position += self.velocity
        
    def expand(self, mousePos):
        self.velocity = 10*(self.position-mousePos)/np.linalg.norm((self.position-mousePos))
    
    def iscontact(self,ball):
        return hypot((ball.position[0] - self.position[0]), (ball.position[1]- self.position[1])) <= (self.radius + ball.radius)
    
    @staticmethod
    def bounce(a,b):
        rot90 = np.array([[0,-1],[1,0]])
        normvec = np.array([[b.position[0]-a.position[0]],[b.position[1]-a.position[1]]])
        normvec = normvec/np.linalg.norm(normvec)
        tangvec = rot90@normvec
        rotmatrix = np.concatenate((normvec,tangvec),axis =1)
        vA = rotmatrix@a.velocity.reshape(2,1)
        vB = rotmatrix@b.velocity.reshape(2,1)
        vAN = (vA[0]*(a.radius**2-b.radius**2)+2*b.radius**2*vB[0])/(a.radius**2+b.radius**2)
        vBN = (vB[0]*(b.radius**2-a.radius**2)+2*a.radius**2*vA[0])/(a.radius**2+b.radius**2)
        vA = np.array([[vAN],[vA[1]]]).reshape(2,1)
        vB = np.array([[vBN],[vB[1]]]).reshape(2,1)
        vA = np.linalg.inv(rotmatrix)@vA
        vB = np.linalg.inv(rotmatrix)@vB
        a.velocity = 0.999*vA.T.reshape(2,)
        b.velocity = 0.999*vB.T.reshape(2,)
        distIn = ((a.radius + b.radius)-hypot((b.position[0] - a.position[0]), (b.position[1]- a.position[1]))+1)/2
        a.position -= distIn*normvec.T.reshape(2,)
        b.position += distIn*normvec.T.reshape(2,)