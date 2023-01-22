import pygame
from constants import TILE_SIZE, TILE_SCREEN_HEIGHT


def create_screen_and_canvas():

    # The main screen which the player will see
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Surface used to draw on. The actual image on the screen will be a resize of this screen
    canvas = pygame.Surface((TILE_SIZE*TILE_SCREEN_HEIGHT*screen.get_rect().width/screen.get_rect().height, TILE_SIZE*TILE_SCREEN_HEIGHT))

    return screen, canvas