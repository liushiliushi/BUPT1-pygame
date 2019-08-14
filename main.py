import pygame
import sys
from rider import *
import threading
import input
import output
import globalvar as gl
gl._init() # initialize
pygame.init() # initialize
def buy_riders():
    while gl.get_value('money') >= 400:
        tem = gl.get_value('money')
        gl.set_value('money', tem - 300)
        new_rider = Rider()
        tem = gl.get_value('riders')
        tem.append(new_rider)
        gl.set_value('riders',tem)
        print('*****************')



def main():
    # 初始化
    clock = pygame.time.Clock()
    coordinate =[] # 坐标
    gl.set_value('money', 1000) # 设置钱
    gl.set_value('riders',[])
    running = True
    t = threading.Thread(target = input.input_event)
    t.start()

    while running:
        buy_riders() # 买骑手
        output.cartoon_output() #动画输出
        
    
    t.join()


if __name__ == '__main__':
    main()
