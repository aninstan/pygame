import pygame
from math import cos, sin, pi
from vec2 import Vec2
from constants import TILE_SIZE


class GameObject:
    def __init__(self, pos, img):
        self.pos = pos
        self.img = img

    def draw(self, screen, offset):
        screen.blit(self.img, (self.pos.x - offset.x, self.pos.y - offset.y))


class Bullet(GameObject):
    def __init__(self, pos, vel, img):
        super().__init__(pos, img)
        self.vel = vel
    
    def update_pos(self):
        self.pos += self.vel


class Weapon(GameObject):
    def __init__(self, pos, img):
        super().__init__(pos, img)


class Character(GameObject):
    def __init__(self, pos, speed, img):
        super().__init__(pos, img)
        self.direction = Vec2(0, 0)
        self.speed = speed

    def update(self, dt):
        self.pos += self.direction.get_scaled(dt * TILE_SIZE * self.speed)


class Player(Character):
    def __init__(self, pos, speed, img):
        super().__init__(pos, speed, img)
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
