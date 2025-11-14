#-*- coding: utf-8 -*-
import pygame
pygame.init() #초기화(반드시 필요)

#화면크기 설정
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀(제목창)
pygame.display.set_caption("태극기")

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인

while running: #반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (50,100),(150,30),15)
    pygame.draw.line(screen, (0,0,0), (50,120),(150,50),15)
    pygame.draw.line(screen, (0,0,0), (50,140),(150,70),15)

    pygame.draw.line(screen, (0,0,0), (350,30),(450,100),15)
    pygame.draw.line(screen, (255,255,255), (400,10),(400,100),5)
    pygame.draw.line(screen, (0,0,0), (350,70),(450,140),15)
    pygame.draw.line(screen, (255,255,255), (400,10),(400,140),5)
    pygame.draw.line(screen, (0,0,0), (350,50),(450,120),15)

    pygame.draw.line(screen, (0,0,0), (50,380),(150,450),15)
    pygame.draw.line(screen, (255,255,255), (100,380),(100,450),5)
    pygame.draw.line(screen, (0,0,0), (50,360),(150,430),15)
    pygame.draw.line(screen, (0,0,0), (50,400),(150,470),15)

    pygame.draw.line(screen, (0,0,0), (350,470),(450,400),15)
    pygame.draw.line(screen, (0,0,0), (350,450),(450,380),15)
    pygame.draw.line(screen, (0,0,0), (350,430),(450,360),15)
    pygame.draw.line(screen, (255,255,255), (400,380),(400,450),5)

    pygame.draw.circle(screen,(200,0,0), (250,250),120,draw_top_right=True,draw_top_left=True)
    pygame.draw.circle(screen,(0,0,200), (250,250),120,draw_bottom_right=True,draw_bottom_left=True)
    pygame.draw.circle(screen,(200,0,0), (190,250),60)
    pygame.draw.circle(screen,(0,0,200), (310,250),60)

    pygame.display.update()
#종료처리
pygame.quit()