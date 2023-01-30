import pygame
import copy
import sys
from world import World
from assets_loader import player_animation_list, player
from constants import FPS, TILE_SIZE

pygame.init()
clock = pygame.time.Clock()


world = World(26, 16, player)


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

    # Change animation frame of player based on total elapsed time
    player.animation_frame = int((time / FPS / 3)) % player_animation_list.steps[player.animation_index]

    if (player.direction.abs() > 0):
        player.animation_index = 4
    else:
        player.animation_index = 0

    # No need to update character if it is standing still
    if (player.direction.abs() != 0):

        player.update(dt)

        player_out_of_bounds_pos_change = copy.deepcopy(player.pos)
        world.fix_out_of_bounds(player)
        player_out_of_bounds_pos_change -= player.pos
        
        world.offset += player.direction.normalized() * (dt * TILE_SIZE * player.speed / 1000) - player_out_of_bounds_pos_change


    for gunner in world.gunners:
        world.fix_out_of_bounds(gunner)


    player.weapon.update_bullets(dt)

    a = 0

    while a < len(player.weapon.bullets):
        if (world.out_of_bounds(player.weapon.bullets[a])):
            del player.weapon.bullets[a]
        a += 1

    world.draw()

    pygame.display.flip()
    
