import pygame
import sys
import rider

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
    click = 0 # 鼠标点击 0/未点击/1/点击
    coordinate =[] # 坐标

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 如果鼠标点击
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # 如果未指定餐馆
                if click == 0:
                    click = 1
                    coordinate.append(pos)
                # 如果已指定餐馆
                else :
                    coordinate.append(pos)
                    # 选定骑手
                    #for each in riders:
                    qishou.move()
                        
        # 确定是否要买骑手
 #       buy_riders()

        # 绘制屏幕
        screen.fill((255, 255, 204))
        # 绘制房子
        for i in range(0, 900, 100):
            for j in range(0, 900, 100):
                screen.blit(house, (i, j))
        # 绘制骑手
        for each in riders:
#            each.move()
            screen.blit(each.image, each.rect)
 #       screen.blit(rider,(385, 385))
        pygame.display.update() 
        clock.tick(60) # 设置帧数


if __name__ == '__main__':
    main()