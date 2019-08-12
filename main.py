import pygame
import sys

bg_size = width, height = 800, 800 #屏幕大小尺寸
screen = pygame.display.set_mode(bg_size) 
rider1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手小.png').convert_alpha()
house1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/食客.png').convert_alpha()
house = pygame.transform.scale(house1, (100, 100))
rider = pygame.transform.scale(rider1, (30, 30))
pygame.display.set_caption('外卖订单派送系统')

def main():
    # 初始化
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 204))
        # 绘制房子
        for i in range(0, 900, 100):
            for j in range(0, 900, 100):
                screen.blit(house, (i, j))
        screen.blit(rider,(385, 385))
        pygame.display.update() 
        clock.tick(60) # 设置帧数

if __name__ == '__main__':
    main()