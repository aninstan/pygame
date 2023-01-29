import pygame
from vec2 import Vec2
import animation
from spritesheet import SpriteSheet


tile_img = pygame.image.load("assets/testtile20px.png")

player_sprite_sheet_image = pygame.image.load('assets/character_animations.png')
player_sprite_sheet = SpriteSheet(player_sprite_sheet_image)
player_animation_list = animation.AnimationList(player_sprite_sheet, [4, 4, 4, 4, 4, 4, 4, 4])

gun_img = pygame.image.load("assets/gun.png")
rotated_gun_array = animation.create_rotated_image_array(gun_img, Vec2(13, 12), 90)

bullet_img = pygame.image.load("./assets/bullet.png")
hand_img = pygame.image.load("./assets/hand.png")
