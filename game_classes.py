from pygame import Surface
import math
from vec2 import Vec2
from constants import TILE_SIZE


class GameObject:
    def __init__(self, pos: Vec2, img: Surface):
        self.pos = pos
        self.img = img

    def draw(self, screen: Surface, offset: Vec2):
        screen.blit(self.img, (self.pos.x - offset.x, self.pos.y - offset.y))


class Bullet(GameObject):
    def __init__(self, pos: Vec2, direction: Vec2, vel: float, img: Surface):
        super().__init__(pos, img)
        self.direction = direction
        self.vel = vel
    
    def update_pos(self, dt: int):
        self.pos += self.direction.normalized() * (dt * TILE_SIZE * self.vel / 1000)


class Weapon(GameObject):
    def __init__(self, pos: Vec2, hand_to_tip: Vec2, bullet_velocity: Vec2, rotated_image_array: list[Surface], bullet_img: Surface):
        super().__init__(pos, rotated_image_array[0])
        self.hand_to_tip = hand_to_tip
        self.hand_to_tip_angle = math.atan(hand_to_tip.y / hand_to_tip.x)
        self.angle = 0
        self.rotated_image_array = rotated_image_array
        self.bullet_velocity = bullet_velocity
        self.bullet_img = bullet_img
        self.bullets: list[Bullet] = []
    
    def draw(self, screen: Surface, offset: Vec2):
        screen.blit(self.img, (self.pos.x - offset.x - self.img.get_width()/2, self.pos.y - offset.y - self.img.get_height()/2))

    def shoot(self):
        self.bullets.append(Bullet(self.pos + self.hand_to_tip, Vec2(math.cos(self.angle), math.sin(self.angle)), self.bullet_velocity, self.bullet_img))
    
    def update_bullets(self, dt: int):
        for bullet in self.bullets:
            bullet.update_pos(dt)
    
    def draw_bullets(self, screen: Surface, offset: Vec2):
        for bullet in self.bullets:
            bullet.draw(screen, offset)
