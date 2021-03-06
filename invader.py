#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import os
import sys
import beam

SCR_RECT = Rect(0, 0, 640, 480)
WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
    """自機"""
    speed = 5  # 移動速度
    def __init__(self):
        # imageとcontainersはmain()でセットされる
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom =　SCR _RECT.bottom  # プレイヤーが画面の一番下
    def update(self):
        # 押されているキーをチェック
        pressed_keys = pygame.key.get_pressed()
        # 押されているキーに応じてプレイヤーを移動
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        self.rect.clamp_ip(SCR_RECT)
        #スペースキーが押されたらショット！！！！
        if pressed_keys[K_SPACE]:
           beam.Beam(self.rect.center)

