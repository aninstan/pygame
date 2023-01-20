from vec2 import Vec2
from constants import TILE_SIZE


class Character():
    def __init__(self, pos, speed, animation_list):
        self.pos = pos
        self.speed = speed
        self.direction = Vec2(0, 0)
        self.animation_list = animation_list
        self.animation_index = 2
        self.animation_frame = 0

    def draw(self, screen, offset):
        screen.blit(self.animation_list.list[self.animation_index][self.animation_frame], (self.pos.x - offset.x, self.pos.y - offset.y))

    def update(self, dt):
        if (self.direction.abs() != 0):
            self.pos += self.direction.normalized().get_scaled(dt * TILE_SIZE * self.speed / 1000)