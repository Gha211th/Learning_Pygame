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
color_black = (0, 0, 255)

# for movement
x, y = 50, 50
speed = 5

# limit space
box_size = 10

# for fps
clock = pygame.time.Clock()
fps_target = 300

# starting the game!
while True:
    # to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    # for movement:
    keys = pygame.key.get_pressed()

    # for wasd or row
    if keys[pygame.K_UP or pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN or pygame.K_s]:
        y += speed
    if keys[pygame.K_RIGHT or pygame.K_d]:
        x += speed
    if keys[pygame.K_LEFT or pygame.K_a]:
        x -= speed


    # limit space
    if x < 0:
        x = 0
    if x + box_size > 500:
        x = 500 - box_size
    if y < 0:
        y = 0
    if y + box_size > 500:
        y = 500 - box_size
    
    # initialize the window
    screen.fill(color_white)
    pygame.draw.rect(screen, color_black, (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(fps_target)