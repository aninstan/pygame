import pygame
import copy
import sys
from vec2 import Vec2
from world import World
from character import Character
from game_classes import Weapon
from assets_loader import player_animation_list, gun_img, bullet_img, hand_img
from constants import FPS, TILE_SIZE

pygame.init()
clock = pygame.time.Clock()

gun = Weapon(Vec2(0, 0), Vec2(5, 10), Vec2(45, 5), 15, gun_img, bullet_img)

player = Character(Vec2(-10, -15), Vec2(15, 23), 5, player_animation_list, hand_img, gun)

world = World(15, 20, player)


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

    player.animation_frame = int((time / FPS / 3)) % player_animation_list.steps[player.animation_index]

    if (player.direction.abs() != 0):

        player.update(dt)

        player_wall_collision_pos_change = copy.deepcopy(player.pos)
        world.check_wall_collision(player)
        player_wall_collision_pos_change -= player.pos
        
        world.offset += player.direction.normalized() * (dt * TILE_SIZE * player.speed / 1000) - player_wall_collision_pos_change


    player.weapon.update_bullets(dt)

    world.draw()

    pygame.display.flip()
    
