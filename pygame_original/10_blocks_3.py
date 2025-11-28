#-*- coding: utf-8 -*-
import pygame
import random
pygame.init() #초기화(반드시 필요)

#화면크기 설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀(제목창)
pygame.display.set_caption("뼊똘꼐끼")

#막대기 정의
bar_width = screen_width / 4
bar_height = screen_height / 20

bar_xPos = screen_width / 2 - bar_width / 2
bar_yPos = screen_height - bar_height
bar_rect = pygame.Rect(bar_xPos, bar_yPos, bar_width, bar_height)
bar_to_X = 0

#공 정의
ball_size = 20

ball_xPos = screen_width / 2
ball_yPos = screen_height - bar_height - ball_size

ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_xPos, ball_yPos)

ball_x_speed = 5
ball_y_speed = 1

#블록 정의
block_width = screen_width / 10
block_height = screen_height / 20

block_xPos = 0
block_yPos = 0

blocks = [[] for _ in range(10)]
block_color = [[] for _ in range(10)]

for i in range(10):
    for j in range(3):
        blocks[i].append(pygame.Rect(i*block_width, j*block_height, block_width, block_height))
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256)))

#마우스로 막대기 조작
mouse_xPos = 0
mouse_yPos = 0
#점수
point = 0
#글자 출력
pygame.font.init()

def gameText(words): #매개변수로 받는 내용 출력
    font = pygame.font.SysFont(None, 100)#폰트 지정

    text = font.render(words, True, (255,50,50))#글자내용,색상지정

    text_width = text.get_rect().size[0]#택스트 가로,세로 크기지정
    text_height = text.get_rect().size[1]

    text_xPos = screen_width / 2 - text_width / 2 #택스트 위치 지정
    text_yPos = screen_height / 2 - text_height / 2

    screen.blit(text, (text_xPos, text_yPos))#택스트 갱신

def gameTText(words): #매개변수로 받는 내용 출력
    font = pygame.font.SysFont(None, 100)#폰트 지정

    text = font.render(words, True, (255, 50, 50))#글자내용,색상지정

    text_width = text.get_rect().size[0]#택스트 가로,세로 크기지정
    text_height = text.get_rect().size[1]

    text_xPos = screen_width / 2 - text_width / 2 #택스트 위치 지정
    text_yPos = 0

    screen.blit(text, (text_xPos, text_yPos))#택스트 갱신

#카운트 시작
count = True
#이벤트루프
running = True
while running:
    if count:
        count = False
        for i in range(3,0,-1):
            screen.fill((0,0,0))
            gameText(str(i))
            pygame.display.update()
            pygame.time.delay(1000)
        screen.fill((0,0,0))
        gameText("Go!")
        pygame.display.update()
        pygame.time.delay(1000)

    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
        
        if event.type == pygame.MOUSEMOTION:
            mouse_xPos, mouse_yPos = pygame.mouse.get_pos()
            if mouse_xPos - bar_width / 2 >= 0 and mouse_xPos + bar_width / 2 <= screen_width:
                bar_xPos = mouse_xPos - bar_width / 2
                bar_rect.left = mouse_xPos - bar_width / 2
    
    #배경그리기
    screen.fill((200,200,100))
    #막대기 그리기
    if bar_xPos < 0:
        bar_xPos = 0
    if bar_xPos > screen_width - bar_width:
        bar_xPos = screen_width - bar_width
    bar_rect.left = bar_xPos
    
    pygame.draw.rect(screen, (90,90,225), bar_rect)
    
    #공 튕기기
    if ball_xPos - ball_size <= 0:
        ball_x_speed = -ball_x_speed
    elif ball_xPos >= screen_width - ball_size:
        ball_x_speed = -ball_x_speed

    if ball_yPos - ball_size <= 0:
        ball_y_speed = -ball_y_speed
    elif ball_yPos >= screen_height - ball_size:
        #ball_y_speed = -ball_y_speed
        screen.fill((0,0,0))
        gameText(f"점수: {point}")
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    ball_xPos += ball_x_speed
    ball_yPos += ball_y_speed

    #공 그리기
    ball_rect.center = (ball_xPos, ball_yPos)
    pygame.draw.circle(screen, (255,255,255), (ball_xPos, ball_yPos), ball_size)
    #충돌판정
    if ball_rect.colliderect(bar_rect):
        ball_y_speed *= -1
    #벽돌 그리기
    for i in range(10):
        for j in range(3):
            if blocks[i][j]:    
                pygame.draw.rect(screen, block_color[i][j], blocks[i][j])
                blocks[i][j].topleft = (i*block_width, j*block_height)

                if ball_rect.colliderect(blocks[i][j]):
                    ball_x_speed *= -1
                    ball_y_speed *= -1
                    blocks[i][j] = 0
                    point += 1
                    
    if point >= 30:
        screen.fill((0,255,0))
        gameText(f"{timer}초 만에 클리어!")
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    timer = (pygame.time.get_ticks() // 1000) - 4
    gameTText(f"{timer}")
    pygame.display.update()
#종료 처리
pygame.quit()