from pygame import Surface
import math
from vec2 import Vec2
from game_classes import GameObject, Weapon
from animation import AnimationList
from constants import TILE_SIZE


class Character(GameObject):
    def __init__(self, pos: Vec2, hand_offset: Vec2, speed: float, animation_list: AnimationList, hand_img: Surface, weapon: Weapon):
        super().__init__(pos, animation_list.list[0][0])
        self.pos = pos
        self.hand_offset = hand_offset
        self.speed = speed
        self.direction = Vec2(0, 0)

        self.animation_list = animation_list
        self.animation_index = 0
        self.animation_frame = 0

        self.hand_img = hand_img

        self.weapon = weapon
        self.weapon.pos = pos + hand_offset

    def draw(self, screen: Surface, offset: Vec2):

        self.img = self.animation_list.list[self.animation_index][self.animation_frame]

        screen.blit(self.img, (self.pos.x - offset.x, self.pos.y - offset.y))
        self.weapon.draw(screen, offset)
        screen.blit(self.hand_img, (self.pos.x - offset.x + self.hand_offset.x - self.hand_img.get_width()/2, self.pos.y - offset.y + self.hand_offset.y - self.hand_img.get_height()/2))
        
        self.weapon.hand_to_tip = Vec2(math.cos(self.weapon.angle + self.weapon.hand_to_tip_angle), math.sin(self.weapon.angle + self.weapon.hand_to_tip_angle)) * self.weapon.hand_to_tip.abs()
        
        screen.blit(self.hand_img, (self.weapon.pos.x - offset.x + self.weapon.hand_to_tip.x, self.weapon.pos.y - offset.y + self.weapon.hand_to_tip.y))

    def update(self, dt: int):
        if (self.direction.abs() != 0):
            movement = self.direction.normalized() * (dt * TILE_SIZE * self.speed / 1000)
            self.pos += movement
            self.weapon.pos += movement