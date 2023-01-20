import pygame
from math import cos, sin, pi
from vec2 import Vec2
from character import Character


class Player(Character):
    def __init__(self, pos, speed, animation_list):
        super().__init__(pos, speed, animation_list)
        self.direction = Vec2(0, 0)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w:
                    self.direction += Vec2(0, -1)

                case pygame.K_a:
                    self.direction += Vec2(-1, 0)

                case pygame.K_s:
                    self.direction += Vec2(0, 1)

                case pygame.K_d:
                    self.direction += Vec2(1, 0)

        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w:
                    self.direction -= Vec2(0, -1)

                case pygame.K_a:
                    self.direction -= Vec2(-1, 0)

                case pygame.K_s:
                    self.direction -= Vec2(0, 1)

                case pygame.K_d:
                    self.direction -= Vec2(1, 0)
        
        if (self.direction.x < 0):
            self.animation_index = 1
        elif (self.direction.x > 0):
            self.animation_index = 0
