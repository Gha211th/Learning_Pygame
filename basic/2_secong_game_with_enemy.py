import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my second game with enemy")

# for color
color_white = (255, 255, 255)
color_black = (0, 0, 255)
color_red = (255, 0, 0)

# for player
player_x = 100
player_y = 400
player_size = 50
player_speed = 5

# for enemy
enemy_x = 100
enemy_y = 200
enemy_size = 50
enemy_speed = 10

# enemy direction
enemy_direct = 1

# for fps
clock = pygame.time.Clock()
fps_target = 120

# limit space
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
    if player_x + box_size < 500:
        x = 500 - box_size
    if player_y < 0:
        player_y = 0
    if player_y + box_size < 500:
        y = 500 - box_size
    
    screen.fill(color_white)
    pygame.draw.rect(screen, color_black, (player_x, player_y, player_size, player_size))
    pygame.display.flip()
    clock.tick(fps_target)
