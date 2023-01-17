class GameObject:
    def __init__(self, pos, img):
        self.pos = pos
        self.img = img
    

    def draw(self, screen, offset):
        screen.blit(self.img, (self.pos.x - offset.x, self.pos.y - offset.y))


class Character(GameObject):
    def __init__(self, pos, img):
        super().__init__(pos, img)
