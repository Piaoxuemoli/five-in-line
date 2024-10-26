import pygame as pg
import random
import sys
import time
import numpy as np
from enum import Enum

#初始化pygame
pg.init()

#初始化窗口大小
size = height, width = 640, 640
screen = pg.display.set_mode(size)

#设置窗口标题
pg.display.set_caption('Chess of Uzi')

#棋盘类
class ChessBoard:
    def __init__(self):
        #设置棋盘
        self.board = [[0 for i in range(15)] for j in range(15)]

    def draw_board(self, screen):
        #绘制棋盘
        for i in range(1, 16):
            pg.draw.line(screen, (0, 0, 0), (40, i*40), (width-40, i*40))
            pg.draw.line(screen, (0, 0, 0), (i*40, 40), (i*40, height-40))
    
    def draw_chess(self, screen, x, y, color):
        #绘制棋子
        if color == 1:
            co = (0, 0, 0)
        elif color == -1:
            co = (255, 255, 255)
        pg.draw.circle(screen, co, (x+20, y+20), 20)

    def state_change(self, x, y, color):
        #改变棋盘状态
        self.board[x][y] = color

#游戏主循环
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
            #退出
            pg.quit()
            sys.exit()
            
    #背景颜色
    pg.draw.rect(screen, (173, 216, 230), (0, 0, width, height))

    #绘制棋盘
    

    #playstart
    #game_over = False
    #while game_over == False:

    
    #循环绘制
    pg.display.flip()
