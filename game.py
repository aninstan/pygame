import pygame
import sys
from screen import create_screen_and_canvas
from game_classes import GameObject

pygame.init()
clock = pygame.time.Clock()
FPS = 60

screen, canvas = create_screen_and_canvas()

tile = pygame.image.load("assets/testtile20px.png")

test = GameObject(100, 100, tile)

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
    
    canvas.fill((50, 50, 50))
    test.draw(canvas)

    screen.blit(pygame.transform.scale(canvas, screen.get_rect().size), (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
