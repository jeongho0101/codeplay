#-*- coding: utf-8 -*-
import pygame
import random
pygame.init()#초기화

#화면크기 설정
screen_width = 800#가로
screen_height = 800#세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀(제목)
pygame.display.set_caption("그리기")
#FPS
clock = pygame.time.Clock()

r = 120
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((220,165,95))

    # pygame.draw.line(1,2,3,4,5)#1.그리는곳 2.색지정 3.시작지점 4.끝지점 5.굵기
    # pygame.draw.line(screen, (0, 55, 0), (0,0),(screen_width,screen_height),50)
    # pygame.draw.line(screen,(0,0,0),(0,screen_height), (screen_width, 0),50)

    # measure = screen_width / 10

    # for i in range(10):
    #     pygame.draw.line(screen,(0,0,0),(0,i*measure), (screen_width, i*measure),2)
    #     pygame.draw.line(screen,(0,0,0),(i*measure,0), (i*measure, screen_height),2)
    ll = 760 // 18
    offset = 22
    for i in range(0,800,ll):
        pygame.draw.line(screen,(0,0,0),(i+offset,0),(i+offset,800))
    for i in range(0,800,ll):
        pygame.draw.line(screen,(0,0,0),(0,i+offset),(800,i+offset))
    
    pygame.draw.line(screen,(0,0,0),(0,0),(0,screen_width),offset*2)
    pygame.draw.line(screen,(0,0,0),(screen_height,0),(screen_height,screen_width),offset*2)
    pygame.draw.line(screen,(0,0,0),(0,0),(screen_height,0),offset*2)
    pygame.draw.line(screen,(0,0,0),(0,screen_width),(screen_height,screen_width),offset*2)
    
    
    start_point = (ll*3) + offset
    for k in range(3):
        for i in range(3):
            pygame.draw.circle(screen,(0,0,0),(start_point+(k*(6*ll)),start_point+(i*(6*ll))),ll/8)

    pygame.display.update()

pygame.quit()
