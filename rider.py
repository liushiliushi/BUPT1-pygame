import pygame

class Rider(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手红.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        