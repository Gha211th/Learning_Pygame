# i just practice my skill at pygame
# without using ai A.K.A code by myself

import pygame
import sys

pygame.init()

# for window size and title
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pacticing my pygame skills")

# for color:
color_white = (255, 255, 255)

# for player
player = pygame.image.load("player.png")

# for movement
x, y = 50, 50
speed = 5

# for fps
clock = pygame.time.Clock()
fps_target = 120

# starting the game!
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()