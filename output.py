import main
import pygame

def cartoon_output():
    # 绘制屏幕
    screen.fill((255, 255, 204))
    # 绘制房子
    for i in range(0, 900, 100):
        for j in range(0, 900, 100):
            screen.blit(house, (i, j))
    # 绘制骑手
    for each in riders:
        each.move() # 改变骑手位置
        screen.blit(each.image, each.rect)
    pygame.display.update() 
    clock.tick(60) # 设置帧数
