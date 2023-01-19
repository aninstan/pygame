import pygame
from constants import TILE_SIZE


def create_screen_and_canvas():
    # The number of tiles necessary to cover the screen height
    tile_screen_height = 10

    # The main screen which the player will see
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Surface used to draw on. The actual image on the screen will be a resize of this screen
    canvas = pygame.Surface((TILE_SIZE*tile_screen_height*screen.get_rect().width/screen.get_rect().height, TILE_SIZE*tile_screen_height))

    return screen, canvas