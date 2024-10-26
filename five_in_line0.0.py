import pygame as pg
import random
import sys
import time
import numpy as np
from enum import Enum

#��ʼ��pygame
pg.init()

#��ʼ�����ڴ�С
size = height, width = 640, 640
screen = pg.display.set_mode(size)

#���ô��ڱ���
pg.display.set_caption('Chess of Uzi')

#������
class ChessBoard:
    def __init__(self):
        #��������
        self.board = [[0 for i in range(15)] for j in range(15)]

    def draw_board(self, screen):
        #��������
        for i in range(1, 16):
            pg.draw.line(screen, (0, 0, 0), (40, i*40), (width-40, i*40))
            pg.draw.line(screen, (0, 0, 0), (i*40, 40), (i*40, height-40))
    
    def draw_chess(self, screen, x, y, color):
        #��������
        if color == 1:
            co = (0, 0, 0)
        elif color == -1:
            co = (255, 255, 255)
        pg.draw.circle(screen, co, (x+20, y+20), 20)

    def state_change(self, x, y, color):
        #�ı�����״̬
        self.board[x][y] = color

#��Ϸ��ѭ��
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
            #�˳�
            pg.quit()
            sys.exit()
            
    #������ɫ
    pg.draw.rect(screen, (173, 216, 230), (0, 0, width, height))

    #��������
    

    #playstart
    #game_over = False
    #while game_over == False:

    
    #ѭ������
    pg.display.flip()
