import pygame
from vec2 import Vec2
from spritesheet import SpriteSheet
from constants import BLACK


class AnimationList:
    def __init__(self, spritesheet: SpriteSheet, steps: list[int]):
        self.list = []
        self.steps = steps
        for n, animation in enumerate(steps):
            img_list = []
            for i in range(animation):
                img_list.append(spritesheet.get_image(i + n*animation, 20, 30, 1, BLACK))
            self.list.append(img_list)


def create_rotated_image_array(img: pygame.Surface, center: Vec2, size: int):
    
    new_img = pygame.Surface((img.get_width()*2 - center.x, img.get_height()*2 - center.y))
    new_img.blit(img, (new_img.get_width()*0.5 - center.x, new_img.get_height()*0.5 - center.y))
    new_img.set_colorkey(BLACK)
    arr = [new_img]
    
    for i in range(size - 1):
        arr.append(pygame.transform.rotate(new_img, -i / size * 360))

    return arr