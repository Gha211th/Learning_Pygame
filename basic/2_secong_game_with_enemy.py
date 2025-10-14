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

# box size
box_size = 50

