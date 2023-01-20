import pygame
import sys
from vec2 import Vec2
from game_classes import Player
from world import World
from assets_loader import player_img
from constants import FPS


pygame.init()
clock = pygame.time.Clock()

cropped = pygame.Surface((20, 30))
cropped.blit(player_img, (0, 0))

player = Player(Vec2(0, 0), 5, cropped)
world = World(20, 10, player)

time = 0

# Main game loop
while True:

    # Read input from player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_ESCAPE:
                sys.exit()

        player.handle_input(event)

    new_time = pygame.time.get_ticks() / 1000
    dt = new_time - time
    time = new_time
    
    player.update(dt)

    world.draw()
    pygame.display.flip()
    
    clock.tick(FPS)
