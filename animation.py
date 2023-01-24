from spritesheet import SpriteSheet
from constants import BLACK


class AnimationList():
    def __init__(self, spritesheet: SpriteSheet, steps: list[int]):
        self.list = []
        self.steps = steps
        for n, animation in enumerate(steps):
            img_list = []
            for i in range(animation):
                img_list.append(spritesheet.get_image(i + n*animation, 20, 30, 1, BLACK))
            self.list.append(img_list)
