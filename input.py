import main
import pygame
import rider

def change(coordinate):
    pos = []
    pos[0] = (coordinate[0] / 100) * 100 + 50
    pos[2] = (coordinate[2] / 100) * 100 + 50
    pos[1] = (coordinate[1] / 100) * 100 + 100
    pos[3] = (coordinate[3] / 100) * 100 + 100
    return pos
def input_event():
    print('1')
    click = 0 # 鼠标点击 0/未点击/1/点击x
    running = True
    tem_rider = rider.Rider # 暂时骑手
    while running:
        print('2')
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
                    order = change(cooridinate) # 将输入点转换
                    tem = riders[0]
                    # 将订单分配给适合的骑手
                    for each in riders:
                        distance1 = (tem.rect.left - order[0]) ** 2 + (tem.rect.top - order[1]) ** 2
                        distance2 = (each.rect.left - order[0]) ** 2 + (each.rect.top - order[1]) ** 2
                        if distance2 < distance1:
                            tem = each
                    tem.orders.append(order)
                    click = 0