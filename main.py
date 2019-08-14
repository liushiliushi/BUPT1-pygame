import pygame
import sys
from rider import *
import threading
import input
import output



riders = [] # 骑手序列
money = 1000 # 钱

def buy_riders():
    global money
    global riders
    while money >= 400:
        money -= 300
        new_rider = Rider()
        riders.append(new_rider)
        print('*****************')



def main():
    # 初始化
    clock = pygame.time.Clock()
    coordinate =[] # 坐标
#    t = threading.Thread(target = input.input_event)
 #   t.start()

    while True:
        buy_riders()
        print('***', riders)
        output.cartoon_output()
        
    
  #  t.join()


if __name__ == '__main__':
    main()