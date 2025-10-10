import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("first game!")

color_white = (255, 255, 255)
color_black = (0, 0, 255)

x, y = 10, 15
speed = 5
box_size = 50

clock = pygame.time.Clock()
fps_rate = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed

    if x < 0:
        x = 0
    if x + box_size > 500:
        x = 500 - box_size
    if y < 0:
        y = 0
    if y + box_size > 500:
        y = 500 - box_size

    screen.fill(color_white)
    pygame.draw.rect(screen, color_black, (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(fps_rate)

    