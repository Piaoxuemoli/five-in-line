import pygame as pg
import sys

#初始化pygame
pg.init()

#设置字体
font = pg.font.Font(None, 36)

#初始化窗口大小
size = height, width = 640, 640
screen = pg.display.set_mode(size)

#设置窗口标题
pg.display.set_caption('Chess of Uzi')

#绘制函数
def draw_board(screen):
    #绘制棋盘
    for i in range(1, 16):
        pg.draw.line(screen, (0, 0, 0), (40, i*40), (width-40, i*40))
        pg.draw.line(screen, (0, 0, 0), (i*40, 40), (i*40, height-40))
    
def draw_chess(screen, x, y, color):
    #绘制棋子
    if color == 1:
        co = (0, 0, 0)
    elif color == -1:
        co = (255, 255, 255)
    pg.draw.circle(screen, co, ((x+1)*40, (y+1)*40), 15)

#棋盘状态函数
def state_change(board, x, y, color):
    #改变棋盘状态
    board[x][y] = color

#棋盘类
class ChessBoard:
    def __init__(self):
        #设置棋盘
        self.board = [[0 for i in range(15)] for j in range(15)]

#棋手类
class Player:
    def __init__(self, color):
        self.color = color

    def win_check(self, board,x,y):
        #check横向
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
        #check纵向
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
        #check左上到右下斜向
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
        #check右上到左下斜向
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
        #走子函数
        state_change(board,x,y,self.color)
        draw_chess(screen,x,y,self.color)
        state_change(board,x,y,self.color)

#初始化棋盘
chessboard = ChessBoard()

#初始化玩家
player_black = Player(1)
player_white = Player(-1)
current_player = player_black#起始棋手为黑方

#绘制棋盘和背景
pg.draw.rect(screen, (173, 216, 230), (0, 0, width, height))#背景颜色    
draw_board(screen)#绘制棋盘

game_over = False#游戏是否结束

#游戏主循环
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()#退出
        elif not game_over:
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = round(event.pos[0]/40)-1, round(event.pos[1]/40)-1#获取鼠标位置
                current_player.move(chessboard.board,x,y)#走子
                state_change(chessboard.board,x,y,current_player.color)#改变棋盘状态
                #画出所有棋子
                for i in range(15):
                    for j in range(15):
                        if chessboard.board[i][j]!=0:
                            draw_chess(screen,i,j,chessboard.board[i][j])
                #判断胜负
                if current_player.win_check(chessboard.board,x,y):
                    #显示胜利信息
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

                #交换棋手
                if current_player == player_black:
                    current_player = player_white
                else:
                    current_player = player_black
       
    #循环绘制
    pg.display.flip()
