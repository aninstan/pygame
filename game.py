import pygame
import sys
from vec2 import Vec2
from world import World
from player import Player
from assets_loader import player_animation_list
from constants import FPS

pygame.init()
clock = pygame.time.Clock()






player = Player(Vec2(0, 0), 5, player_animation_list)

world = World(5, 5, player)

action = 0

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

    new_time = pygame.time.get_ticks()
    dt = new_time - time
    time = new_time

    player.animation_frame = int((time / FPS)) % player_animation_list.steps[action]


    
    player.update(dt)

    world.draw()


    pygame.display.flip()
    
    clock.tick(FPS)
