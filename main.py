import pygame
import sys
from rider import *
import threading
import output
import globalvar as gl

gl._init()  # initialize
pygame.init()  # initialize

gl.set_value('bianhao', 0) # 初始化骑手编号
# 转换坐标函数
def change(coordinate):
    pos = []
    pos.append((coordinate[0] // 100) * 100 + 50) 
    pos.append((coordinate[1] // 100) * 100 + 100)
    pos.append((coordinate[2] // 100) * 100 + 50) 
    pos.append((coordinate[3] // 100) * 100 + 100)
    return pos

def main():
    # 初始化
        clock = pygame.time.Clock()
        coordinate = []  # 坐标
        gl.set_value('money', 1000)  # 设置钱
        gl.set_value('riders', [])
        gl.set_value('running',True)
        t = threading.Thread(target=output.cartoon_output)
        # 输出
        t.start()
        # 输入
        click = 0
        while gl.get_value('running'):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gl.set_value('running', False)
                                pygame.quit()
                                sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                # 如果未指定餐馆
                                if click == 0:
                                        click = 1
                                        coordinate.extend(pos)
                                # 如果已指定餐馆
                                else :
                                        click = 0 # 转换状态
                                        coordinate.extend(pos)
                                        print(coordinate)
                                        order = change(coordinate) # 将输入点转换
                                        print(order)
                                        coordinate = [] # 清空
                                        tem = gl.get_value('riders')[0]
                                        # 将订单分配给适合的骑手
                                        for each in gl.get_value('riders'):
                                                distance1 = (tem.rect.left - order[0]) ** 2 + (tem.rect.top - order[1]) ** 2
                                                distance2 = (each.rect.left - order[0]) ** 2 + (each.rect.top - order[1]) ** 2
                                                if distance2 < distance1:
                                                        tem = each
                                        print(tem.num)
                                        tem.orders.append(order)
                                        #tem.order_num + = 1
                                
                                        
                        else:
                                pass
        
        t.join()

if __name__ == '__main__':
        main()
