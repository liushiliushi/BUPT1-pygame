# 引入需要的模块
import pygame
# 设置页面宽高
scr_width=800
scr_height =560
# 创建控制结束的状态
GAMEOVER = False
# 创建地图类
class Map():

class Rider():
    """骑手

    state：骑手的状态，空闲0/取餐1/送餐2
    stop：骑手停靠状态，路上0/餐馆1/食客2 
    x,y：骑手的坐标
    accept,over,finish,currentnumber：该骑手的接单数，超时数，完成数，当前订单数；
    """

    def __init__(self, state, stop, x, y, accept,):
        self.state = 0
        self.stop = 0
        self.x = 8
        self.y = 7
        self.accept = 0
        self.over = 0
        self.finish = 0
        self.current_number = 0

class order():
    """订单

    current_state:该单状态  未派单0/待取餐1/待送餐2/已完成3/超时完成4 
    rider_num:配送该单的骑手序号
    overtime:未超时0/超时1
    cx,cy:餐馆横纵坐标
    sx,sy；食客横纵坐标 
    """

    def __init__(self, current_state, overtime):
        self.current_state = 0
        self.overtime = 0


class Maingame():
    