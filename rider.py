import pygame

class Rider(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手红.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 10
    # 向上运动
    def move_up(self):
        self.rect.top -= self.speed
    # 向下运动
    def move_down(self):
        self.rect.top += self.speed
    # 向左运动
    def move_left(self):
        self.rect.left -= self.speed
    # 向右运动
    def move_right(self):
        self.rect.right += self.speed
        