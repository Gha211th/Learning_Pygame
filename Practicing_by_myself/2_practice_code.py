import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("practicing:)")

color_white = (255, 255, 255)
color_black = (0, 0, 255)
color_red = (255, 0, 0)

player_x = 100
player_y = 300
player_speed = 5
player_size = 50

enemy_x = 100
enemy_y = 400
enemy_speed = 5
enemy_size = 50

enemy_direct = 5

clock = pygame.time.Clock()
fps_target = 120

box_size = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if player_x < 0:
        player_x = 0
    if player_x + box_size > 500:
        player_x = 500 - box_size
    if player_y < 0:
        player_x = 0
    if player_y + box_size > 500:
        player_y = 500 - box_size
    
    screen.fill(color_white)
    pygame.draw.rect(screen, color_black, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, color_red, (enemy_x, enemy_y, enemy_size, enemy_size))
    pygame.display.flip()

    clock.tick(fps_target)
