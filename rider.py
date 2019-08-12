import pygame

class Rider(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 初始化
        
        rider1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手小.png').convert_alpha()
        self.image = pygame.transform.scale(rider1, (30, 30))
        self.rect = self.image.get_rect()
        self.speed = 10 # 速度
        self.rect.left, self.rect.top = 385, 385 #初始化骑手位置

    # 运动
    def move(self,pos):
        

        