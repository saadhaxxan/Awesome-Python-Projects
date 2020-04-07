import pygame
import time
pygame.init()
display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width,display_height))
pygame.display.update()

pygame.display.set_caption("Car Game")

clock = pygame.time.Clock()

def gameloop():
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
                quit()
                
