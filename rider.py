import pygame
import globalvar as gl

class Rider(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 初始化
        
        rider1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手小.png').convert_alpha()
        self.image = pygame.transform.scale(rider1, (30, 30))
        self.rect = self.image.get_rect()
        self.speed = 10 # 速度
        self.rect.left, self.rect.top = 385, 385 #初始化骑手位置
        self.orders = []
        self.state = 0 #骑手状态 0/空闲/1/取餐/2/送餐
    
    # 加入订单
    def add_order(self, pos):
        self.orders.append(pos)

    # 运动
    def move(self):
        # 确定目标点x, y
        if self.state == 0: # 如果空闲
            pass
        else:
            if self.state == 1: # 如果去取餐
                # 确定目标点
                x = self.orders[0][0] - 15
                y = self.orders[0][1] - 15
                
            else: # 如果去送餐
                # 确定目标点
                x = self.orders[0][2] - 15
                y = self.orders[0][3] - 15
            
            if y == self.rect.top: # 如果骑手和目标点在一条街上
                if x < self.rect.left: # 如果目标点在骑手左侧
                    self.rect.left -= self.speed # 骑手向左运动
                elif x > self.rect.left : # 如果目标点在骑手右侧
                    self.rect.left += self.speed # 骑手向右运动
                else : # 如果骑手已到达目标点
                    pass
            elif y > self.rect.top: # 如果骑手在目标点下方
                if (self.rect.left + 15) % 100 == 0: # 如果骑手在纵街道上或者在交叉点上
                    self.rect.top += self.speed
                else :
                    if x <= self.rect.left: # 如果目标点在骑手左侧或者同一方位
                        self.rect.left -= self.speed # 骑手向左运动
                    else: # 如果目标点在骑手右侧
                        self.rect.left += self.speed # 骑手向右运动
            else: # 如果骑手在目标点上方
                if (self.rect.left + 15) % 100 == 0: # 如果骑手在纵街道上或者在交叉点上
                    self.rect.top - self.speed
                else :
                    if x <= self.rect.left: # 如果目标点在骑手左侧或者同一方位
                        self.rect.left -= self.speed # 骑手向左运动
                    else: # 如果目标点在骑手右侧
                        self.rect.left += self.speed # 骑手向右运动



        

        

        