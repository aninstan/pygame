import pygame
import sys
from world import World
from assets_loader import player
from constants import FPS

pygame.init()
clock = pygame.time.Clock()

world = World(30, 30, player, 40)

# Main game loop
while True:

    # Read input from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_ESCAPE:
                sys.exit()

        world.handle_input(event)

    # Get time in milliseconds
    time = pygame.time.get_ticks()
    dt = clock.tick(FPS)

    world.update(time, dt)    

    world.draw()

    pygame.display.flip()
