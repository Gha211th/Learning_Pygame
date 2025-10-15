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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
