#-*- coding: utf-8 -*-
import pygame
import random
pygame.init()#초기화

#화면크기 설정
screen_width = 500#가로
screen_height = 500#세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀(제목)
pygame.display.set_caption("똥피하기-코드플레이")
#FPS
clock = pygame.time.Clock()

#이속 고정
character_speed = 1
enemy_speed = 10

#이미지 불러오기(배경)
bg = pygame.image.load("pygame_original/source/background.png")#상대경로로 해야함

#스프라이트 불러오기
character = pygame.image.load("pygame_original/source/character.png")#상대경로로 해야됨

character_size = character.get_rect().size#가로 세로 크기 구하기
character_width = character_size[0]#위에서 얻은 1번째값
character_height = character_size[1]#위에서 얻은 2번째값
character_xPos = (screen_width / 2) - (character_width / 2)#가로화면 정중앙
character_yPos = screen_height - character_height#화면 세로 맨아래
to_x = 0
to_y = 0
#적군 생성
enemy = pygame.image.load("pygame_original/source/enemy.png")
#적군 크기, 위치 지정
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos =random.randint(0,(screen_width - enemy_width))
enemy_yPos = 0
#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(120) #게임 화면 초당 리프레시 횟수
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= character_speed
            elif event.key == pygame.K_d:
                to_x += character_speed
            elif event.key == pygame.K_w:
                to_y -= character_speed
            elif event.key == pygame.K_s:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0
    #추가한 이미지 화면에 띄우기
    character_xPos += to_x * dt#위치 반영
    character_yPos += to_y * dt#위치 반영
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
    
    enemy_yPos += enemy_speed
    if enemy_yPos > screen_height:
        enemy_yPos = 0
        enemy_speed = random.randint(10,25)
        enemy_xPos = random.randint(0, screen_width - enemy_width)

    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌!!!")
        running = False
    
    screen.blit(bg, (0,0))#blit:배경그리기
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    pygame.display.update()#화면 새로고침
    
#종료처리
pygame.quit()