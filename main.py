import pygame
import sys
import rider
import threading
import input
import output

bg_size = width, height = 800, 800 #屏幕大小尺寸
screen = pygame.display.set_mode(bg_size) 
house1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/食客.png').convert_alpha()
house = pygame.transform.scale(house1, (100, 100))
pygame.display.set_caption('外卖订单派送系统')
riders = [] # 骑手序列
money = 1000 # 钱

def buy_riders():
    global money
    global riders
    while money >= 400:
        money -= 300
        new_rider = rider.Rider()
        riders.append(new_rider)
        print('1',money)



def main():
    # 初始化
    running = True
    clock = pygame.time.Clock()
    coordinate =[] # 坐标
    t = threading.Thread(target = input.input_event)
    t.start()

    while :
        
        output.cartoon_output()
        
    
    t.join()


if __name__ == '__main__':
    main()