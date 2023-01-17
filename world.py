import pygame
from screen import create_screen_and_canvas
from vec2 import Vec2


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen, self.canvas = create_screen_and_canvas()
        self.objects = []
        self.offset = Vec2(-self.canvas.get_rect().width/2, -self.canvas.get_rect().height/2)

    
    def draw(self):

        # Fill background
        self.canvas.fill((50, 50, 50))

        # Draw all game objects
        for object in self.objects:
            object.draw(self.canvas, self.offset)

        # Draw resized image on screen
        self.screen.blit(pygame.transform.scale(self.canvas, self.screen.get_rect().size), (0, 0))
        