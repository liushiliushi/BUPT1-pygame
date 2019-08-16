import pygame
import globalvar as gl

class Rider(pygame.sprite.Sprite):
    def __init__(self, bianhao):
        pygame.sprite.Sprite.__init__(self) # 初始化
        
        rider1 = pygame.image.load('C:/Users/lalala/Documents/GitHub/BUPT1-pygame/素材/骑手小.png').convert_alpha()
        self.image = pygame.transform.scale(rider1, (30, 30))
        self.rect = self.image.get_rect()
        self.speed = 10 # 速度
        self.rect.left, self.rect.top = 435, 385 #初始化骑手位置
        self.orders = []
        self.state = 0 #骑手状态 0/空闲/1/取餐/2/送餐
        self.num = bianhao # 骑手编号
        self.order_num = 0
        self.spe = False # 初始化，不是特殊情况
    
    # 加入订单
    def add_order(self, pos):
        self.orders.append(pos)
  
    # 运动
    def move(self):
        # 确定目标点x, y
        if self.state == 0: # 如果空闲
            self.spe = False # 初始化，不是特殊情况
            # 看骑手还有无订单
            if self.orders == []:
                pass
            else:
                self.state = 1 # 改变状态为取餐
        else: # 如果取餐或者送餐
            if self.state == 1: # 如果去取餐
                # 确定目标点
                x = self.orders[0][0] - 15
                y = self.orders[0][1] - 15
              
            else: # 如果去送餐
                # 确定目标点
                x = self.orders[0][2] - 15
                y = self.orders[0][3] - 15
            print(x, y)
            if y == self.rect.top: # 如果骑手和目标点在一条街上
                print('已到达同一条街')
                if x < self.rect.left: # 如果目标点在骑手左侧
                    print('向左运动')
                    self.rect.left -= self.speed # 骑手向左运动
                elif x > self.rect.left : # 如果目标点在骑手右侧
                    print('向右运动')
                    self.rect.left += self.speed # 骑手向右运动
                else : # 如果骑手已到达目标点
                    print('到达目标点')
                    # 如果骑手去取餐
                    if self.state == 1:
                        self.state = 2 # 改变状态为送餐
                        print('改为送餐')
                    # 如果骑手去送餐
                    else:
                        print('此单送到')
                        self.state = 0 # 改变状态为空闲
                        self.orders.pop(0) # 删除骑手已完成的这个订单

            elif y < self.rect.top: # 如果骑手在目标点下方
                print('骑手在下方')
                if (self.rect.left + 15) % 100 == 0: # 如果骑手在纵街道上或者在交叉点上
                    print('到达纵街道')
                    self.rect.top -= self.speed
                    if self.spe:
                        self.spe = not self.spe # 不是特殊情况了
                        print('情况变正常')
                else :
                    if x < self.rect.left or self.spe: # 如果目标点在骑手左侧或者特殊情况
                        print('向左运动')
                        self.rect.left -= self.speed # 骑手向左运动
                    elif x == self.rect.left: # 如果目标点在骑手同一方位
                        print('在同一x方位，情况特殊')
                        self.spe = True # 特殊情况特殊对待
                        self.rect.left -= self.speed # 骑手向左运动
                    elif x > self.rect.left and not self.spe: # 如果目标点在骑手右侧且不是特殊情况
                        print('向右运动')
                        self.rect.left += self.speed # 骑手向右运动
            else: # 如果骑手在目标点上方
                print(self.rect)
                print('骑手在上方')
                if (self.rect.left + 15) % 100 == 0: # 如果骑手在纵街道上或者在交叉点上
                    print('在交叉点上')
                    self.rect.top += self.speed
                    if self.spe:
                        self.spe = not self.spe # 不是特殊情况了
                else :
                    if x < self.rect.left or self.spe: # 如果目标点在骑手左侧
                        print('向左运动')
                        self.rect.left -= self.speed # 骑手向左运动
                    elif x == self.rect.left: # 如果目标点在骑手同一方位
                        print('在同一方位，情况特殊')
                        self.spe = True # 特殊情况特殊对待
                        self.rect.left -= self.speed # 骑手向左运动
                    elif x > self.rect.left and not self.spe: # 如果目标点在骑手右侧且不是特殊情况
                        print('向右运动')
                        self.rect.left += self.speed # 骑手向右运动



        

        

        