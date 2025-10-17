#-*- coding: utf-8 -*-
import pygame
pygame.init()#초기화

#화면크기 설정
screen_width = 500#가로
screen_height = 500#세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀(제목)
pygame.display.set_caption("똥피하기-코드플레이")

#이미지 불러오기(배경)
bg = pygame.image.load("pygame_original/source/background.png")#상대경로로 해야함

#스프라이트 불러오기
character = pygame.image.load("pygame_original/source/character.png")#상대경로로 해야됨

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height /2) - (character_height / 2)
to_x = 0
to_y = 0
#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= 100
            elif event.key == pygame.K_d:
                to_x += 100
            elif event.key == pygame.K_w:
                to_y -= 100
            elif event.key == pygame.K_s:
                to_y += 100
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0
    #추가한 이미지 화면에 띄우기
    character_xPos += to_x#위치 반영
    character_yPos += to_y#위치 반영
    #가로화면 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    #세로화면 안벗어나게
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height
    
    screen.blit(bg, (0,0))#blit:배경그리기
    screen.blit(character, (character_xPos, character_yPos))
    pygame.display.update()#화면 새로고침
    
#종료처리
pygame.quit()