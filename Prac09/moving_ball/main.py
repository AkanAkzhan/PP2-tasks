import pygame
import sys
from ball import Ball

pygame.init()
WIDTH = 800
HEIGHT = 600
x = 400
y = 300
screen = pygame.display.set_mode((WIDTH,HEIGHT))
ball = Ball(x,y,25,20,WIDTH,HEIGHT)
pygame.display.set_caption("Moving Ball")

running = True


while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - 20 >= 25:
                    ball.move_up()
            if event.key == pygame.K_DOWN:
                if y + 20 <= HEIGHT - 25:
                    ball.move_down()
            if event.key == pygame.K_LEFT:
                if x - 20 >=25:
                    ball.move_left()
            if event.key == pygame.K_RIGHT:
                if x + 20 <= WIDTH - 25:
                    ball.move_right()

    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(ball.x, ball.y),ball.radius)

    pygame.display.flip()

pygame.qiut()
sys.exit()