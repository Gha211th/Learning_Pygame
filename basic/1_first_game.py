import pygame
import sys

pygame.init()

width, height = 500, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("first game!")

color_white = (255, 255, 255)
color_black = (0, 0, 255)

x, y = 10, 15
speed = 5
box_size = 50

margin = 50

clock = pygame.time.Clock()
fps_rate = 1000

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

    if x < margin:
        x = margin
    if x + box_size > width - margin:
        x = width - box_size - margin
    if y < margin:
        y = margin
    if y + box_size > height - margin:
        y = height - box_size - margin

    screen.fill(color_white)
    pygame.draw.rect(screen, color_black, (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(fps_rate)

    