import pygame
from math import cos, sin, pi
from vec2 import Vec2
from character import Character


class Player(Character):
    def __init__(self, pos, speed, animation_list):
        super().__init__(pos, speed, animation_list)
        self.key_count = 0
        self.angle = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w:
                    self.key_count += 1
                    self.angle += 3*pi/2

                case pygame.K_a:
                    self.key_count += 1
                    self.angle += pi

                case pygame.K_s:
                    self.key_count += 1
                    self.angle += pi/2
                    

                case pygame.K_d:
                    self.key_count += 1
                    # self.angle += 2*pi

        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w:
                    self.key_count -= 1
                    self.angle -= 3*pi/2

                case pygame.K_a:
                    self.key_count -= 1
                    self.angle -= pi

                case pygame.K_s:
                    self.key_count -= 1
                    self.angle -= pi/2
                    
                case pygame.K_d:
                    self.key_count -= 1
                    # self.angle -= 2*pi
        
        if (self.key_count == 0):
            self.direction = Vec2(0, 0)
        else:
            self.direction = Vec2(cos(self.angle / self.key_count), sin(self.angle / self.key_count))
        
        if (self.direction.x < 0):
            self.animation_index = 1
        elif (self.direction.x > 0):
            self.animation_index = 0
