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
    click = 0 # 鼠标点击 0/未点击/1/点击x
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
                    order = change(cooridinate) # 将输入点转换
                    
                    click = 0