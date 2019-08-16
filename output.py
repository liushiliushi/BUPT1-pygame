import main
import pygame
import globalvar as gl
import rider
from pygame.locals import *

bg_size = width, height = 800, 800 #屏幕大小尺寸
screen = pygame.display.set_mode(bg_size) 
house1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/食客.png').convert_alpha()
house = pygame.transform.scale(house1, (100, 100))
pygame.display.set_caption('外卖订单派送系统')

def buy_riders():
    while gl.get_value('money') >= 400:
        tem = gl.get_value('money')
        gl.set_value('money', tem - 300)
        new_rider = rider.Rider()
        tem = gl.get_value('riders')
        tem.append(new_rider)
        gl.set_value('riders',tem)

def cartoon_output():
    clock = pygame.time.Clock()
    while True:
        # 确定是否要买骑手
        buy_riders()
        # 绘制屏幕
        global screen
        screen.fill((255, 255, 204))
        # 绘制房子
        for i in range(0, 900, 100):
            for j in range(0, 900, 100):
                screen.blit(house, (i, j))
        # 绘制骑手
        for each in gl.get_value('riders'):
            each.move() # 改变骑手位置
            screen.blit(each.image, each.rect)
        pygame.display.update() # 更新
        clock.tick(60) # 设置帧数
