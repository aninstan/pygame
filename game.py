import pygame
import sys
from vec2 import Vec2
from game_classes import Character
from world import World
from assets_loader import player_img
from constants import FPS


pygame.init()
clock = pygame.time.Clock()

world = World(10, 5)

player = Character(Vec2(0, 0), player_img)

# world.objects.append(player)

# Main game loop
while True:

    # Read input from player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            match event.key:

                case pygame.K_ESCAPE:
                    sys.exit()
            
            if event.key == pygame.K_w:
                player.pos.y -= 10
                world.offset.y -= 10
            
            if event.key == pygame.K_a:
                player.pos.x -= 10
                world.offset.x -= 10
            
            if event.key == pygame.K_s:
                player.pos.y += 10
                world.offset.y += 10
            
            if event.key == pygame.K_d:
                player.pos.x += 10
                world.offset.x += 10
            
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     player.pos.y -= 10
        #     world.offset.y -= 10
            
        # if keys[pygame.K_a]:
        #     player.pos.x -= 10
        #     world.offset.x -= 10
        
        # if keys[pygame.K_s]:
        #     player.pos.y += 10
        #     world.offset.y += 10
        
        # if keys[pygame.K_d]:
        #     player.pos.x += 10
        #     world.offset.x += 10
                
    
    world.draw()

    pygame.display.flip()
    clock.tick(FPS)
