import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bouncing Ball Game')

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)

# 공 설정
ball_size = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3
ball_speed_y = 3

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 가장자리에 부딪히면 반대 방향으로 튕기기
    if ball_x <= 0 or ball_x >= screen_width - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y = -ball_speed_y

    # 화면 업데이트
    screen.fill(black)
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_size)
    pygame.display.flip()

    # FPS 설정
    clock.tick(60)

pygame.quit()
sys.exit()
