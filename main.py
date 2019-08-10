import pygame
import sys

bg_size = width, height = 900, 600 #屏幕大小尺寸
screen = pygame.display.set_mode(bg_size) 
rider = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手红.jpg')
pygame.display.set_caption('外卖订单派送系统').convert()

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
        pygame.display.update() 
        clock.tick(60) # 设置帧数

if __name__ == '__main__':
    main()