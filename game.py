import pygame
import sys
from vec2 import Vec2
from game_classes import GameObject
from assets_loader import tile_img
from world import World


pygame.init()
clock = pygame.time.Clock()
FPS = 60

world = World(200, 200)

tile = GameObject(Vec2(0, 0), tile_img)

world.objects.append(tile)

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
                
                case pygame.K_LEFT:
                    world.offset.x -= 10
                
                case pygame.K_RIGHT:
                    world.offset.x += 10
                
                case pygame.K_DOWN:
                    world.offset.y -= 10
                
                case pygame.K_UP:
                    world.offset.y += 10
                
    
    world.draw()

    pygame.display.flip()
    clock.tick(FPS)
