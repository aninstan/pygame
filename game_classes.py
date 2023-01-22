from pygame import Surface
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
    def __init__(self, pos: Vec2, grip_offset: Vec2, tip_offset: Vec2, bullet_velocity: Vec2, img: Surface, bullet_img: Surface):
        super().__init__(pos, img)
        self.grip_offset = grip_offset
        self.tip_offset = tip_offset
        self.direction = Vec2(1, 0)
        self.bullet_velocity = bullet_velocity
        self.bullet_img = bullet_img
        self.bullets: list[Bullet] = []
    
    def shoot(self):
        self.bullets.append(Bullet(self.pos + self.tip_offset, self.direction, self.bullet_velocity, self.bullet_img))
    
    def update_bullets(self, dt: int):
        for bullet in self.bullets:
            bullet.update_pos(dt)
    
    def draw_bullets(self, screen, offset):
        for bullet in self.bullets:
            bullet.draw(screen, offset)
