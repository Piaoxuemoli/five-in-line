import pygame as pg
import sys

#��ʼ��pygame
pg.init()

#��������
font = pg.font.Font(None, 36)

#��ʼ�����ڴ�С
size = height, width = 640, 640
screen = pg.display.set_mode(size)

#���ô��ڱ���
pg.display.set_caption('Chess of Uzi')

#���ƺ���
def draw_board(screen):
    #��������
    for i in range(1, 16):
        pg.draw.line(screen, (0, 0, 0), (40, i*40), (width-40, i*40))
        pg.draw.line(screen, (0, 0, 0), (i*40, 40), (i*40, height-40))
    
def draw_chess(screen, x, y, color):
    #��������
    if color == 1:
        co = (0, 0, 0)
    elif color == -1:
        co = (255, 255, 255)
    pg.draw.circle(screen, co, ((x+1)*40, (y+1)*40), 15)

#����״̬����
def state_change(board, x, y, color):
    #�ı�����״̬
    board[x][y] = color

#������
class ChessBoard:
    def __init__(self):
        #��������
        self.board = [[0 for i in range(15)] for j in range(15)]

#������
class Player:
    def __init__(self, color):
        self.color = color

    def win_check(self, board,x,y):
        #check����
        countleft = 0
        countright = 0
        i=1
        while board[x][y-i]!=-self.color and y-i>-1:
            if board[x][y-i]==self.color:
                countleft+=1
            else:
                break
            i+=1
        i=1
        while board[x][y+i]!=-self.color and y+i<15:
            if board[x][y+i]==self.color:
                countright+=1
            else:
                break
            i+=1
        if countleft+countright>=4:
            return True
        #check����
        countup = 0
        countdown = 0
        i=1
        while board[x-i][y]!=-self.color and x-i>-1:
            if board[x-i][y]==self.color:
                countup+=1
            else:
                break
            i+=1
        i=1
        while board[x+i][y]!=-self.color and x+i<15:
            if board[x+i][y]==self.color:
                countdown+=1
            else:
                break
            i+=1
        if countup+countdown>=4:
            return True
        #check���ϵ�����б��
        countleftup = 0
        countrightdown = 0
        i=1
        while board[x-i][y-i]!=-self.color and x-i>-1 and y-i>-1:
            if board[x-i][y-i]==self.color:
                countleftup+=1
            else:
                break
            i+=1
        i=1
        while board[x+i][y+i]!=-self.color and x+i<15 and y+i<15:
            if board[x+i][y+i]==self.color:
                countrightdown+=1
            else:
                break
            i+=1
        if countleftup+countrightdown>=4:
            return True
        #check���ϵ�����б��
        countrightup = 0        
        countleftdown = 0
        i=1
        while board[x-i][y+i]!=-self.color and x-i>-1 and y+i<15:
            if board[x-i][y+i]==self.color:
                countrightup+=1
            else:
                break
            i+=1
        i=1
        while board[x+i][y-i]!=-self.color and x+i<15 and y-i>-1:
            if board[x+i][y-i]==self.color:
                countleftdown+=1
            else:
                break
            i+=1
        if countrightup+countleftdown>=4:
            return True
        return False

    def move(self,board,x,y):
        #���Ӻ���
        state_change(board,x,y,self.color)
        draw_chess(screen,x,y,self.color)
        state_change(board,x,y,self.color)

#��ʼ������
chessboard = ChessBoard()

#��ʼ�����
player_black = Player(1)
player_white = Player(-1)
current_player = player_black#��ʼ����Ϊ�ڷ�

#�������̺ͱ���
pg.draw.rect(screen, (173, 216, 230), (0, 0, width, height))#������ɫ    
draw_board(screen)#��������

game_over = False#��Ϸ�Ƿ����

#��Ϸ��ѭ��
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()#�˳�
        elif not game_over:
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = round(event.pos[0]/40)-1, round(event.pos[1]/40)-1#��ȡ���λ��
                current_player.move(chessboard.board,x,y)#����
                state_change(chessboard.board,x,y,current_player.color)#�ı�����״̬
                #������������
                for i in range(15):
                    for j in range(15):
                        if chessboard.board[i][j]!=0:
                            draw_chess(screen,i,j,chessboard.board[i][j])
                #�ж�ʤ��
                if current_player.win_check(chessboard.board,x,y):
                    #��ʾʤ����Ϣ
                    tb=font.render("black win!", True, (255, 0, 0))
                    tb_rect=tb.get_rect()
                    tb_rect.center=(width/2,height/2)
                    tw=font.render("white win!", True, (255, 0, 0))
                    tw_rect=tw.get_rect()
                    tw_rect.center=(width/2,height/2+30)
                    if current_player.color == 1:
                        screen.blit(tb,tb_rect)
                    else:
                        screen.blit(tw,tw_rect)
                    game_over = True

                #��������
                if current_player == player_black:
                    current_player = player_white
                else:
                    current_player = player_black
       
    #ѭ������
    pg.display.flip()
