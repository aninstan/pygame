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
        self.pos = pos
        self.img = img


class Character(GameObject):
    def __init__(self, pos, img):
        super().__init__(pos, img)
