#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import os
import sys

SCR_RECT = Rect(0, 0, 640, 480)
WHITE = (255,255,255)

class Beam(pygame.sprite.Sprite):
    """docstring for ClassName"""
    speed = -10 #移動速度
    def __init__(self, pos):
         # imageとcontainersはmain()でセットされる
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def update(self):
        self.move_up()

    def move_up(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom < SCR_RECT.top:
            self.kill()





