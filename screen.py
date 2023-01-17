import pygame


def create_screen_and_canvas():
    # The number of tiles necessary to cover the screen height
    tile_screen_height = 10

    # The size of the default tile image in pixels
    tile_size_px = 20

    # The main screen which the player will see
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Surface used to draw on. The actual image on the screen will be a resize of this screen
    canvas = pygame.Surface((tile_size_px*tile_screen_height*screen.get_rect().width/screen.get_rect().height, tile_size_px*tile_screen_height))

    return screen, canvas