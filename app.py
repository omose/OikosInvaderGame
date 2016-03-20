#!/usr/bin/env python
#coding: utf-8
import pygame
from pygame.locals import *
import os
import sys
import invader
import function

SCR_RECT = Rect(0, 0, 640, 480)
WHITE = (255,255,255)

class InvaderGame:
    def __init__(self):
        pygame.init()
        #ウインドの設定
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption(u"Oikos Invader Game")

        # スプライトグループを作成して登録
        all = pygame.sprite.RenderUpdates()
        invader.Player.containers = all

        # スプライトの画像を登録
        invader.Player.image = function.load_image("player.png")
        
        # 自機を作成
        invader.Player()
        
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            screen.fill((0, 0, 0))
            all.update()
            all.draw(screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    InvaderGame()