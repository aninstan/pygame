import pygame
from screen import create_screen_and_canvas
from vec2 import Vec2
from game_classes import GameObject
from assets_loader import tile_img, player_img
from constants import TILE_SIZE


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen, self.canvas = create_screen_and_canvas()
        self.offset = Vec2(int(-self.canvas.get_rect().width/2), int(-self.canvas.get_rect().height/2))
        self.floortiles = []
        for y in range(height):
            for x in range(width):
                self.floortiles.append(GameObject(Vec2(x*TILE_SIZE - TILE_SIZE*width/2, y*TILE_SIZE - TILE_SIZE*height/2), tile_img))

    
    def draw(self):

        # Fill background
        self.canvas.fill((50, 50, 50))

        # Draw all game objects
        for object in self.floortiles:
            object.draw(self.canvas, self.offset)

        # Draw resized image on screen
        self.screen.blit(pygame.transform.scale(self.canvas, self.screen.get_rect().size), (0, 0))
        